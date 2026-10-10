#!/usr/bin/env python3
"""Report missing internal href/src targets in a built Hugo site.

Standard library only. Existing findings are advisory unless --strict is used.
External links, anchors and factual accuracy require separate review.
"""
import argparse
from collections import defaultdict
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []

    def handle_starttag(self, tag, attrs):
        self.urls.extend(value for key, value in attrs
                         if key in {"href", "src"} and value)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", nargs="?", default="public")
    parser.add_argument("--base-url", default="https://giacomorondina.org/")
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()
    root = Path(args.directory).resolve()
    pages = sorted(root.rglob("*.html"))
    if not pages:
        parser.error("No HTML files found; build the site with Hugo first.")
    origin = urlsplit(args.base_url)
    missing = defaultdict(set)
    for page in pages:
        relative = page.relative_to(root).as_posix()
        page_url = urljoin(args.base_url, relative)
        links = Links()
        links.feed(page.read_text(encoding="utf-8"))
        for raw in links.urls:
            if raw.startswith("#"):
                continue
            target = urlsplit(urljoin(page_url, raw))
            if target.scheme not in {"http", "https"} or target.netloc != origin.netloc:
                continue
            path = unquote(target.path)
            candidate = (root / path.lstrip("/")).resolve()
            if not candidate.is_relative_to(root):
                missing[path].add(relative)
                continue
            if not candidate.is_file() and not (candidate / "index.html").is_file():
                missing[path].add(relative)
    print(f"Checked {len(pages)} HTML files; {len(missing)} missing internal targets.")
    for target, sources in sorted(missing.items()):
        names = ", ".join(sorted(sources)[:5])
        extra = f" (+{len(sources)-5} more)" if len(sources) > 5 else ""
        print(f"- {target}: {names}{extra}")
    print("External URLs, PDF contents, dates and factual consistency need separate review.")
    return 1 if args.strict and missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
