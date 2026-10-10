# Giacomo Rondina website maintenance

## Project and source of truth

- Site: https://giacomorondina.org/
- Repository: grondinaucsd/grondinaucsd.github.io; production branch: main.
- Hugo extended 0.108.0 with a customized, vendored PaperMod theme.
- `config.yml`: homepage biography, navigation and social links.
- `content/papers/*.md`: paper metadata and pages. Preserve existing URLs.
- `content/courses/*.md`: teaching pages, including historical materials.
- `content/static/`: published PDFs and images.
- `cv/RondinaCV.tex`: authoritative editable CV; `content/static/cv.pdf` is generated.
- `maintenance/`: operating notes and audit records, outside Hugo's published content.
- This repository is public. Store only approved public information in it.

## Editing and publication

- Preserve the layout, styling and content outside the requested change.
- Prepare a branch and reviewable pull request. Do not push directly to main,
  merge or deploy without the user's approval of the concrete changes.
- Read current files and existing PRs before updating. Avoid duplicate proposals.
- Use a paper for posting only when the user explicitly approves it for that
  purpose. Do not substitute private drafts or infer approval from timestamps.
- Verify title, author order, date, abstract, citation, status and PDF target.
  Revision requests do not establish acceptance or publication.
- Ask about conflicting facts. Do not invent events, dates or accomplishments;
  conversation memory is not sufficient evidence for a public change.
- Keep the CV's visible date and PDF metadata synchronized when making real
  approved content updates. Do not advance the date just because a build runs.
- Record suspected factual typos with supporting evidence for user review.

## New paper workflow

1. Read the approved PDF and compare it with the posted paper and page.
2. Update the PDF and supported title, authors, date, abstract, summary,
   citation and status. Check figures, slides and appendices for consistency.
3. Preserve download URLs where feasible. Do not redirect historical URLs to
   unrelated papers. Review legacy aliases for conflicts.
4. Update the matching CV entry if approved; otherwise list it as a question.
5. Build, verify, and show the changes and remaining questions in a PR.

## Monthly review

1. Read `maintenance/SETUP.md` and the current CV and public pages.
2. Check stale versions, conflicting metadata, broken links, missing approved
   publications, and ambiguity between current and historical teaching.
3. Ask a concise grouped question about papers/status, presentations, teaching,
   grants/awards, appointments/service, and advising since the last review.
   Include concrete discrepancies; avoid repeating resolved questions.
4. End the check-in and await the user's reply. An unattended run must not
   assume it can wait indefinitely or treat silence as approval.
5. Apply the user's selected updates in the follow-up, build the CV and site,
   and prepare a PR with review artifacts. Publication requires approval.
6. Record decisions in the PR. If nothing changed, make no date-only commit.

## Build and verification

- Linux prerequisites: Hugo extended 0.108.0, Python 3.10+, TeX Live packages
  `texlive-latex-extra` and `texlive-fonts-recommended`.
- Compile: `bash scripts/build_cv.sh`.
- Inspect the PDF visually after edits: date columns, page breaks, headings,
  links and any overfull-box warnings.
- Build: `hugo --minify --baseURL https://giacomorondina.org/`.
- Audit: `python3 scripts/audit_site.py public`. Existing issues are recorded in
  `maintenance/INITIAL_AUDIT.md`; do not hide them or claim they are fixed.
  Use `--strict` once that backlog is resolved.
- Verify `public/static/cv.pdf` matches the compiled PDF. Source files under
  `cv/` and `maintenance/` must not appear in the generated website.
- Commit CV source and generated PDF together. Exclude build output, LaTeX
  auxiliary files and credentials.
- GitHub builds PRs for review and deploys successful main-branch builds.
  Verify the actual GitHub run after setup; local success alone is not CI proof.
