# Website and CV maintenance setup

Prepared for Giacomo Rondina on October 9, 2026 (America/Los_Angeles).

## What is ready

The supplied `RondinaCV.tex` is preserved byte for byte in `cv/RondinaCV.tex`.
The build compiles it to `content/static/cv.pdf`, preserving the existing
https://giacomorondina.org/static/cv.pdf address. The source stays out of Hugo's
published output, but is visible in this public GitHub repository.

`AGENTS.md` gives Codex the repository map, maintenance workflow and review rules.
The GitHub workflow compiles the CV and builds Hugo for every PR and main-branch
push. PRs produce downloadable review files without publishing. Successful
main-branch builds deploy. The workflow contains no model calls or API keys;
Codex supplies the reasoning and editing when given a task and repository access.

## Apply this setup

1. Open or clone `grondinaucsd/grondinaucsd.github.io` in a Codex environment
   with permission to create a branch and pull request.
2. Apply the supplied patch on a new branch, after checking it against the latest
   main branch. Alternatively, copy the `repository-files/` contents from the
   setup ZIP into the repository root on a new branch.
3. Run the build commands below and review the generated CV and file diff.
4. Open a PR. In its Actions run, download `website-review-<run-id>` to inspect
   the generated site and `build/cv/RondinaCV.pdf`.
5. Check repository Settings > Pages uses GitHub Actions. Review the actual
   Actions result. Merge only after approving the changes and resolving any CI
   errors. Then verify the live CV and homepage.

The preparation session had public read access but no authenticated push
access. It did not create a remote branch/PR, alter GitHub settings, or deploy.
GitHub-hosted CI cannot be verified until the setup is pushed.

## Build locally or in Codex

Use Hugo extended 0.108.0 to match the existing site. On Ubuntu install
`texlive-latex-extra` and `texlive-fonts-recommended` for the CV. Python 3.10+
is required for the link audit. Then run from the repository root:

```bash
bash scripts/build_cv.sh
hugo --minify --baseURL https://giacomorondina.org/
python3 scripts/audit_site.py public
```

In TeXstudio, open `cv/RondinaCV.tex` and use pdfLaTeX. For the repository update,
run the script above to copy the generated output to the public PDF location.
After future edits, commit both the LaTeX source and its generated public PDF.
The workflow also recompiles from source before deploying, so a successful
deployment uses the source even if a manually committed PDF was stale.

The link audit reports existing problems without blocking this setup. Once the
backlog in `INITIAL_AUDIT.md` is fixed, add `--strict` to make missing internal
links fail a build. External URLs and semantic mistakes need agent review.

## Monthly check-in and follow-up

A ChatGPT check-in was enabled on October 9, 2026 for the first day of each
month, starting November 1, around 8 a.m. America/Los_Angeles time. It asks about papers/publication status,
presentations, teaching, grants/awards, appointments/service and advising.
The question itself needs no GitHub connection. It does not edit or publish.

When the user replies, use the connected Codex repository environment to read
the current sources and apply the chosen updates. Prepare a PR, compile and
visually inspect the CV, and wait for approval before merging. Repository
editing is a separate follow-up stage; the reminder is not a fully configured
unattended GitHub editor.

After authenticated repository access is verified, the recurring task can be
expanded to audit the repository before asking questions. Keep the durable
instructions here and in `AGENTS.md`, not only in a chat transcript.

## New paper intake

Upload the exact PDF and identify it as the version approved for the website.
Include changes to title, date, status, figures/slides or appendices if relevant.
Codex should compare these sources, update the existing paper URL and matching
CV entry as authorized, and present a reviewable proposal. No latest-paper PDF
was supplied in the initial setup, so the February 2023 sustainable-investing
paper has not been replaced.

## Initial verification

- Supplied LaTeX source copied without content or formatting changes.
- CV compiled successfully in two passes to eight pages, without LaTeX warnings
  or overfull boxes; all pages visually inspected.
- Site built successfully with the existing Hugo extended 0.108.0 version.
- Generated site's CV matches the compiled public PDF byte for byte.
- CV source and maintenance files are absent from the generated website.
- Internal link audit identified six missing targets; documented for review.
- GitHub-hosted workflow execution and live deployment remain unverified.
