#!/usr/bin/env python3
"""Build grounded Q&A corpus for the History 54N Essay Guide agent.

Output: website/data/essay_corpus.json
"""
from __future__ import annotations

import json
import re
from html import unescape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HTML = ROOT / "website" / "index.html"
KB_DIR = ROOT / "notes"
DATA = ROOT / "website" / "data"
ASSETS_DATA = ROOT / "website" / "assets" / "data"
OUT = DATA / "essay_corpus.json"

SECTION_TITLES = {
    "hero": "What She Did Not Say",
    "argument-summary": "Argument summary",
    "part1-question": "The question",
    "part2-antebellum": "Antebellum: Jacobs and the garret",
    "part3-freedom": "Freedom: Walker, clubs, and NACW",
    "timeline": "Timeline",
    "part4-activism": "Activism: Wells and the lynching script",
    "part5-blues": "Blues legacies",
    "part6-civilrights": "Civil rights and Black feminism",
    "part7-contemporary": "Contemporary visibility",
    "conclusions": "Conclusions",
    "sources": "Sources",
    "ask-anything": "Ask me anything",
}

STOPWORDS = frozenset(
    "a an the and or but in on at to for of is are was were be been being "
    "it its this that with from as by not no so if than then into about "
    "what when how why who which their there they them we you your our".split()
)


def strip_html(html: str) -> str:
    html = re.sub(r"<script[\s\S]*?</script>", " ", html, flags=re.I)
    html = re.sub(r"<style[\s\S]*?</style>", " ", html, flags=re.I)
    html = re.sub(r"<[^>]+>", " ", html)
    text = unescape(html)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def neutralize_em_dash(text: str) -> str:
    return re.sub(r"\s*—\s*", ", ", text).replace(" ,", ",")


def clean_ui_noise(text: str) -> str:
    patterns = [
        r"Start with Part \d+\s*↓?",
        r"Jump to timeline\s*→?",
        r"Next:.*?↓",
        r"Final Project\s*·\s*History 54N\s*·\s*Spring 2026",
        r"Part \d+",
        r"Section \d+",
        r"You are here",
        r"Previous quotation",
        r"Next quotation",
        r"Select quotation",
    ]
    for pat in patterns:
        text = re.sub(pat, " ", text, flags=re.I)
    text = re.sub(r"\s+([,.])", r"\1", text)
    return re.sub(r"\s+", " ", text).strip()


def extract_sections(html: str) -> dict[str, str]:
    parts: dict[str, str] = {}
    for m in re.finditer(
        r'<section\s+id="([^"]+)"[^>]*>([\s\S]*?)</section>',
        html,
        flags=re.I,
    ):
        sid, body = m.group(1), m.group(2)
        parts[sid] = strip_html(body)
    return parts


def slug_from_note_path(path: Path) -> str:
    name = path.stem
    if name.startswith("reading-"):
        return name[len("reading-") :]
    return name


def load_kb_chunks() -> list[dict]:
    chunks = []
    if not KB_DIR.is_dir():
        return chunks
    for path in sorted(KB_DIR.glob("*.md")):
        raw = path.read_text(encoding="utf-8")
        if raw.startswith("---"):
            end = raw.find("---", 3)
            if end != -1:
                raw = raw[end + 3 :]
        text = neutralize_em_dash(strip_html(raw))
        if len(text) < 40:
            continue
        slug = slug_from_note_path(path)
        title = slug.replace("-", " ").title()
        chunks.append(
            {
                "id": f"kb-{slug}",
                "section": "sources",
                "title": f"Reading notes: {title}",
                "anchor": "#sources",
                "text": text[:4000],
                "stats": [],
                "kb": [slug],
                "keywords": tokenize(text)[:40],
            }
        )
    return chunks


def tokenize(text: str) -> list[str]:
    words = re.findall(r"[a-z0-9']+", text.lower())
    return [w for w in words if len(w) > 2 and w not in STOPWORDS]


def load_chart_chunks() -> list[dict]:
    chunks = []
    lfp_path = ASSETS_DATA / "lfp_black_women.json"
    if lfp_path.is_file():
        lfp = json.loads(lfp_path.read_text(encoding="utf-8"))
        years = lfp.get("years", [])
        values = lfp.get("values", [])
        if years and values:
            chunks.append(
                {
                    "id": "chart-lfp",
                    "section": "hero",
                    "title": "Black women labor force participation chart",
                    "anchor": "#hero",
                    "text": (
                        "The hero chart tracks Black women labor force participation from "
                        f"{years[0]} to {years[-1]}, rising from about {values[0]}% to "
                        f"{values[-1]}%. The essay uses it as a descriptive backdrop: "
                        "public economic visibility does not automatically translate into "
                        "credibility for interior testimony."
                    ),
                    "stats": [
                        {"label": "1880 LFP", "value": f"{values[0]}%"},
                        {"label": "2020 LFP", "value": f"{values[-1]}%"},
                    ],
                    "kb": [],
                    "keywords": ["lfp", "labor", "participation", "chart", "work"],
                }
            )
    nacw_path = ASSETS_DATA / "nacw_clubs.json"
    if nacw_path.is_file():
        nacw = json.loads(nacw_path.read_text(encoding="utf-8"))
        chunks.append(
            {
                "id": "chart-nacw",
                "section": "part3-freedom",
                "title": "NACW club growth chart",
                "anchor": "#part3-freedom",
                "text": (
                    "The NACW clubs chart shows institutional growth of Black women's "
                    "club networks after emancipation. The essay pairs it with respectability "
                    "politics: clubs could be leverage inside Jim Crow governance while also "
                    "disciplining members who fell outside moral scripts."
                ),
                "stats": [],
                "kb": ["nacw"],
                "keywords": ["nacw", "clubs", "chart", "institution", "respectability"],
            }
        )
    ba_path = ASSETS_DATA / "ba_attainment_black_women.json"
    if ba_path.is_file():
        ba = json.loads(ba_path.read_text(encoding="utf-8"))
        chunks.append(
            {
                "id": "chart-ba",
                "section": "part7-contemporary",
                "title": "Black women BA attainment chart",
                "anchor": "#part7-contemporary",
                "text": (
                    "The contemporary section charts rising bachelor's degree attainment "
                    "among Black women alongside persistent credibility gaps in medicine, "
                    "school discipline, and public mourning. Visibility and credentials "
                    "do not end the essay's central problem: institutions still struggle "
                    "to hear interior claims at full depth."
                ),
                "stats": [],
                "kb": [],
                "keywords": ["attainment", "education", "chart", "contemporary", "ba"],
            }
        )
    return chunks


def load_meta_chunks() -> list[dict]:
    return [
        {
            "id": "meta-scope",
            "section": "hero",
            "title": "About this project",
            "anchor": "#hero",
            "text": (
                "What She Did Not Say is a History 54N visual essay by Sunmit Hallur "
                "(Spring 2026, Stanford). It argues that Black women often looked open while "
                "guarding interior life under surveillance (Hine's dissemblance), and that "
                "respectability politics was the public layer of that strategy (Higginbotham). "
                "Photographs, a sixteen-card timeline, and three charts carry evidence; "
                "interpretation stays in the prose."
            ),
            "stats": [],
            "kb": [],
            "keywords": [
                "essay",
                "history",
                "project",
                "site",
                "about",
                "thesis",
                "argument",
                "stanford",
                "54n",
                "sunmit",
                "hallur",
                "visual",
            ],
        },
        {
            "id": "meta-thesis",
            "section": "argument-summary",
            "title": "Central thesis",
            "anchor": "#argument-summary",
            "text": (
                "Black women often looked open while guarding what exposure could cost them—"
                "Hine called that dissemblance. Uplift dress and deportment were the public "
                "layer Higginbotham names respectability politics. Three claims organize the "
                "evidence: dissemblance as shield, respectability as cage and key, blues and "
                "movement politics as refusal when uplift speech could not name desire, violence, "
                "or anger directly."
            ),
            "stats": [],
            "kb": [],
            "keywords": [
                "thesis",
                "dissemblance",
                "respectability",
                "hine",
                "inner",
                "archive",
                "argument",
            ],
        },
        {
            "id": "meta-sections",
            "section": "hero",
            "title": "How the site is organized",
            "anchor": "#hero",
            "text": (
                "Navigation: About, Essay (hero through Part 8), Timeline, Conclusion, Sources. "
                "Essay sections run Jacobs and the garret, post-emancipation labor and NACW "
                "clubs, Wells on lynching, Davis on blues and Passing, civil rights and Combahee, "
                "contemporary credibility traps (Hill, #MeToo, clinical bias), then conclusions "
                "with a quote carousel. Ask me anything and the Guide sidebar answer from "
                "essay text and course readings."
            ),
            "stats": [],
            "kb": [],
            "keywords": [
                "section",
                "structure",
                "navigate",
                "walkthrough",
                "timeline",
                "read",
                "where",
                "find",
            ],
        },
        {
            "id": "meta-sources",
            "section": "sources",
            "title": "Course readings and bibliography",
            "anchor": "#sources",
            "text": (
                "Key secondary sources include Hine (1989) on dissemblance, Higginbotham (1993) "
                "on respectability, Jacobs (1861), Hunter (1997), Davis (1998) on blues, Wells "
                "(1892), McGuire (2004), Ransby (2003) on Ella Baker, Sharpe (2023), Cottom (2019), "
                "and Villarosa (2022). Primary sources include Combahee River Collective (1977) "
                "and Lorde (1981). Charts draw on census and BLS tabulations cited in Sources."
            ),
            "stats": [],
            "kb": [],
            "keywords": [
                "source",
                "reading",
                "bibliography",
                "hine",
                "jacobs",
                "wells",
                "davis",
                "citation",
            ],
        },
        {
            "id": "meta-findings",
            "section": "conclusions",
            "title": "Headline takeaways",
            "anchor": "#conclusions",
            "text": (
                "Shield: dissemblance hid interior life when rape culture made disclosure "
                "dangerous (Hine 1989). Cage: respectability won schools and votes—and "
                "punished women who missed the performance (Higginbotham 1993). Refusal: blues, "
                "Combahee, Lorde, and contemporary portraiture named what uplift speech coded "
                "indirectly. When a narrative sounds too neat, check the gap between what was "
                "performed and what was withheld."
            ),
            "stats": [],
            "kb": [],
            "keywords": [
                "finding",
                "takeaway",
                "conclusion",
                "summary",
                "shield",
                "cage",
                "refusal",
                "remember",
            ],
        },
    ]


def main() -> None:
    html = HTML.read_text(encoding="utf-8")
    sections = extract_sections(html)
    chunks: list[dict] = []

    for sid, text in sections.items():
        if sid == "ask-anything":
            continue
        if len(text) < 40:
            continue
        paras = [
            p.strip()
            for p in re.split(r"(?<=[.!?])\s+", text)
            if len(p.strip()) > 30
        ]
        buf = ""
        part = 0
        for para in paras:
            if len(buf) + len(para) > 1200 and buf:
                chunks.append(_section_chunk(sid, buf, part))
                part += 1
                buf = para
            else:
                buf = f"{buf} {para}".strip() if buf else para
        if buf:
            chunks.append(_section_chunk(sid, buf, part))

    chunks.extend(load_kb_chunks())
    chunks.extend(load_chart_chunks())
    chunks.extend(load_meta_chunks())

    faqs = [
        (
            "what is this essay about",
            "What She Did Not Say traces how Black women guarded interior life under "
            "surveillance (Hine's dissemblance) and used respectability as its public face "
            "(Higginbotham)—from Jacobs's garret through Wells, blues, Combahee, and "
            "contemporary credibility traps.",
            "hero",
            "#hero",
            ["essay", "about", "project", "dissemblance", "respectability"],
        ),
        (
            "what is dissemblance",
            "Darlene Clark Hine's culture of dissemblance names collective practices of "
            "concealment under sexualized surveillance, not reducible to shame or silence-as-absence. "
            "It guarded interior life the archive rarely documents fairly.",
            "part2-antebellum",
            "#part2-antebellum",
            ["dissemblance", "hine", "concealment", "surveillance"],
        ),
        (
            "what is respectability",
            "Evelyn Brooks Higginbotham's politics of respectability describes how Black women "
            "used moral language and institution-building as leverage inside Jim Crow governance. "
            "Beside Hine, respectability can discipline communities from within while dissemblance "
            "protects individuals from exposure.",
            "part3-freedom",
            "#part3-freedom",
            ["respectability", "higginbotham", "morality", "institution"],
        ),
        (
            "who is harriet jacobs",
            "Harriet Jacobs hid for years in a garret to escape sexual coercion, narrating "
            "dissemblance as spatial and bodily strategy in Incidents in the Life of a Slave Girl (1861). "
            "The essay treats her garret as early evidence that protection of interior life required "
            "literal concealment.",
            "part2-antebellum",
            "#part2-antebellum",
            ["jacobs", "garret", "slavery", "incidents"],
        ),
        (
            "who is ida b wells",
            "Ida B. Wells documented and challenged the lynching script in Southern Horrors (1892), "
            "insisting that public testimony could puncture respectability narratives used to justify "
            "violence against Black women and men.",
            "part4-activism",
            "#part4-activism",
            ["wells", "lynching", "activism", "southern horrors"],
        ),
        (
            "what does angela davis argue",
            "Angela Davis reads blues women as theorists of desire, labor, and refusal who "
            "operated outside narrow respectability scripts. Blues Legacies and Black Feminism (1998) "
            "helps the essay connect song to interior claims the archive often misread.",
            "part5-blues",
            "#part5-blues",
            ["davis", "blues", "song", "feminism"],
        ),
        (
            "what is the timeline",
            "The timeline is sixteen cards from 1818 to 2024. Each date links one event to "
            "how Black women managed visibility, labor, or testimony—and what that moment "
            "cost in credibility or risk.",
            "timeline",
            "#timeline",
            ["timeline", "dates", "chronology", "cards"],
        ),
        (
            "remember one sentence",
            "Dissemblance hid interior life under surveillance; respectability was its public "
            "face—and could cage or unlock depending on who held the keys.",
            "conclusions",
            "#conclusions",
            ["takeaway", "conclusion", "one sentence", "remember"],
        ),
        (
            "what are the main findings",
            "Shield (Hine), cage and key (Higginbotham), refusal (Davis, Combahee, Lorde, Sharpe). "
            "Neither tactic maps cleanly onto virtue—both cost labor audiences rarely repaid.",
            "conclusions",
            "#conclusions",
            ["findings", "main", "takeaway", "summary"],
        ),
        (
            "what data do you use",
            "Three descriptive charts: Black women labor force participation (1880–2020), "
            "NACW club growth, and Black women's BA attainment. They illustrate context; "
            "the argument rests on historical interpretation of readings and visual sources.",
            "sources",
            "#sources",
            ["data", "chart", "lfp", "nacw", "attainment"],
        ),
        (
            "how should i explain this to my professor",
            "Frame the essay as a narrative visual history argument: Hine's dissemblance and "
            "Higginbotham's respectability as paired lenses on Black women's interior lives, "
            "read through Jacobs, Wells, Davis, civil rights feminism, and contemporary portraiture. "
            "Charts and timeline support but do not replace interpretation.",
            "argument-summary",
            "#argument-summary",
            ["professor", "explain", "present", "summary"],
        ),
        (
            "what is the combahee river collective",
            "The Combahee River Collective Statement (1977) named politics that exceeded narrow "
            "respectability scripts, centering Black lesbian feminists' analysis of intersecting "
            "oppressions. The essay cites it in the civil rights section as refusal.",
            "part6-civilrights",
            "#part6-civilrights",
            ["combahee", "collective", "1977", "feminism"],
        ),
    ]
    for fid, text, section, anchor, kws in faqs:
        chunks.append(
            {
                "id": f"faq-{fid.replace(' ', '-')}",
                "section": section,
                "title": f"FAQ: {fid}",
                "anchor": anchor,
                "text": neutralize_em_dash(text),
                "stats": [],
                "kb": [],
                "keywords": kws,
            }
        )

    for c in chunks:
        if c.get("text"):
            c["text"] = neutralize_em_dash(c["text"])
        if "keywords" not in c or not c["keywords"]:
            c["keywords"] = tokenize(c.get("text", ""))[:50]

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(
        json.dumps({"version": 1, "chunks": chunks}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"Wrote {len(chunks)} chunks -> {OUT}")


def _section_chunk(sid: str, text: str, part: int) -> dict:
    title = SECTION_TITLES.get(sid, sid.replace("-", " ").title())
    text = neutralize_em_dash(clean_ui_noise(text))
    return {
        "id": f"{sid}-{part}" if part else sid,
        "section": sid,
        "title": title,
        "anchor": f"#{sid}",
        "text": text[:2000],
        "stats": [],
        "kb": [],
        "keywords": tokenize(text)[:50],
    }


if __name__ == "__main__":
    main()
