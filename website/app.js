/* History 54N · visual essay: timeline, Chart.js, quote orbit, scroll spy (forked from Econ 30 patterns). */
(() => {
  "use strict";

  const $ = (sel, root = document) => root.querySelector(sel);
  const $$ = (sel, root = document) => [...root.querySelectorAll(sel)];

  const themeKey = "history54n-theme";
  const cssVar = name => getComputedStyle(document.documentElement).getPropertyValue(name).trim();
  const palette = () => ({
    bg: cssVar("--bg"),
    fg: cssVar("--fg"),
    muted: cssVar("--fg-muted"),
    rule: cssVar("--rule"),
    accent: cssVar("--accent"),
    accentSoft: cssVar("--accent-soft"),
    "chart-lfp": cssVar("--chart-lfp"),
    "chart-nacw": cssVar("--chart-nacw"),
    "chart-ba": cssVar("--chart-ba"),
  });

  const applyTheme = t => {
    document.documentElement.dataset.theme = t;
    const icon = $("#theme-toggle .theme-icon");
    const btn = $("#theme-toggle");
    if (icon) icon.textContent = t === "dark" ? "◑" : "◐";
    if (btn) {
      btn.setAttribute("aria-pressed", t === "dark" ? "true" : "false");
      btn.setAttribute("aria-label", t === "dark" ? "Switch to light theme" : "Switch to dark theme");
    }
  };
  const initialTheme = () =>
    localStorage.getItem(themeKey) ||
    (window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
  applyTheme(initialTheme());
  $("#theme-toggle")?.addEventListener("click", () => {
    const cur = document.documentElement.dataset.theme === "dark" ? "light" : "dark";
    localStorage.setItem(themeKey, cur);
    applyTheme(cur);
    refreshAllChartsForTheme();
  });

  const formatChartTickPlain = value => {
    const n = Number(value);
    if (!Number.isFinite(n)) return String(value);
    if (Number.isInteger(n)) return String(n);
    const r = Math.round(n);
    if (Math.abs(n - r) < 1e-9) return String(r);
    return n.toLocaleString(undefined, { useGrouping: false, maximumFractionDigits: 8 });
  };

  const setChartDefaults = () => {
    const p = palette();
    Chart.defaults.font.family = '"Libre Franklin", -apple-system, system-ui, sans-serif';
    Chart.defaults.color = p.muted;
    Chart.defaults.borderColor = p.rule;
    Chart.defaults.plugins.legend.labels.color = p.fg;
  };
  setChartDefaults();

  const applyPaletteToChart = chart => {
    const p = palette();
    const o = chart.options;
    if (o.plugins?.legend?.labels) o.plugins.legend.labels.color = p.fg;
    chart.data.datasets.forEach(ds => {
      if (!ds.paletteKey || !p[ds.paletteKey]) return;
      const color = p[ds.paletteKey];
      const border = `${color}${ds.colorAlpha ?? ""}`;
      ds.borderColor = border;
      ds.backgroundColor = `${color}${ds.backgroundAlpha ?? "33"}`;
      if ("pointBackgroundColor" in ds && ds.pointBackgroundColor !== undefined) {
        ds.pointBackgroundColor = border;
      }
    });
    Object.values(o.scales || {}).forEach(scale => {
      if (!scale || typeof scale !== "object") return;
      if (scale.ticks) scale.ticks.color = p.muted;
      if (scale.grid) scale.grid.color = p.rule;
      if (scale.title?.display) scale.title.color = p.muted;
    });
    chart.update();
  };

  const refreshAllChartsForTheme = () => {
    setChartDefaults();
    document.querySelectorAll("canvas").forEach(canvas => {
      const c = Chart.getChart?.(canvas);
      if (c) applyPaletteToChart(c);
    });
  };

  const annotationPlugin = {
    id: "essayAnnotation",
    afterDraw(chart, _args, opts) {
      const items = opts?.items;
      if (!Array.isArray(items) || !items.length || !chart?.scales?.x || !chart?.scales?.y) return;
      const { ctx, chartArea, scales } = chart;
      const pal = palette();
      ctx.save();
      items.forEach(item => {
        if (item.type === "band") {
          const x1 = scales.x.getPixelForValue(item.x1);
          const x2 = scales.x.getPixelForValue(item.x2);
          ctx.fillStyle = item.fill || pal.accentSoft;
          ctx.fillRect(x1, chartArea.top, x2 - x1, chartArea.bottom - chartArea.top);
          ctx.fillStyle = item.color || pal.fg;
          ctx.font = '600 11px "Libre Franklin", sans-serif';
          ctx.fillText(item.label || "", x1 + 6, chartArea.top + 14);
        } else if (item.type === "marker") {
          const x = scales.x.getPixelForValue(item.x);
          ctx.strokeStyle = item.color || pal.rule;
          ctx.lineWidth = item.width || 1.25;
          ctx.setLineDash(item.dash || [4, 4]);
          ctx.beginPath();
          ctx.moveTo(x, chartArea.top);
          ctx.lineTo(x, chartArea.bottom);
          ctx.stroke();
          ctx.setLineDash([]);
          ctx.fillStyle = item.color || pal.fg;
          ctx.font = '600 11px "Libre Franklin", sans-serif';
          ctx.fillText(item.label || "", x + 5, chartArea.top + 14 + (item.dy || 0));
        }
      });
      ctx.restore();
    },
  };

  const makeLineChart = (canvasEl, { datasets, yTitle, xTitle, annotations = [], xMin, xMax }) => {
    const p = palette();
    if (Chart.registry && !Chart.registry.plugins.get("essayAnnotation")) {
      Chart.register(annotationPlugin);
    }
    return new Chart(canvasEl, {
      type: "line",
      data: { datasets },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        interaction: { intersect: false, mode: "index" },
        parsing: false,
        plugins: {
          legend: { position: "bottom", labels: { usePointStyle: true, boxWidth: 8 } },
          essayAnnotation: { items: annotations },
          tooltip: {
            callbacks: {
              title(items) {
                if (!items.length) return "";
                const x = items[0].parsed?.x;
                return x != null && Number.isFinite(x) ? formatChartTickPlain(x) : "";
              },
              label(ctx) {
                const name = ctx.dataset.label ?? "";
                const y = ctx.parsed?.y;
                if (y == null || !Number.isFinite(y)) return name;
                return name ? `${name}: ${formatChartTickPlain(y)}` : formatChartTickPlain(y);
              },
            },
          },
        },
        scales: {
          x: {
            type: "linear",
            ...(xMin != null ? { min: xMin } : {}),
            ...(xMax != null ? { max: xMax } : {}),
            title: xTitle ? { display: true, text: xTitle, color: p.muted } : { display: false },
            grid: { color: p.rule, drawBorder: false },
            ticks: {
              color: p.muted,
              maxRotation: 0,
              autoSkip: true,
              maxTicksLimit: 6,
              callback: formatChartTickPlain,
            },
          },
          y: {
            title: yTitle ? { display: true, text: yTitle, color: p.muted } : { display: false },
            grid: { color: p.rule, drawBorder: false },
            ticks: { color: p.muted, callback: formatChartTickPlain },
          },
        },
        elements: {
          line: { tension: 0.25, borderWidth: 2 },
          point: { radius: 3, hoverRadius: 5 },
        },
      },
    });
  };

  const makeBarChart = (canvasEl, { datasets, yTitle, xTitle, annotations = [], xMin, xMax }) => {
    const p = palette();
    if (Chart.registry && !Chart.registry.plugins.get("essayAnnotation")) {
      Chart.register(annotationPlugin);
    }
    return new Chart(canvasEl, {
      type: "bar",
      data: { datasets },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        parsing: false,
        plugins: {
          legend: { position: "bottom", labels: { usePointStyle: true, boxWidth: 8 } },
          essayAnnotation: { items: annotations },
          tooltip: {
            callbacks: {
              title(items) {
                if (!items.length) return "";
                const x = items[0].parsed?.x;
                return x != null && Number.isFinite(x) ? formatChartTickPlain(x) : "";
              },
              label(ctx) {
                const name = ctx.dataset.label ?? "";
                const y = ctx.parsed?.y;
                if (y == null || !Number.isFinite(y)) return name;
                return name ? `${name}: ${formatChartTickPlain(y)}` : formatChartTickPlain(y);
              },
            },
          },
        },
        scales: {
          x: {
            type: "linear",
            ...(xMin != null ? { min: xMin } : {}),
            ...(xMax != null ? { max: xMax } : {}),
            title: xTitle ? { display: true, text: xTitle, color: p.muted } : { display: false },
            grid: { color: p.rule, drawBorder: false },
            ticks: {
              color: p.muted,
              autoSkip: true,
              maxTicksLimit: 6,
              callback: formatChartTickPlain,
            },
          },
          y: {
            beginAtZero: true,
            title: yTitle ? { display: true, text: yTitle, color: p.muted } : { display: false },
            grid: { color: p.rule, drawBorder: false },
            ticks: { color: p.muted, callback: formatChartTickPlain },
          },
        },
      },
    });
  };

  const TIMELINE = [
    { year: "1818", title: "Truth born", body: "Sojourner Truth's life begins in slavery; her later cartes de visite and speeches outlast archives that recorded her as property." },
    { year: "1861", title: "Jacobs publishes Incidents", body: "Harriet Jacobs prints seven years in a garret—concealment as the condition for narrating freedom under coercion." },
    { year: "1881", title: "Atlanta washerwomen strike", body: "Black washerwomen strike for wage control; Hunter reads it as labor politics authored by women, not household footnote." },
    { year: "1892", title: "Southern Horrors", body: "Ida B. Wells names victims and press lies in print, countering newspapers that called lynching honorable." },
    { year: "1896", title: "NACW founded", body: "National Association of Colored Women federates clubs that pair uplift rhetoric with schools and mutual aid." },
    { year: "1900", title: "Burroughs names barriers", body: "Nannie Helen Burroughs documents how sexism inside Black politics hindered women's leadership." },
    { year: "1909", title: "National Training School", body: "Burroughs opens a Washington training school—deportment taught as defense against white employers, landlords, and courts." },
    { year: "1917", title: "Walker and national wealth", body: "Madam C. J. Walker's hair-care empire makes Black women's grooming a national market—and a public spectacle." },
    { year: "1929", title: "Larsen's Passing", body: "Nella Larsen's novel stages racial passing as intimacy and surveillance with psychic costs." },
    { year: "1955", title: "Montgomery bus boycott", body: "Montgomery organizers mobilize dignity politics; domestic workers' labor underwrites mass protest." },
    { year: "1961", title: "Tougaloo Nine", body: "Nine Tougaloo students sit in at a whites-only library wearing Sunday dress—respectability as tactical uniform." },
    { year: "1977", title: "Combahee Statement", body: "Combahee River Collective names intersectional politics that narrow respectability scripts could not hold." },
    { year: "1981", title: "Lorde on anger", body: "Audre Lorde argues anger against racism is information, not a flaw to manage for white comfort." },
    { year: "1991", title: "Anita Hill testimony", body: "Anita Hill testifies before the Senate; televised disbelief shows credibility traps for Black women accusing powerful men." },
    { year: "2013", title: "Obama official portrait", body: "Michelle Obama's White House portrait intensifies scrutiny of Black women's dress, competence, and composure." },
    { year: "2024", title: "Sherald, American Sublime", body: "Amy Sherald's SFMOMA retrospective, including Breonna Taylor, links portraiture to mourning and delayed justice." },
  ];

  const renderTimeline = () => {
    const list = $("#timeline-list");
    if (!list) return;
    TIMELINE.forEach((item, idx) => {
      const li = document.createElement("li");
      const above = idx % 2 === 0;
      li.className = `timeline-node ${above ? "timeline-node--above" : "timeline-node--below"}`;
      const cardInner = `
          <span class="timeline-idx">${String(idx + 1).padStart(2, "0")}</span>
          <span class="year">${item.year}</span>
          <h4>${item.title}</h4>
          <p>${item.body}</p>`;
      li.innerHTML = above
        ? `<div class="timeline-card">${cardInner}</div>
        <div class="timeline-axis-slot" aria-hidden="true">
          <span class="timeline-stem timeline-stem--up"></span>
          <span class="timeline-dot"></span>
        </div>
        <div class="timeline-fill" aria-hidden="true"></div>`
        : `<div class="timeline-fill" aria-hidden="true"></div>
        <div class="timeline-axis-slot" aria-hidden="true">
          <span class="timeline-dot"></span>
          <span class="timeline-stem timeline-stem--down"></span>
        </div>
        <div class="timeline-card">${cardInner}</div>`;
      list.appendChild(li);
    });
  };

  const wireTimelineAutoscroll = () => {
    const scrollEl = $("#timeline-scroll");
    const shell = $("#timeline-shell");
    const listEl = $("#timeline-list");
    const sectionEl = document.getElementById("timeline");
    const playToggleBtn = $("#timeline-play-toggle");
    const restartBtn = $("#timeline-restart");
    if (!scrollEl || !shell) return;

    const mqVerticalRail = window.matchMedia("(max-width: 860px)");
    const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    let autoplay = !reduceMotion && scrollEl.dataset.autoplay === "true";
    let sectionVisible = false;
    let rafId = 0;
    const speed = 0.45;
    const ioTarget = sectionEl || shell;

    const syncChrome = () => {
      scrollEl.classList.toggle("is-autoplay-paused", !autoplay);
      if (!playToggleBtn) return;
      playToggleBtn.setAttribute("aria-pressed", autoplay ? "true" : "false");
      const text = playToggleBtn.querySelector(".ghost-btn__text");
      if (text) text.textContent = autoplay ? "Pause timeline" : "Play timeline";
    };

    const applyTimelineLayoutMode = () => {
      const stacked = mqVerticalRail.matches;
      scrollEl.classList.toggle("timeline-h-scroll--stacked", stacked);
      [playToggleBtn, restartBtn].forEach(btn => {
        if (!btn) return;
        if (stacked) {
          btn.disabled = true;
          btn.setAttribute("aria-disabled", "true");
        } else {
          btn.disabled = false;
          btn.removeAttribute("aria-disabled");
        }
      });
      if (stacked) {
        autoplay = false;
        if (rafId) {
          cancelAnimationFrame(rafId);
          rafId = 0;
        }
        playToggleBtn?.setAttribute("title", "Autoplay applies to the horizontal timeline on wider screens.");
        restartBtn?.setAttribute("title", "Restart applies to the horizontal timeline on wider screens.");
      } else {
        playToggleBtn?.removeAttribute("title");
        restartBtn?.removeAttribute("title");
      }
      syncChrome();
    };

    const tick = () => {
      if (!autoplay || !sectionVisible) {
        rafId = 0;
        return;
      }
      const max = scrollEl.scrollWidth - scrollEl.clientWidth;
      if (max <= 0) {
        rafId = 0;
        return;
      }
      if (scrollEl.scrollLeft >= max - 0.5) {
        scrollEl.scrollLeft = max;
        rafId = 0;
        return;
      }
      scrollEl.scrollLeft = Math.min(max, scrollEl.scrollLeft + speed);
      rafId = requestAnimationFrame(tick);
    };

    const startIfNeeded = () => {
      if (!autoplay || !sectionVisible) return;
      const max = scrollEl.scrollWidth - scrollEl.clientWidth;
      if (max > 0 && scrollEl.scrollLeft >= max - 0.5) scrollEl.scrollLeft = 0;
      if (rafId) return;
      rafId = requestAnimationFrame(tick);
    };

    const toggleAutoplay = () => {
      if (playToggleBtn?.disabled) return;
      autoplay = !autoplay;
      if (!autoplay && rafId) {
        cancelAnimationFrame(rafId);
        rafId = 0;
      }
      syncChrome();
      startIfNeeded();
    };

    const restartTimeline = () => {
      if (restartBtn?.disabled) return;
      scrollEl.scrollLeft = 0;
      startIfNeeded();
    };

    window.addEventListener("resize", () => {
      if (sectionVisible) startIfNeeded();
    });

    if (typeof ResizeObserver !== "undefined") {
      const ro = new ResizeObserver(() => {
        if (sectionVisible) startIfNeeded();
      });
      ro.observe(scrollEl);
      if (listEl) ro.observe(listEl);
    }

    if (document.fonts?.ready) {
      document.fonts.ready.then(() => {
        if (sectionVisible) startIfNeeded();
      });
    }

    const io = new IntersectionObserver(
      entries => {
        entries.forEach(en => {
          sectionVisible = en.isIntersecting;
          if (sectionVisible) startIfNeeded();
          else if (rafId) {
            cancelAnimationFrame(rafId);
            rafId = 0;
          }
        });
      },
      { root: null, threshold: 0 }
    );
    io.observe(ioTarget);
    playToggleBtn?.addEventListener("click", toggleAutoplay);
    restartBtn?.addEventListener("click", restartTimeline);

    mqVerticalRail.addEventListener("change", () => {
      applyTimelineLayoutMode();
      requestAnimationFrame(() => startIfNeeded());
    });
    applyTimelineLayoutMode();
    syncChrome();
  };

  const wireTOC = () => {
    const links = [...$$(".topnav a")];
    const progressFill = document.getElementById("top-progress-fill");
    const indicatorText = document.getElementById("section-indicator-text");
    if (!links.length) return;

    const sectionOrder = [
      "about",
      "argument-summary",
      "part1-question",
      "part2-antebellum",
      "part3-freedom",
      "timeline",
      "part4-activism",
      "part5-blues",
      "part6-civilrights",
      "part7-contemporary",
      "conclusions",
      "sources",
    ];
    const spyIds = ["about", "hero", ...sectionOrder.slice(1, -1), "ask-anything", "sources"];
    const spySections = spyIds.map(id => document.getElementById(id)).filter(Boolean);
    const navHrefForSection = sectionId => {
      if (sectionId === "about") return "#about";
      if (sectionId === "timeline") return "#timeline";
      if (sectionId === "conclusions" || sectionId === "ask-anything") return "#conclusions";
      if (sectionId === "sources") return "#sources";
      return "#hero";
    };
    const sectionLabelById = new Map(
      sectionOrder.map((id, idx) => {
        const h = document.querySelector(`#${CSS.escape(id)} h2`);
        const title = h ? h.textContent.replace(/^\d+\s*[·.-]\s*/, "").trim() : id;
        return [id, `${idx + 1}/${sectionOrder.length} · ${title}`];
      })
    );
    sectionLabelById.set("ask-anything", sectionLabelById.get("conclusions") ?? "Conclusion");

    const readingLineY = () => window.scrollY + window.innerHeight * 0.55;

    const syncProgress = () => {
      if (!progressFill) return;
      const doc = document.documentElement;
      const max = doc.scrollHeight - window.innerHeight;
      const pct = max > 0 ? Math.min(100, Math.max(0, (window.scrollY / max) * 100)) : 0;
      progressFill.style.width = `${pct.toFixed(2)}%`;
    };

    const syncActiveNav = () => {
      const doc = document.documentElement;
      const nearBottom = window.scrollY + window.innerHeight >= doc.scrollHeight - 6;
      const y = readingLineY();
      let activeId = spySections[0]?.id ?? "hero";
      if (nearBottom && spySections.length) {
        activeId = spySections[spySections.length - 1].id;
      } else {
        for (const sec of spySections) {
          const rect = sec.getBoundingClientRect();
          const top = rect.top + window.scrollY;
          const bottom = top + rect.height;
          if (top <= y && bottom > y) {
            activeId = sec.id;
            break;
          }
          if (top <= y) activeId = sec.id;
        }
      }

      const activeNavHref = navHrefForSection(activeId);
      links.forEach(l => {
        l.classList.toggle("active", l.getAttribute("href") === activeNavHref);
      });

      if (indicatorText) {
        indicatorText.textContent =
          activeId === "hero"
            ? "Essay"
            : sectionLabelById.get(activeId) ?? activeId;
      }
    };

    const onScroll = () => {
      syncProgress();
      syncActiveNav();
    };
    window.addEventListener("scroll", onScroll, { passive: true });
    window.addEventListener("resize", onScroll);
    onScroll();
  };

  const QUOTE_ORBIT_SLIDES = [
    {
      quote: "And ain't I a woman?",
      name: "Sojourner Truth",
      designation: "1851 · Akron convention",
      faceSrc: "assets/photos/portraits/sojourner-truth-1870.webp",
      faceAlt: "Sojourner Truth, c. 1870",
      credit: "Sojourner Truth, c. 1870. Wikimedia Commons, public domain.",
    },
    {
      quote: "I would rather drudge out my life on a cotton plantation, till the grave opened to give me rest, than to live with him without the rights of a wife.",
      name: "Harriet Jacobs",
      designation: "1861 · Incidents in the Life of a Slave Girl",
      faceSrc: "assets/photos/portraits/harriet-jacobs-gilbert-studios.webp",
      faceAlt: "Harriet Jacobs, Gilbert Studios portrait, 1894",
      credit: "Gilbert Studios, Washington, D.C., 1894. Wikimedia Commons, public domain.",
    },
    {
      quote: "The way to right wrongs is to turn the light of truth upon them.",
      name: "Ida B. Wells",
      designation: "1892 · Southern Horrors",
      faceSrc: "assets/photos/portraits/ida-b-wells-mary-garrity.webp",
      faceAlt: "Ida B. Wells-Barnett portrait by Mary Garrity",
      credit: "Mary Garrity, via Google Art Project. Wikimedia Commons, public domain.",
    },
    {
      quote: "My silences had not protected me. Your silence will not protect you.",
      name: "Audre Lorde",
      designation: "1980 · The Cancer Journals",
      faceSrc: "assets/photos/portraits/audre-lorde-1980.webp",
      faceAlt: "Audre Lorde, Austin, Texas, 1980",
      credit: "K. Kendall, 1980. Wikimedia Commons, CC BY 2.0.",
    },
    {
      quote: "I want a wake work that enacts an ethics of care as a practice of worrying the details and holding them close.",
      name: "Christina Sharpe",
      designation: "2016 · In the Wake",
      faceSrc: "assets/photos/portraits/christina-sharpe-york.webp",
      faceAlt: "Christina Sharpe, York University faculty portrait",
      credit: "Faculty profile photograph. York University, profiles.laps.yorku.ca/profiles/cesharpe/",
    },
  ];

  /**
   * One rAF-throttled scroll pass: hero portrait, visual-panel film layers, ground figures,
   * and a whisper of ambient depth. Skipped when prefers-reduced-motion.
   */
  const wireScrollParallax = () => {
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;

    const heroWrap = document.querySelector("#hero .hero-figure");
    const heroImg = heroWrap?.querySelector(".hero-photo");
    const films = $$(".section-visual-panel .section-bg-film");

    const clamp = (n, lo, hi) => Math.min(hi, Math.max(lo, n));
    let ticking = false;

    const update = () => {
      ticking = false;
      const H = window.innerHeight;
      const doc = document.documentElement;
      const maxScroll = Math.max(1, doc.scrollHeight - H);

      if (heroWrap && heroImg) {
        const r = heroWrap.getBoundingClientRect();
        if (r.bottom < -120 || r.top > H + 120) {
          heroImg.style.transform = "";
          heroImg.style.willChange = "auto";
        } else {
          const cy = r.top + r.height * 0.5;
          const norm = (cy - H * 0.5) / (H * 0.7);
          const ty = clamp(norm * -16, -14, 14);
          heroImg.style.willChange = "transform";
          heroImg.style.transform = `translate3d(0, ${ty.toFixed(2)}px, 0)`;
        }
      }

      films.forEach(film => {
        const panel = film.closest(".section-visual-panel");
        const r = panel?.getBoundingClientRect();
        if (!r || r.bottom < -160 || r.top > H + 160) {
          film.style.transform = "";
          film.style.willChange = "auto";
          return;
        }
        const cy = r.top + r.height * 0.5;
        const norm = (cy - H * 0.5) / H;
        const ty = clamp(norm * -48, -44, 44);
        film.style.willChange = "transform";
        film.style.transform = `translate3d(0, ${ty.toFixed(2)}px, 0)`;
      });

      $$("figure.ground-photo img").forEach(img => {
        const fig = img.closest("figure.ground-photo");
        const r = fig?.getBoundingClientRect();
        if (!r || r.bottom < -60 || r.top > H + 60) {
          img.style.transform = "";
          img.style.willChange = "auto";
          return;
        }
        const cy = r.top + r.height * 0.5;
        const norm = (cy - H * 0.5) / H;
        const ty = clamp(norm * -12, -10, 10);
        img.style.willChange = "transform";
        img.style.transform = `translate3d(0, ${ty.toFixed(2)}px, 0)`;
      });
    };

    const schedule = () => {
      if (!ticking) {
        ticking = true;
        requestAnimationFrame(update);
      }
    };

    window.addEventListener("scroll", schedule, { passive: true });
    window.addEventListener("resize", schedule, { passive: true });
    schedule();
  };

  const wireQuoteOrbit = () => {
    const root = document.getElementById("quote-orbit");
    const face = document.getElementById("quote-orbit-face");
    if (!root) return;

    const nameEl = document.getElementById("quote-orbit-name");
    const desigEl = document.getElementById("quote-orbit-designation");
    const quoteEl = document.getElementById("quote-orbit-quote");
    const creditEl = document.getElementById("quote-orbit-credit");
    const dotsEl = document.getElementById("quote-orbit-dots");
    const btnPrev = document.getElementById("quote-orbit-prev");
    const btnNext = document.getElementById("quote-orbit-next");
    if (!nameEl || !desigEl || !quoteEl || !dotsEl || !btnPrev || !btnNext) return;

    const n = QUOTE_ORBIT_SLIDES.length;
    let active = 0;
    const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    const autoplayOn = root.dataset.autoplay === "true" && !reduce;
    let timer = null;

    const clearTimer = () => {
      if (timer) {
        clearInterval(timer);
        timer = null;
      }
    };

    const startTimer = () => {
      clearTimer();
      if (!autoplayOn) return;
      timer = setInterval(() => {
        active = (active + 1) % n;
        render();
      }, 6500);
    };

    const render = () => {
      const s = QUOTE_ORBIT_SLIDES[active];
      nameEl.textContent = s.name;
      desigEl.textContent = s.designation;
      quoteEl.textContent = `“${s.quote}”`;
      if (creditEl) creditEl.textContent = s.credit || "";
      if (face && s.faceSrc) {
        face.src = s.faceSrc;
        face.alt = s.faceAlt || "";
      }
      dotsEl.querySelectorAll(".quote-orbit__dot").forEach((dot, i) => {
        const on = i === active;
        dot.classList.toggle("is-active", on);
        dot.setAttribute("aria-pressed", on ? "true" : "false");
      });
      root.setAttribute(
        "aria-label",
        `Voices from the record, slide ${active + 1} of ${n}: ${s.name}`
      );
    };

    dotsEl.innerHTML = "";
    QUOTE_ORBIT_SLIDES.forEach((_, i) => {
      const b = document.createElement("button");
      b.type = "button";
      b.className = "quote-orbit__dot";
      b.setAttribute("aria-label", `Show quotation ${i + 1}`);
      b.addEventListener("click", () => {
        active = i;
        clearTimer();
        render();
        startTimer();
      });
      dotsEl.appendChild(b);
    });

    const go = delta => {
      active = (active + delta + n) % n;
      clearTimer();
      render();
      startTimer();
    };

    btnPrev.addEventListener("click", () => go(-1));
    btnNext.addEventListener("click", () => go(1));

    root.addEventListener("keydown", e => {
      if (e.key === "ArrowLeft") {
        e.preventDefault();
        go(-1);
      } else if (e.key === "ArrowRight") {
        e.preventDefault();
        go(1);
      }
    });

    render();
    startTimer();
  };

  const loadCharts = async () => {
    const [lfp, ba, nacw] = await Promise.all([
      fetch("assets/data/lfp_black_women.json").then(r => r.json()),
      fetch("assets/data/ba_attainment_black_women.json").then(r => r.json()),
      fetch("assets/data/nacw_clubs.json").then(r => r.json()),
    ]);

    const heroCanvas = document.getElementById("chart-hero");
    if (heroCanvas && typeof Chart !== "undefined") {
      const pts = lfp.years.map((y, i) => ({ x: Number(y), y: lfp.values[i] }));
      const ds = [
        {
          label: "Labor force participation (%)",
          data: pts,
          fill: true,
          tension: 0.25,
          paletteKey: "chart-lfp",
          colorAlpha: "",
          backgroundAlpha: "28",
          borderWidth: 2,
          pointRadius: 3,
          pointBackgroundColor: palette()["chart-lfp"],
        },
      ];
      const chart = makeLineChart(heroCanvas, {
        datasets: ds,
        yTitle: "Percent",
        xTitle: "Year",
        xMin: 1875,
        xMax: 2025,
        annotations: [
          { type: "marker", x: 1881, label: "1881", dy: 0 },
          { type: "marker", x: 1896, label: "1896", dy: 12 },
          { type: "marker", x: 1965, label: "1965", dy: 0 },
          { type: "marker", x: 1980, label: "1980", dy: 12 },
        ],
      });
      applyPaletteToChart(chart);
    }

    const nacwCanvas = document.getElementById("chart-nacw");
    if (nacwCanvas && typeof Chart !== "undefined") {
      const pts = nacw.years.map((y, i) => ({ x: Number(y), y: nacw.values[i] }));
      const chart = makeBarChart(nacwCanvas, {
        datasets: [
          {
            label: "Estimated affiliated clubs",
            data: pts,
            maxBarThickness: 36,
            paletteKey: "chart-nacw",
            colorAlpha: "",
            backgroundAlpha: "55",
            borderWidth: 1,
          },
        ],
        yTitle: "Clubs (approx.)",
        xTitle: "Year",
        xMin: 1894,
        xMax: 1926,
        annotations: [{ type: "marker", x: 1896, label: "1896 founding" }],
      });
      applyPaletteToChart(chart);
    }

    const baCanvas = document.getElementById("chart-ba");
    if (baCanvas && typeof Chart !== "undefined") {
      const pts = ba.years.map((y, i) => ({ x: Number(y), y: ba.values[i] }));
      const chart = makeLineChart(baCanvas, {
        datasets: [
          {
            label: "BA or higher (%)",
            data: pts,
            fill: true,
            tension: 0.25,
            paletteKey: "chart-ba",
            colorAlpha: "",
            backgroundAlpha: "28",
            borderWidth: 2,
            pointRadius: 3,
            pointBackgroundColor: palette()["chart-ba"],
          },
        ],
        yTitle: "Percent",
        xTitle: "Year",
        xMin: 1940,
        xMax: 2022,
        annotations: [
          { type: "marker", x: 1954, label: "Brown v. Board" },
          { type: "marker", x: 1972, label: "Title IX" },
          { type: "marker", x: 2014, label: "2014 ACS era" },
        ],
      });
      applyPaletteToChart(chart);
    }
  };

  const boot = async () => {
    renderTimeline();
    wireTimelineAutoscroll();
    wireTOC();
    wireScrollParallax();
    wireQuoteOrbit();
    try {
      await loadCharts();
    } catch (e) {
      console.error(e);
    }
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot, { once: true });
  } else {
    boot();
  }
})();
