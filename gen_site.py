#!/usr/bin/env python3
"""Generate index.html for History 54N visual essay (plan-aligned)."""
from datetime import datetime, timezone
from pathlib import Path

OUT = Path(__file__).resolve().parent / "website" / "index.html"

HTML = r'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>What She Did Not Say: Dissemblance, Respectability, and the Inner Lives of Black Women, 1818-2024</title>
  <meta name="description" content="History 54N visual essay on dissemblance, respectability, and Black women's inner lives." />
  <meta property="og:title" content="What She Did Not Say" />
  <meta property="og:description" content="Stanford History 54N final project visual essay." />
  <meta property="og:type" content="article" />
  <meta name="twitter:card" content="summary_large_image" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Source+Serif+4:opsz,wght@8..60,400;8..60,500;8..60,600;8..60,700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="styles.css" />
  <link rel="stylesheet" href="print.css" media="print" />
  <script type="application/ld+json">
  {"@context":"https://schema.org","@type":"ScholarlyArticle","headline":"What She Did Not Say","author":{"@type":"Person","name":"Sunmit Hallur"},"datePublished":"2026-05-06","about":"Black women's history, dissemblance, respectability","isAccessibleForFree":true}
  </script>
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>

  <div class="ambient-paths" aria-hidden="true">
    <svg class="ambient-paths-svg" viewBox="0 0 1440 900" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg">
      <path class="ambient-path ambient-path--1" d="M-80,520 C280,380 520,720 880,480 S1320,200 1520,420" fill="none" stroke="currentColor" stroke-width="1.25" stroke-linecap="round" />
      <path class="ambient-path ambient-path--2" d="M-40,180 C360,320 440,80 780,240 S1180,520 1480,300" fill="none" stroke="currentColor" stroke-width="1" stroke-linecap="round" opacity="0.55" />
      <path class="ambient-path ambient-path--3" d="M200,920 C420,640 900,860 1120,560 S1380,240 1560,480" fill="none" stroke="currentColor" stroke-width="0.9" stroke-linecap="round" opacity="0.45" />
      <path class="ambient-path ambient-path--4" d="M100,360 Q520,120 980,400 T1420,200" fill="none" stroke="currentColor" stroke-width="0.85" stroke-linecap="round" opacity="0.5" />
    </svg>
  </div>

  <header class="topbar">
    <div class="topbar-inner">
      <a class="brand" href="#hero">
        <span class="brand-dot"></span>
        <span class="brand-text">History 54N · Sunmit Hallur</span>
      </a>
      <nav class="topnav" aria-label="Primary">
        <a href="#argument-summary">Thesis</a>
        <a href="#part1-question">Question</a>
        <a href="#part2-antebellum">Antebellum</a>
        <a href="#part3-freedom">Freedom</a>
        <a href="#timeline">Timeline</a>
        <a href="#part4-activism">Activism</a>
        <a href="#part5-blues">Blues</a>
        <a href="#part6-civilrights">Rights</a>
        <a href="#part7-contemporary">Now</a>
        <a href="#conclusions">End</a>
        <a href="#sources">Sources</a>
      </nav>
      <details class="topnav-more">
        <summary>More</summary>
        <div class="topnav-more-menu">
          <a href="#timeline">Timeline</a>
          <a href="#part4-activism">Activism</a>
          <a href="#part5-blues">Blues</a>
        </div>
      </details>
      <button id="theme-toggle" class="ghost-btn ghost-btn--icon" type="button" aria-label="Switch to dark theme" aria-pressed="false" title="Toggle theme">
        <span class="ghost-btn__text"><span class="theme-icon" aria-hidden="true">◐</span></span>
      </button>
    </div>
    <div class="top-progress" aria-hidden="true"><span id="top-progress-fill"></span></div>
  </header>
  <div class="section-indicator" aria-live="polite">
    <span class="section-indicator__kicker">You are here</span>
    <span class="section-indicator__text" id="section-indicator-text">Intro</span>
  </div>

  <main id="main" class="main-stack">

    <section id="hero" class="hero">
      <div class="hero-inner">
        <p class="eyebrow">Final Project · History 54N · Spring 2026</p>
        <h1 class="title">What She Did Not Say</h1>
        <p class="hero-thesis-pull">
          The politics of respectability has rarely told the truth about Black women. It is the public face of a deeper survival strategy that Darlene Clark Hine called the culture of dissemblance, through which Black women have, since slavery, protected an inner life the archive was never built to hold. From Harriet Jacobs's garret to Amy Sherald's portrait of Breonna Taylor, this essay reads photographs, song, and testimony as the record of what Black women said, what they refused to say, and the gap between them.
        </p>
        <p class="hero-data-note">
          Standing in front of Sherald's work in print and online, I keep noticing the same problem visibility cannot solve. The painting can force a national audience to see a life cut short, yet seeing is not the same as believing Black women's interior claims at full depth (Princenthal 2024; SFMOMA 2024).
        </p>
        <div class="meta-row">
          <a class="ghost-btn hero-cta-primary" href="#part2-antebellum"><span class="ghost-btn__text">Start with Part 2 ↓</span></a>
          <a class="hero-text-link" href="#timeline">Jump to timeline →</a>
        </div>
      </div>
      <div class="hero-figure">
        <figure class="hero-photo-card">
          <picture>
            <source srcset="assets/photos/prelude/Michelle_Obama_2013_official_portrait.webp" type="image/webp" />
            <img class="hero-photo" src="assets/photos/prelude/Michelle_Obama_2013_official_portrait.jpg" alt="Michelle Obama seated for official portrait" loading="eager" decoding="async" />
          </picture>
          <figcaption>Michelle Obama, official portrait, 2013. Chuck Kennedy, White House photograph, public domain. The National Portrait Gallery situates the image in a long line of First Lady iconography; this essay returns to that scrutiny in Part 7.</figcaption>
        </figure>
        <div class="hero-chart-stack">
          <p class="hero-chart-caption">Black women labor force participation, 1880 to 2020</p>
          <div class="hero-chart-canvas-wrap">
            <canvas id="chart-hero" aria-label="Labor force participation chart"></canvas>
            <p class="chart-caveat">What white feminism discovered in the 1960s, Black women had been doing for a century. A chart marks labor history. It cannot recover interior life by itself (Goldin 1990; IPUMS; BLS CPS).</p>
          </div>
        </div>
      </div>
    </section>

    <section id="argument-summary" class="argument-summary" aria-label="What this essay argues">
      <h2>What this essay argues</h2>
      <p>
        Respectability names the public protocol many Black women used to demand citizenship and dignity in a society trained to misread them (Higginbotham 1993). Dissemblance names the interior practice Hine recovered when she argued that secrecy could operate like armor against sexualized surveillance (Hine 1989). This essay treats both as political strategies authored under constraint, then tracks how blues performance, civil rights organizing, and contemporary portraiture rewrite the balance between disclosure and refusal.
      </p>
    </section>

    <div class="section-bridge" aria-label="Transition">
      <p class="section-bridge__from">Public protocol meets private strategy.</p>
      <p class="section-bridge__to"><a href="#part1-question">Next: frame the analytic question ↓</a></p>
    </div>

    <section id="part1-question" class="section section-question">
      <div class="section-head">
        <p class="section-step">Part 1</p>
        <h2>The Question: Whose interior can history see?</h2>
        <p class="section-lede">
          In 1989 Hine published the essay that became a syllabus anchor for this course. She insisted that dissemblance was not shame alone. It was a collective pattern of hiding that shaped what could be known about Black women's inner lives in the Middle West (Hine 1989).
        </p>
      </div>
      <div class="prose">
        <p>
          Elsa Barkley Brown's question, what has happened here, pushes historians to notice how difference operates inside women's history itself (Brown 1992). Vivian May's reading of Anna Julia Cooper keeps intellectual genealogy from collapsing into a single story of uplift (May 2012). Kimberlé Crenshaw's intersection framing matters here because respectability and dissemblance land differently depending on whether a woman is being read through labor markets, courts, churches, or museums (Crenshaw 2016).
        </p>
        <p>
          Evelyn Brooks Higginbotham's politics of respectability helps explain why institution-building and moral language could function as leverage inside Jim Crow governance (Higginbotham 1993). Read beside Hine, the pairing does not tidy into a slogan. Respectability could discipline Black communities from within. Dissemblance could protect individuals from exposure. Both could also punish anyone who fell outside their scripts.
        </p>
        <aside class="inline-voice card">
          <p class="inline-voice__kicker">Hine on dissemblance</p>
          <blockquote>
            <p class="inline-voice__lead">"The secrecy and the dissemblance served as a shield."</p>
            <p class="inline-voice__follow">Dissemblance here is not mere silence. It is practiced withholding that defended interior life when surveillance treated Black women's bodies as legible evidence.</p>
          </blockquote>
          <p class="inline-voice__source">Opening sentence from Hine (1989); second paragraph glosses her claim in this essay's terms.</p>
        </aside>
        <p>
          That shield came with costs. Silence can be misread as consent. Decorum can be misread as satisfaction. This essay keeps returning to photographs because cameras often pretend they settle those misreadings. They rarely do.
        </p>
      </div>
    </section>

    <section id="part2-antebellum" class="section section-ground section-visual-panel">
      <div class="section-bg-film" aria-hidden="true">
        <div class="section-bg-film__slide section-bg-film__slide--a"></div>
        <div class="section-bg-film__slide section-bg-film__slide--b"></div>
        <div class="section-bg-film__slide section-bg-film__slide--c"></div>
      </div>
      <div class="section-visual-panel-inner">
        <div class="section-head">
          <p class="section-step">Part 2</p>
          <h2>Antebellum: Soul murder, sack, garret</h2>
          <p class="section-lede">
            Nell Painter's language of soul murder refuses to minimize trauma's bookkeeping (Painter 1995). Harriet Jacobs structured her narrative around concealment and proximity to violence, then named freedom as a practice of choosing who knows what (Jacobs 1861). Tiya Miles reads Ashley's sack as an object that carries kinship across rupture when paper trails fail (Miles 2021).
          </p>
        </div>
        <div class="ground-sequence">
          <article class="ground-step">
            <figure class="ground-photo">
              <picture>
                <source srcset="assets/photos/antebellum/women-activist-1.webp" type="image/webp" />
                <img src="assets/photos/antebellum/women-activist-1.jpg" alt="Historical photograph of Black women activists" loading="lazy" decoding="async" />
              </picture>
              <figcaption>Archival photograph of Black women in organized public roles; formal dress and grouping train the viewer to read collective respectability as political seriousness.</figcaption>
            </figure>
            <div class="ground-step__text">
              <p class="ground-step__label">Archive pressure</p>
              <h3>The photograph pretends totality</h3>
              <p>
                Deirdre Cooper Owens ties medical spectacle to racialized gender scripts that framed Black women's bodies as available for inspection (Cooper Owens 2017). Against that gaze, dissemblance begins to read less like secrecy for its own sake and more like a boundary drawn where law and medicine refused boundaries.
              </p>
            </div>
          </article>
          <article class="ground-step ground-step--reverse">
            <figure class="ground-photo">
              <picture>
                <source srcset="assets/photos/antebellum/womens-protests.webp" type="image/webp" />
                <img src="assets/photos/antebellum/womens-protests.jpeg" alt="Women protest historical photograph" loading="lazy" decoding="async" />
              </picture>
              <figcaption>Women's protest photograph: banners, spacing, and posture choreograph collective visibility in streets where Black women's politics rarely earned steady coverage.</figcaption>
            </figure>
            <div class="ground-step__text">
              <p class="ground-step__label">Kinship objects</p>
              <h3>What survives when the state steals documents</h3>
              <p>
                Miles demonstrates how a sack can carry memory when archives distort or erase Black women's claims (Miles 2021). Jacobs did similar work in prose by narrating the garret as a space of withheld visibility (Jacobs 1861).
              </p>
            </div>
          </article>
        </div>

        <div class="prose narrow">
          <p>
            Painter's soul murder framing warns historians against translating survival into tone policing. Trauma's bookkeeping is social as well as psychic: households, churches, and selling cultures formed contexts where Black women calculated disclosure under slavery's surveillance (Painter 1995). That calculation belongs in the same conceptual neighborhood as Hine's later essay even when the geography differs.
          </p>
          <p>
            Sojourner Truth's carte-de-visite practice made Black women's labor visible as commodity and testimony at once. Nell Irvin Painter reads Truth's image politics as argument, not accessory. Miles pairs naturally with Jacobs because both remind us that kinship can survive as material trace when ledgers lie (Miles 2021; Jacobs 1861). The sack photograph included on syllabi becomes a refusal of archive innocence: some interior histories arrive as cloth and stitching rather than as confessional prose alone.
          </p>
        </div>
      </div>
    </section>

    <div class="section-bridge" aria-label="Transition">
      <p class="section-bridge__from">Antebellum constraints set postbellum strategies.</p>
      <p class="section-bridge__to"><a href="#part3-freedom">Next: freedom and labor ↓</a></p>
    </div>

    <section id="part3-freedom" class="section section-ground section-visual-panel">
      <div class="section-bg-film" aria-hidden="true">
        <div class="section-bg-film__slide section-bg-film__slide--a"></div>
        <div class="section-bg-film__slide section-bg-film__slide--b"></div>
        <div class="section-bg-film__slide section-bg-film__slide--c"></div>
      </div>
      <div class="section-visual-panel-inner">
        <div class="section-head">
          <p class="section-step">Part 3</p>
          <h2>The Dawn of Freedom: Work, punishment, church</h2>
          <p class="section-lede">
            Tera Hunter reads post-emancipation freedom through domestic labor refusals and creative pressures on employers (Hunter 1997). Talitha LeFlouria ties convict labor systems to gendered brutality in the New South state (LeFlouria 2015).
          </p>
        </div>
        <div class="ground-sequence">
          <article class="ground-step">
            <figure class="ground-photo ground-photo--media">
              <picture>
                <source srcset="assets/photos/freedom/Women-riding-on-the-subway.webp" type="image/webp" />
                <img src="assets/photos/freedom/Women-riding-on-the-subway.jpeg" alt="Women on New York City subway 1958" loading="lazy" decoding="async" />
              </picture>
              <figcaption>Women riding on the subway, New York City, July 1958. Angelo Rizzuto, Library of Congress.</figcaption>
            </figure>
            <div class="ground-step__text">
              <p class="ground-step__label">Urban labor geography</p>
              <h3>Moving bodies, moving discipline</h3>
              <p>
                Hunter forces historians to treat washerwomen strikes and domestic negotiations as politics, not peripheral household drama (Hunter 1997). The subway frame pairs naturally with that argument because it catches Black women between workplaces and neighborhoods while the camera fixes them as types unless we refuse the frame.
              </p>
            </div>
          </article>
          <article class="ground-step ground-step--reverse">
            <figure class="ground-photo ground-photo--media">
              <picture>
                <source srcset="assets/photos/freedom/Sunday_in_Little_Rock,_Ark.,_1935._(3109755087).webp" type="image/webp" />
                <img src="assets/photos/freedom/Sunday_in_Little_Rock,_Ark.,_1935._(3109755087).jpg" alt="Outside Black church Little Rock 1935" loading="lazy" decoding="async" />
              </picture>
              <figcaption>Sunday in Little Rock, Arkansas, 1935. Ben Shahn, public domain.</figcaption>
            </figure>
            <div class="ground-step__text">
              <p class="ground-step__label">Institution-building</p>
              <h3>Sunday best as public argument</h3>
              <p>
                Church photographs can flatten complexity into respectability clichés if we stop at hats and hems. They can also document congregation-level refusal to accept Jim Crow's moral hierarchy on its own terms.
              </p>
            </div>
          </article>
        </div>

        <div class="prose narrow">
          <p>
            LeFlouria's work on convict labor keeps the state in view when we tell freedom stories. The same courts and contracts that emancipation opened could re-ensnare Black women through fines, vagrancy enforcement, and leased labor that dressed coercion as reform (LeFlouria 2015). That history matters for reading respectability without sentimentality. Sunday hats and club mottoes sat beside survival tactics forged in institutions that were happy to borrow Black women's labor while denying their full citizenship.
          </p>
        </div>

        <article class="freedom-essay-pair" aria-labelledby="freedom-walker-heading">
          <div class="freedom-essay-pair__text">
            <h3 class="freedom-essay-pair__title" id="freedom-walker-heading">Spectacle and entrepreneurship</h3>
            <p>
              Madam C. J. Walker's visibility makes entrepreneurship look like individual triumph in photographs that circulate easily online. Hunter and Salem both push against flattening that archive into a single icon. Walker intervened in beauty commerce at a moment when Black women's hair became a national obsession for strangers (Salem 1990). The portrait belongs beside this paragraph because the essay is tracing how presentation became national inventory. The image is not an ornament after the fact. It is part of the evidence trail for how uplift markets staged Black women's bodies for spectators who rarely credited interior motive.
            </p>
          </div>
          <figure class="freedom-essay-pair__fig">
            <picture><source srcset="assets/photos/activism/Madam_C._J._Walker_0268.webp" type="image/webp" /><img src="assets/photos/activism/Madam_C._J._Walker_0268.jpg" alt="Madam C J Walker portrait" loading="lazy" decoding="async" /></picture>
            <figcaption class="freedom-essay-pair__credit">Portrait. Wikimedia Commons.</figcaption>
          </figure>
        </article>

        <article class="freedom-essay-pair freedom-essay-pair--reverse" aria-labelledby="freedom-burroughs-heading">
          <div class="freedom-essay-pair__text">
            <h3 class="freedom-essay-pair__title" id="freedom-burroughs-heading">Schools, clubs, and collective defense</h3>
            <p>
              Burroughs and the NACW milieu built schools and club networks that treated training and public presentation as tools of collective defense (Salem 1990; Hunter 1997). Federated organizing treated deportment as shelter when courts and employers refused shelter in any simpler form. Burroughs's formal portrait therefore belongs in the argument as more than biography. It signs the institution-centered leadership historians attach to respectability frameworks while also indexing labor spent making Black women's competence visible to hostile gatekeepers.
            </p>
          </div>
          <figure class="freedom-essay-pair__fig">
            <picture><source srcset="assets/photos/activism/Nannie_Helen_Burroughs,_1879-_(LOC)_-_Flickr_-_The_Library_of_Congress.webp" type="image/webp" /><img src="assets/photos/activism/Nannie_Helen_Burroughs,_1879-_(LOC)_-_Flickr_-_The_Library_of_Congress.jpg" alt="Nannie Helen Burroughs" loading="lazy" decoding="async" /></picture>
            <figcaption class="freedom-essay-pair__credit">Portrait. Library of Congress.</figcaption>
          </figure>
        </article>

        <div class="chart-mockup chart-mockup--macro freedom-chart-with-seal">
          <div class="chart-mockup__grid">
            <div class="chart-mockup__copy chart-annotations chart-mockup__copy--macro">
              <div class="freedom-seal-copy">
                <div class="freedom-seal-copy__text">
                  <h3 class="freedom-essay-pair__title" id="freedom-seal-heading">Emblem and enrollment</h3>
                  <p class="freedom-seal-lede">
                    The National Association of Colored Women's Clubs seal and the club counts in the chart belong to one motion: uplift as public strategy and mutual aid as shelter when uplift rhetoric failed. The seal turned federated purpose into a legible badge on letterhead and programs. The chart suggests scale. Read together, emblem and graph argue that respectability traveled through institutions that counted members and trained speakers, not only through individual portraits (Jones 1990; Salem 1990).
                  </p>
                </div>
                <figure class="chart-mockup__context-fig chart-mockup__context-fig--seal freedom-seal-copy__fig">
                  <picture><source srcset="assets/photos/activism/Nacwc_logo.webp" type="image/webp" /><img src="assets/photos/activism/Nacwc_logo.png" alt="NACWC seal" loading="lazy" decoding="async" /></picture>
                  <figcaption class="freedom-essay-pair__credit">Seal (&ldquo;Lifting As We Climb&rdquo;). Reproduced for identification; fair use.</figcaption>
                </figure>
              </div>
              <h3 class="chart-mockup__title">Institution-building as respectability's public face</h3>
              <p class="chart-claim">The bars chart approximate cumulative NACW affiliated club growth from founding through the mid-1920s (Jones 1990; Salem 1990).</p>
              <p class="chart-caveat">Counts vary by historian and definition of affiliation. Use this as directional context tied to Part 3, not as a precise census.</p>
            </div>
            <div class="chart-mockup__charts">
              <figure class="card chart-mockup__card">
                <figcaption class="card-head"><h3>NACW affiliated clubs, 1896 to 1924</h3></figcaption>
                <div class="chart-canvas-wrap chart-canvas-wrap--tall"><canvas id="chart-nacw"></canvas></div>
              </figure>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section id="timeline" class="section">
      <div class="section-head">
        <p class="section-step">Timeline</p>
        <h2>Sixteen moments, 1818 to 2024</h2>
        <p class="section-lede">Use the horizontal rail on desktop. Pause if you want to read slowly.</p>
      </div>
      <figure class="ground-photo ground-photo-wide timeline-photo-bleed">
        <picture>
          <source srcset="assets/photos/freedom/Women-riding-on-the-subway.webp" type="image/webp" />
          <img src="assets/photos/freedom/Women-riding-on-the-subway.jpeg" alt="Women on subway as timeline header image" loading="lazy" decoding="async" />
        </picture>
        <figcaption>Public transit photographs repeat across decades because Black women's mobility stayed politically charged.</figcaption>
      </figure>
      <div class="timeline-scroll-shell" id="timeline-shell">
        <div class="timeline-controls" aria-label="Timeline controls">
          <button id="timeline-play-toggle" class="ghost-btn timeline-btn" type="button" aria-pressed="false">
            <span class="ghost-btn__text">Play timeline</span>
          </button>
          <button id="timeline-restart" class="ghost-btn timeline-btn timeline-btn--subtle" type="button">
            <span class="ghost-btn__text">Restart</span>
          </button>
        </div>
        <div class="timeline-h-scroll" id="timeline-scroll" data-autoplay="true" tabindex="0" aria-label="Historical timeline">
          <ol class="timeline timeline-rail" id="timeline-list"></ol>
        </div>
      </div>
    </section>

    <div class="section-bridge" aria-label="Transition">
      <p class="section-bridge__from">Timeline sets sequence.</p>
      <p class="section-bridge__to"><a href="#part4-activism">Next: Wells and the lynching script ↓</a></p>
    </div>

    <section id="part4-activism" class="section">
      <div class="section-head">
        <p class="section-step">Part 4</p>
        <h2>Activism: Wells against the lynching script</h2>
        <p class="section-lede">
          Ida B. Wells's pamphlet Southern Horrors treats lynching as documented practice rather than rumor (Wells 1892). Gail Bederman reads Wells's transatlantic strategy inside contested ideals of civilization and manhood (Bederman 1995).
        </p>
      </div>
      <div class="prose narrow">
        <p>
          Wells weaponized print circulation against newspapers that dignified mob murder as honor. That choice forced readers to confront testimony they preferred to leave unreadable. Respectability language appears in her appeals to audiences abroad because she understood how northern gatekeepers rewarded Black speakers who could translate grief into formats they recognized.
        </p>
        <p>
          Bederman helps name what Wells was navigating when she spoke about civilization to audiences invested in their own innocence (Bederman 1995). The speaker who refused lynching apologias had to calibrate tone in print because readers trained on racist tropes could punish Black women for sounding either too angry or too detached. Photographs of activists and educators from the era belong to the same tactical field: clothing, posture, and caption copy trained spectators to grant seriousness before granting belief.
        </p>
      </div>
      <div class="grid-2">
        <figure class="card">
          <picture><img src="assets/photos/activism/activism-card-1.jpg" alt="Burroughs portrait for uplift era" loading="lazy" decoding="async" /></picture>
          <figcaption>Nannie Helen Burroughs. Library of Congress. Institution-building and training networks treated public presentation as strategy, not accessory, within debates over uplift and respectability.</figcaption>
        </figure>
        <figure class="card">
          <picture><img src="assets/photos/activism/activism-card-2.jpg" alt="Women activism historical photo" loading="lazy" decoding="async" /></picture>
          <figcaption>Women's rights demonstration; placards and crowd density compress political demand into a frame built for newspapers and later archives.</figcaption>
        </figure>
      </div>
    </section>

    <section id="part5-blues" class="section section-inequality">
      <div class="section-head">
        <p class="section-step">Part 5</p>
        <h2>The Blues and Passing: Dissemblance set to music and fiction</h2>
        <p class="section-lede">
          Angela Davis recovers blues discourse as a space where Black women named desire and violence that uplift sermons often coded indirectly (Davis 1998). Nella Larsen's Passing tracks racial passing as a survival technique with psychic costs (Larsen 1929). Rebecca Hall's film adaptation updates that argument for audiences trained by twenty-first century surveillance culture (Hall 2020).
        </p>
      </div>
      <div class="prose narrow">
        <p>
          Respectability could treat blueswomen as scandal. Davis argues that scandal reading misses how Ma Rainey and Bessie Smith shaped audiences who heard truth in timbre, not only in lyric sheets (Davis 1998). Larsen turns passing into narrative pressure so readers cannot pretend visibility equals authenticity (Larsen 1929).
        </p>
        <p>
          Passing in fiction is dissemblance narrated as plot. Irene's surveillance of Clare is also a mirror for historians who treat Black women's social performances as puzzles to solve rather than strategies to respect (Larsen 1929). Hall's film makes those gazes contemporary by tightening the frame until viewers feel how friendship and desire crosscut racial terror in domestic space (Hall 2020). The Cruz portrait included here is not a blueswoman substitute; it marks diaspora performance lineage when syllabi move from southern tent shows toward broader debates about stage persona, glamour, and refusal.
        </p>
      </div>
      <div class="grid-2">
        <figure class="card">
          <picture><source srcset="assets/photos/blues/Celia_Cruz_1957_color.webp" type="image/webp" /><img src="assets/photos/blues/Celia_Cruz_1957_color.jpg" alt="Celia Cruz 1957" loading="lazy" decoding="async" /></picture>
          <figcaption>Celia Cruz, 1957 (colorized). Wikimedia Commons. Marks diaspora performance lineage beside blues-era arguments about persona, glamour, and refusal onstage.</figcaption>
        </figure>
        <figure class="card">
          <picture><source srcset="assets/photos/blues/womens-peace-party.webp" type="image/webp" /><img src="assets/photos/blues/womens-peace-party.jpg" alt="Woman's Peace Party preamble and platform, Washington, January 1915" loading="lazy" decoding="async" /></picture>
          <figcaption>Woman's Peace Party, &ldquo;Preamble and Platform,&rdquo; adopted at Washington, D.C., January 10, 1915. Printed platform leaf; pacifist women's organizing circulated constitutional and diplomatic demands on paper as well as in the street.</figcaption>
        </figure>
      </div>
    </section>

    <section id="part6-civilrights" class="section">
      <div class="section-head">
        <p class="section-step">Part 6</p>
        <h2>Civil Rights and Black Power: The body politic</h2>
        <p class="section-lede">
          Danielle McGuire reframes civil rights origins through sexual violence and community mobilization (McGuire 2004). Barbara Ransby refuses icon-only memory by recovering Ella Baker's organizing theory (Ransby 2025). The Combahee River Collective Statement names politics that exceed narrow respectability scripts (CRC 1977). Audre Lorde theorizes anger as insight rather than embarrassment (Lorde 1981).
        </p>
      </div>
      <div class="prose narrow">
        <p>
          The Tougaloo Nine staged respectability as tactical uniform while refusing segregation's degrading rules. Natural hair movements later refused a cosmetic respectability tied to proximity to whiteness. Both moves show strategy, not naivete, about how spectators read Black women's bodies.
        </p>
        <p>
          McGuire insists that civil rights memory loses its explanatory power if it skips testimony Black women offered about assault and community defense long before national cameras arrived (McGuire 2004). That argument clarifies why dissemblance and disclosure both appear inside movement politics: some truths had to be spoken to mobilize, others had to be guarded from hostile courts and press. Ransby's Baker refuses Great Man history by tracking democratic organizing methods that trusted ordinary people's capacity to lead (Ransby 2025). Combahee named identities and politics that respectability scripts often muted (CRC 1977). Lorde named anger as knowledge that could sharpen coalition rather than break it (Lorde 1981).
        </p>
      </div>
      <div class="grid-2">
        <figure class="card">
          <picture><img src="assets/photos/civilrights/tougaloo-nine.webp" alt="Tougaloo Nine" loading="lazy" decoding="async" /></picture>
          <figcaption>The Tougaloo Nine after the Jackson Municipal Library sit-in, March 1961. Archival photograph widely used in civil rights curricula (including Smithsonian educational materials).</figcaption>
        </figure>
        <figure class="card">
          <picture><source srcset="assets/photos/civilrights/Natural_Afro_-_hair_type_4c-_model_Gwyneth_Ellis.webp" type="image/webp" /><img src="assets/photos/civilrights/Natural_Afro_-_hair_type_4c-_model_Gwyneth_Ellis.jpg" alt="Natural afro portrait" loading="lazy" decoding="async" /></picture>
          <figcaption>Natural Type 4c hair (model Gwyneth Ellis). Stephen Dickson, CC BY-SA 4.0. Pairs natural hair politics with movement-era debates over appearance and citizenship.</figcaption>
        </figure>
        <figure class="card">
          <picture><source srcset="assets/photos/civilrights/Black%20Panther%20Party%201.webp" type="image/webp" /><img src="assets/photos/civilrights/Black%20Panther%20Party%201.jpg" alt="Black Panther Party archival photo" loading="lazy" decoding="async" /></picture>
          <figcaption>Black Panther Party, movement-era archival photograph. Community programs and street-facing politics complicated which bodies national media treated as respectable leadership.</figcaption>
        </figure>
      </div>
    </section>

    <section id="part7-contemporary" class="section">
      <div class="section-head">
        <p class="section-step">Part 7</p>
        <h2>Contemporary inner lives: Competency, medicine, girlhood</h2>
        <p class="section-lede">
          Christina Sharpe theorizes the wake as daily atmosphere rather than past tense metaphor (Sharpe 2024). Linda Villarosa tracks how racism reshapes clinical perception of Black pain (Villarosa 2022). Tressie McMillan Cottom analyzes beauty and competence as disciplinary economies for Black women in public culture (Cottom 2019). Epstein, Blake, and González document adultification of Black girls in institutional settings (Epstein, Blake, and González 2017).
        </p>
      </div>
      <figure class="card">
        <figcaption class="card-head"><h3>BA attainment among Black women age 25 plus, 1940 to 2022</h3><p>Educational attainment is not the same as protection.</p></figcaption>
        <div class="chart-canvas-wrap chart-canvas-wrap--tall"><canvas id="chart-ba"></canvas></div>
        <p class="chart-caveat">Series blends Census decennial and American Community Survey estimates for visualization (U.S. Census Bureau).</p>
      </figure>
      <div class="prose narrow">
        <p>
          Anita Hill's 1991 testimony remains a lecture-ready example of how Black women's speech faces credibility traps layered by gender and race. Megan Thee Stallion and Beyoncé operate in a different genre, yet each negotiates hypervisibility where misogynoir converts confidence into evidence for punishment (Cottom 2019). Kirby Dick and Amy Ziering's On the Record forces viewers to reckon with music industry gatekeeping and Black women's testimony (Dick and Ziering 2020).
        </p>
        <p>
          Villarosa's reporting matters here because medical institutions repeat some of the same credibility hierarchies that courts and entertainment industries do. Pain dismissed as attitude becomes a policy problem shaped by race and gender (Villarosa 2022). Epstein, Blake, and González show school discipline pipelines treating Black girls as older than they are, which converts protection language into punishment logistics (Epstein, Blake, and González 2017). Those studies belong in one essay with Sharpe because they describe ordinary environments where interior life gets overwritten by adult scripts imposed from outside.
        </p>
        <p>
          Sherald's Breonna Taylor portrait compresses several threads at once: memorial practice, Black figurative painting's public power, and the cruel gap between visibility and justice (Princenthal 2024). The Say Her Name frame, renewed in public mourning for Sonya Massey and others, repeats the essay's central problem in present tense. Names circulate nationally while institutions still struggle to credit Black women's testimony at full depth.
        </p>
      </div>
      <div class="grid-2 grid-2--media-cards">
        <figure class="card card--media">
          <picture><source srcset="assets/photos/contemporary/Michelle_Obama_2013_official_portrait.webp" type="image/webp" /><img src="assets/photos/contemporary/contemporary-card-1.jpg" alt="Michelle Obama official portrait" loading="lazy" decoding="async" /></picture>
          <figcaption>Michelle Obama, official portrait, 2013 (Chuck Kennedy, White House). National political aesthetics treat Black women's self-presentation as a referendum on competence and belonging.</figcaption>
        </figure>
        <figure class="card card--media">
          <picture><img src="assets/photos/contemporary/contemporary-card-2.webp" alt="Women activists with protest signs" loading="lazy" decoding="async" /></picture>
          <figcaption>Contemporary protest; bodies, signage, and slogans compress rights claims into imagery made for mass circulation.</figcaption>
        </figure>
        <figure class="card card--media">
          <picture><img src="assets/photos/contemporary/contemporary-card-3.webp" alt="Women's International League for Peace and Freedom logo" loading="lazy" decoding="async" /></picture>
          <figcaption>Women's International League for Peace and Freedom emblem; transnational women's reform circuits threaded respectability language through peace and labor campaigns.</figcaption>
        </figure>
      </div>
    </section>

    <section id="conclusions" class="section">
      <div class="section-head">
        <p class="section-step">Part 8</p>
        <h2>Conclusion: Shield, cage, refusal</h2>
      </div>
      <div class="conclusion-stack">
        <div class="card conclusion-stack__card"><h3 class="card-title">Shield</h3><p>Dissemblance protected interior life when exposure meant danger (Hine 1989).</p></div>
        <div class="card conclusion-stack__card"><h3 class="card-title">Cage</h3><p>Respectability could discipline Black women who needed access to institutions controlled by outsiders (Higginbotham 1993).</p></div>
        <div class="card conclusion-stack__card"><h3 class="card-title">Refusal</h3><p>Blues, collective statements, and contemporary portraiture keep rewriting what counts as legible truth (Davis 1998; CRC 1977; Sharpe 2024).</p></div>
      </div>
      <p class="prose narrow">
        After a quarter of reading for this course, I hold a simpler rule alongside the complicated ones. When a source sounds too neat about Black women's motives, return to the gap between performance and interiority. That gap is not emptiness. It is history's unfinished homework.
      </p>
      <p class="prose narrow">
        If respectability sometimes worked like a cage, it also worked like a key for people who needed leverage inside hostile institutions. If dissemblance sometimes worked like a shield, it also forced Black women to spend cognitive labor on audiences who rarely returned the effort of careful listening. The blues, Combahee, Lorde, and contemporary painters do not cancel those tensions. They keep naming them in forms that invite audiences to hear interior claims without demanding spectacle as proof (Davis 1998; CRC 1977; Lorde 1981; Sharpe 2024).
      </p>
      <div class="card quote-orbit-card">
        <h3 class="card-title">Voices from the record</h3>
        <div id="quote-orbit" class="quote-orbit" tabindex="0" aria-label="Quotation carousel" data-autoplay="false">
          <div class="quote-orbit__stage">
            <div class="quote-orbit__ring" id="quote-orbit-ring">
              <img class="quote-orbit__face" id="quote-orbit-face" src="assets/photos/antebellum/women-activist-1.jpg" alt="" />
            </div>
          </div>
          <div class="quote-orbit__panel">
            <div class="quote-orbit__copy" id="quote-orbit-copy" aria-live="polite">
              <h4 class="quote-orbit__name" id="quote-orbit-name"></h4>
              <p class="quote-orbit__designation" id="quote-orbit-designation"></p>
              <blockquote class="quote-orbit__quote" id="quote-orbit-quote"></blockquote>
            </div>
            <div class="quote-orbit__controls">
              <button type="button" class="quote-orbit__arrow quote-orbit__arrow--prev" id="quote-orbit-prev" aria-label="Previous quotation"><span aria-hidden="true">&#10094;</span></button>
              <button type="button" class="quote-orbit__arrow quote-orbit__arrow--next" id="quote-orbit-next" aria-label="Next quotation"><span aria-hidden="true">&#10095;</span></button>
            </div>
            <div class="quote-orbit__dots" id="quote-orbit-dots" aria-label="Select quotation"></div>
          </div>
        </div>
      </div>
    </section>

    <section id="sources" class="section">
      <div class="section-head">
        <p class="section-step">Part 9</p>
        <h2>Sources and bibliography (Chicago author-date)</h2>
      </div>
      <div class="grid-3">
        <div class="card">
          <h3 class="card-title">Secondary sources</h3>
          <ul class="link-list">
            <li>Bederman, Gail. 1995. <em>Manliness and Civilization</em>. Chicago: University of Chicago Press.</li>
            <li>Brown, Elsa Barkley. 1992. "What Has Happened Here." <em>Feminist Studies</em> 18 (2): 295-312.</li>
            <li>Cottom, Tressie McMillan. 2019. <em>Thick</em>. New York: New Press.</li>
            <li>Crenshaw, Kimberlé. 2016. "The Urgency of Intersectionality." TEDWomen lecture.</li>
            <li>Davis, Angela Y. 1998. <em>Blues Legacies and Black Feminism</em>. New York: Pantheon.</li>
            <li>Cooper Owens, Deirdre. 2017. <em>Medical Bondage</em>. Athens: University of Georgia Press.</li>
            <li>Higginbotham, Evelyn Brooks. 1993. <em>Righteous Discontent</em>. Cambridge, MA: Harvard University Press.</li>
            <li>Hine, Darlene Clark. 1989. "Rape and the Inner Lives of Black Women in the Middle West." <em>Signs</em> 14 (4): 912-20.</li>
            <li>Hunter, Tera W. 1997. <em>To 'Joy My Freedom</em>. Cambridge, MA: Harvard University Press.</li>
            <li>Jones, Adrienne Lash. 1990. "NACW." In <em>Black Women in United States History</em>, edited by Darlene Clark Hine. Carlson.</li>
            <li>LeFlouria, Talitha. 2015. <em>Chained in Silence</em>. Chapel Hill: University of North Carolina Press.</li>
            <li>May, Vivian M. 2012. "Intellectual Genealogies, Intersectionality, and Anna Julia Cooper." In <em>Feminist Solidarity at the Crossroads</em>, edited by Kim Marie Walker and Roseanna L. Dufault, 131-60. New York: Routledge.</li>
            <li>McGuire, Danielle L. 2004. "It Was Like All of Us Had Been Raped." <em>Journal of American History</em> 91 (3): 904-31.</li>
            <li>Miles, Tiya. 2021. <em>All That She Carried</em>. New York: Random House.</li>
            <li>Painter, Nell Irvin. 1995. "Soul Murder." In <em>Southern History Across the Color Line</em>, 15-39. Chapel Hill: University of North Carolina Press.</li>
            <li>Princenthal, Nancy. 2024. "Amy Sherald, Brazen Optimist." <em>New York Times</em>, September 9, 2024.</li>
            <li>Ransby, Barbara. 2025. <em>Ella Baker and the Black Freedom Struggle</em>. Berkeley: University of California Press.</li>
            <li>Salem, Dorothy. 1990. <em>To Better Our World</em>. Brooklyn: Carlson.</li>
            <li>Sharpe, Christina. 2016. <em>In the Wake: On Blackness and Being</em>. Durham, NC: Duke University Press.</li>
            <li>Sharpe, Christina. 2024. <em>Ordinary Notes</em>. New York: Farrar, Straus and Giroux.</li>
            <li>Villarosa, Linda. 2022. <em>Under the Skin</em>. New York: Doubleday.</li>
          </ul>
        </div>
        <div class="card">
          <h3 class="card-title">Primary sources and films</h3>
          <ul class="link-list">
            <li>Combahee River Collective (CRC). 1977. "The Combahee River Collective Statement."</li>
            <li>Dick, Kirby, and Amy Ziering. 2020. <em>On the Record</em>. Film.</li>
            <li>Hall, Rebecca. 2020. <em>Passing</em>. Film.</li>
            <li>Jacobs, Harriet. 1861. <em>Incidents in the Life of a Slave Girl</em>.</li>
            <li>Larsen, Nella. 1929. <em>Passing</em>.</li>
            <li>Lorde, Audre. 1981. "The Uses of Anger."</li>
            <li>Wells, Ida B. 1892. <em>Southern Horrors</em>.</li>
          </ul>
        </div>
        <div class="card">
          <h3 class="card-title">Data and images</h3>
          <ul class="link-list">
            <li>BLS (Current Population Survey). Various years.</li>
            <li>Goldin, Claudia. 1990. <em>Understanding the Gender Gap</em>. New York: Oxford University Press.</li>
            <li>IPUMS USA. Integrated census microdata extracts.</li>
            <li>U.S. Census Bureau. Decennial census and American Community Survey tabulations.</li>
            <li>Image credits and licenses: <a href="assets/CREDITS.md">assets/CREDITS.md</a>.</li>
          </ul>
        </div>
      </div>
      <p class="section-lede">SFMOMA exhibition reference for Sherald: American Sublime (2024).</p>
    </section>

    <footer class="footer">
      <p>Stanford History 54N, Spring 2026. Author: Sunmit Hallur.</p>
    </footer>
  </main>

  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.4/dist/chart.umd.min.js"></script>
  <script src="app.js"></script>
</body>
</html>
'''

def apply_asset_version(html: str) -> str:
    """Bust browser cache on every build so local preview picks up CSS/JS changes."""
    v = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")
    html = html.replace('href="styles.css"', f'href="styles.css?v={v}"')
    html = html.replace('href="print.css"', f'href="print.css?v={v}"')
    html = html.replace('src="app.js"', f'src="app.js?v={v}"')
    return html


OUT.write_text(apply_asset_version(HTML), encoding="utf-8")
print("Wrote", OUT)
