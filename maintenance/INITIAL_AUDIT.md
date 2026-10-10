# Initial website audit

Reviewed October 9, 2026 (America/Los_Angeles).
Repository baseline: `29eddf21d7fcc4fb8a56f995d9133db2a49ee62b`.
Sources: the current repository and live site, the supplied July 2026 LaTeX CV,
and the PDFs already in the repository. No assumed unpublished paper versions
or conversation-memory facts were used for content edits.

## Highest-priority items

| Item | Observed evidence | Next action |
| --- | --- | --- |
| Posted CV | `/static/cv.pdf` is dated August 2023; supplied source is July 2026. | The setup package includes the compiled July 2026 replacement. Review and publish via PR. |
| Sustainable-investing paper | `/4/` is dated February 2023. The PDF explicitly says February 15, 2023 and preliminary/incomplete. The supplied CV lists an October 2025 revision and R&R. | Obtain the exact PDF approved for posting; update PDF, page, citation and CV entry together. Review figures/slides against that version. |
| Orbit-use paper | `/3/` has a 2023 working-paper citation. The supplied CV lists JAERE 12(2), March 2025. | Prepare a publication-status/citation update; obtain approved final PDF and bibliographic details. Do not change scientific summary from citation data alone. |
| Walker coauthored paper | `/5/` lists “Equivalence Results with Endogenous Signal Extraction,” May 2023. CV lists “A Hierarchical Representation of Dispersed Information,” June 2026. | Ask whether this is a renamed revision or a distinct paper; obtain the approved PDF before changing the page. |
| Missing selected research | The website lists five papers; the CV lists additional publications and working papers, including the global-games paper. | Ask whether Papers should remain a selected list or cover the full CV. |

## Incorrect or missing links and content

- `content/papers/1.md`: the “Frequendy Domain Primer” link points to the CV.
  Ask for the intended document or remove the misleading link as approved.
- `content/papers/2.md`: “Appendix — Additional empirical results” also points
  to the CV. Ask for the intended appendix.
- `content/courses/112.md`: all five modules use `/x1.pdf` and `/x4.pdf`.
  Both returned HTTP 404 on the live site. Obtain the correct resources or
  remove the placeholders as approved.
- `content/courses/110A.md`: Modules 2–5 have growth/labor/consumption headings
  but descriptions and PDFs copied from the sustainability course. These are
  semantic mismatches even though the PDF links resolve. Correct from actual
  teaching materials; do not generate replacement syllabus claims.
- The generated HTML references missing browser icons at `/favicon.ico`,
  `/favicon-16x16.png`, `/favicon-32x32.png`, and `/apple-touch-icon.png`.
  There is an existing `/static/favicon.ico`; review icon configuration.
- Legacy aliases collide: `/1.html`, `/4.html`, `/t3.html`, and several old
  `/uploads/...` PDF addresses belong to more than one page. Resolve each old
  URL to its intended document/page before altering redirect ownership.
- The CV's old `/uploads/7/0/2/0/70200055/cv.pdf` alias appears on three paper
  pages. It should not lead to an unrelated paper.
- `/5/` has visible missing spaces in its abstract, including “equilibriumand,”
  “theoremdelivers,” “betweenmodels,” and “forminmodels.” Verify replacement
  text against the approved paper.

## Teaching and profile questions

- Courses shows Econ 110A, Econ 112 and the 2022 sustainability summer school;
  the supplied CV also lists Econ 3 and Econ 210B. Decide whether to add those
  pages and label historical materials explicitly. No current teaching load
  can be inferred from the older course pages.
- The courses index describes classes “currently teaching,” although listed
  pages are dated 2022–2023. Confirm intended scope.
- Confirm the office location and desired office-hours wording during the first
  review. The existing generic office-hours language is not proven wrong.

## CV details requiring review

- “Confounding Dynamics” is listed as Journal of Economic Theory volume 156
  in the supplied CV. The article's first page and website citation both give
  volume 196 (2021), article 105251. Propose this correction for approval.
- The CV and homepage use different wording for the current teaching title.
  Ask which wording to standardize; do not assume either is substantively wrong.
- Keep the July 2026 date until a substantive update is approved. The setup
  preserves the supplied source verbatim, including factual review items.

## Technical results and boundaries

- Build succeeds with Hugo extended 0.108.0; no engine/theme migration is needed
  for this maintenance setup.
- The original workflow used older Pages artifact actions. The proposed workflow
  updates to checkout v4, upload-artifact v4, upload-pages-artifact v3 and
  deploy-pages v4; adds PR builds and CV compilation; and retains the Hugo pin.
- Internal checker scanned 73 generated HTML files and found six distinct
  missing targets: four icon paths and the two Econ 112 placeholder PDFs.
- This was a targeted audit, not a full verification of all external links,
  historical biographical facts, teaching documents or third-party services.
- No public pages, paper files, repository settings or remote branches were
  changed. The proposed patch includes the generated CV replacement and setup
  files; content corrections above remain for user review.
