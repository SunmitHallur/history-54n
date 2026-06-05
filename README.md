# History 54N Visual Essay

## Title
What She Did Not Say: Dissemblance, Respectability, and the Inner Lives of Black Women, 1818-2024

## Abstract
This project is a narrative-first visual essay built for History 54N at Stanford. It traces dissemblance and respectability across Black women's history from slavery to the present. Photographs, a sixteen-card timeline, and three descriptive charts support the argument without replacing interpretation.

## Live site
**Primary (Essay Guide + LLM Q&A):** deploy to Vercel from this repo (`outputDirectory`: `website`). Example URL: `https://history-54n.vercel.app` (set after linking).

**Static fallback (no `/api/chat`):** https://sunmithallur.github.io/history-54n/

Repository: https://github.com/SunmitHallur/history-54n

## Essay Guide (walkthrough + grounded Q&A)
- **Guide** button in the top bar opens a sidebar with **Ask** and **Walkthrough** tabs.
- **Ask me anything** section (before Sources) uses the same agent inline.
- Answers are grounded in the essay HTML + `notes/*.md` via RAG (`website/data/essay_corpus.json`).
- Optional LLM polish runs on Vercel at `POST /api/chat` (see [docs/ESSAY_GUIDE_API.md](docs/ESSAY_GUIDE_API.md)).

Rebuild the retrieval corpus after editing essay copy or reading notes:
```bash
python3 gen_site.py
python3 scripts/build_essay_corpus.py
```

## Deploy to Vercel
1. Import the GitHub repo at [vercel.com/new](https://vercel.com/new) (Framework: Other; output directory is set in `vercel.json`).
2. Add environment variables: `OPENAI_API_KEY` (required for LLM answers). Optional: `UPSTASH_REDIS_REST_URL`, `UPSTASH_REDIS_REST_TOKEN`, `ESSAY_GUIDE_ALLOWED_ORIGINS`.
3. Deploy. Verify in browser console:
   ```javascript
   fetch('/api/chat', { method: 'HEAD' }).then(r =>
     console.log(r.status, r.headers.get('X-Essay-Guide-RateLimit'))
   );
   ```
4. Local API dev: `npx vercel env pull .env.local && npx vercel dev` (plain `python3 -m http.server` does not run `/api/chat`).

GitHub Pages (`.github/workflows/deploy-pages.yml`) remains a static-only fallback without the API.

## Run locally (static)
```bash
cd ~/Documents/History\ 54N/website
python3 -m http.server 8000
```
Then open `http://localhost:8000`. Walkthrough and client-side retrieval work; LLM answers require Vercel dev or production.

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
- `website/` · static site (`index.html`, `styles.css`, `app.js`, `essay-guide.js`, `print.css`, `assets/`, `data/`)
- `api/` · Vercel serverless `/api/chat` for Essay Guide LLM answers
- `gen_site.py` · regenerates `index.html` (edit here for long-form copy)
- `scripts/build_essay_corpus.py` · builds `website/data/essay_corpus.json`
- `notes/` · reading note stubs aligned to syllabus sources (also indexed by Essay Guide)
- `vercel.json` · Vercel static output + cache headers
