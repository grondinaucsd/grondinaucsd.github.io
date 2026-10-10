#!/usr/bin/env bash
# Replace the public CV only after a successful two-pass compilation.
set -euo pipefail
repo_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
build_dir="$repo_root/build/cv"
mkdir -p "$build_dir"
command -v pdflatex >/dev/null || { echo 'Install pdfLaTeX / TeX Live first.' >&2; exit 1; }
export TZ=UTC
export SOURCE_DATE_EPOCH="${SOURCE_DATE_EPOCH:-$(git -C "$repo_root" log -1 --format=%ct)}"
cd "$repo_root/cv"
for pass in 1 2; do
  if ! pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error \
      -file-line-error -output-directory="$build_dir" RondinaCV.tex \
      >"$build_dir/pass-$pass.log" 2>&1; then
    cat "$build_dir/pass-$pass.log" >&2
    exit 1
  fi
done
test -s "$build_dir/RondinaCV.pdf"
install -m 644 "$build_dir/RondinaCV.pdf" "$repo_root/content/static/cv.pdf"
echo 'Built content/static/cv.pdf from cv/RondinaCV.tex'
if grep -E 'Overfull|LaTeX Warning' "$build_dir/RondinaCV.log"; then
  echo 'Review the warnings above before publishing.'
fi
