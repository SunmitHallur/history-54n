# History 54N Visual Essay

## Title
What She Did Not Say: Dissemblance, Respectability, and the Inner Lives of Black Women, 1818-2024

## Abstract
This project is a narrative-first visual essay built for History 54N at Stanford. It traces dissemblance and respectability across Black women's history from slavery to the present. Photographs, a sixteen-card timeline, and three descriptive charts support the argument without replacing interpretation.

## Run locally
```bash
cd ~/Documents/History\ 54N/website
python3 -m http.server 8000
```
Then open `http://localhost:8000`.

To regenerate `website/index.html` from the content template:
```bash
python3 ~/Documents/History\ 54N/gen_site.py
```

## Export to PDF
1. Open the page in Chrome.
2. File > Print.
3. Destination: Save as PDF.
4. Paper: Letter.
5. Margins: Default.
6. Save to `History54N-VisualEssay.pdf`.

Print styles keep narrative body text and quotation blockquotes visible while hiding navigation chrome and carousel controls (dots and arrows).

## Word count (rubric guidance)
| Area | Approximate words | Notes |
|------|------------------|--------|
| Full page template (`gen_site.py` HTML, tags stripped) | **~3,000** | Main narrative, captions, chart labels, bibliography cards |
| Reading notes (`notes/*.md`) | ~600 (stubs + bullets) | Expand before finals if instructor wants reading journals |

Target for the syllabus paper equivalent is roughly **3,000 to 3,500 words** of body prose plus bibliography; regenerate counts after edits with the same strip-tags method used in office hours.

## Submission checklist
- [ ] Office-hours project discussion completed by Week 8.
- [ ] Final PDF exported and checked for citations.
- [ ] `website/assets/CREDITS.md` completed and accurate.
- [ ] Final submission emailed by Thursday, June 11 at midnight.

## Repository layout
- `website/` · static site (`index.html`, `styles.css`, `app.js`, `print.css`, `assets/`)
- `gen_site.py` · regenerates `index.html` (edit here for long-form copy)
- `notes/` · reading note stubs aligned to syllabus sources
