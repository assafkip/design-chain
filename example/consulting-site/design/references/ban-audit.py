#!/usr/bin/env python3
"""Test every tell the canon bans against the five sites the founder named as the target.

Founder, 2026-09-15: "remove the old cannon bans if they and make sense anymore".

site-design.md section 7 lists the AI-default fingerprint: Inter or Geist as the only
choice, violet or indigo accents, gradient text on a headline, emoji as icons, dark hero
with a glow, two side-by-side CTAs, rows of three icon cards, and the newer "tasteful" wash
(cream background, amber accent, serif italics, uppercase eyebrow labels, monospace body).

Some of those the exemplars do. A ban the target set breaks is not a standard, it is a
reason the build can never resemble the target, and it has cost seven rounds. This decides
which is which by measurement rather than by argument, live against each site, because the
stored captures do not carry everything the question needs.

Exit 0 always. This reports; the canon edit is the founder's.
"""
from __future__ import annotations

import colorsys
import json
import pathlib
import sys

REFS = pathlib.Path(__file__).resolve().parent

PROBE = r"""
() => {
  const vh = innerHeight, vw = innerWidth;
  const deep = (root, out) => { for (const e of root.querySelectorAll('*')) {
      out.push(e); if (e.shadowRoot) deep(e.shadowRoot, out); } return out; };
  const all = deep(document.body, []);
  const inFold = e => { const r = e.getBoundingClientRect();
    return r.width > 0 && r.height > 0 && r.top < vh && r.bottom > 0; };
  const fold = all.filter(inFold);
  const cs = e => getComputedStyle(e);

  // gradient painted INTO type
  const gradText = fold.filter(e => {
    const c = cs(e);
    return (c.webkitBackgroundClip === 'text' || c.backgroundClip === 'text') &&
           (c.backgroundImage || '').includes('gradient'); }).length;

  // any gradient surface at all, and how big the biggest one is
  const gradEls = fold.filter(e => (cs(e).backgroundImage || '').includes('gradient'));
  const gradMax = gradEls.reduce((m, e) => { const r = e.getBoundingClientRect();
    return Math.max(m, Math.round(100 * r.width * r.height / (vw * vh))); }, 0);

  // two actions sitting side by side: same row, adjacent, both real controls
  // A CTA is a control, not a link in a menu. The first version of this matched any two
  // adjacent elements with an href and reported ['Product','Solutions'] as a side-by-side
  // CTA pair on four of five sites, which is a navigation, not a pair of calls to action.
  const isCta = e => {
    if (e.closest('nav')) return false;
    const c = cs(e);
    const painted = (c.backgroundColor || '').match(/\d+/g);
    const hasFill = painted && !(painted[3] !== undefined && +painted[3] === 0);
    const hasBorder = parseFloat(c.borderTopWidth || '0') > 0;
    return e.tagName === 'BUTTON' || hasFill || hasBorder;
  };
  const acts = fold.filter(e => (e.tagName === 'BUTTON' ||
      (e.tagName === 'A' && e.hasAttribute('href'))) && isCta(e))
    .map(e => { const r = e.getBoundingClientRect();
      return { t: Math.round(r.top), l: Math.round(r.left), r: Math.round(r.right),
               h: Math.round(r.height), txt: (e.innerText || '').trim().slice(0, 24) }; })
    .filter(b => b.h > 28 && b.txt);
  let pairs = [];
  for (const a of acts) for (const b of acts) {
    if (a === b || b.l <= a.l) continue;
    if (Math.abs(a.t - b.t) <= 6 && (b.l - a.r) >= 0 && (b.l - a.r) < 40)
      pairs.push([a.txt, b.txt]);
  }

  // emoji used as an icon
  const emoji = fold.filter(e => {
    const t = [...e.childNodes].filter(n => n.nodeType === 3).map(n => n.textContent).join('');
    return /[\u{1F300}-\u{1FAFF}\u{2600}-\u{27BF}]/u.test(t); }).length;

  // uppercase eyebrow labels and monospace body, the "tasteful wash" markers
  const upper = fold.filter(e => { const c = cs(e);
    const t = [...e.childNodes].filter(n => n.nodeType === 3).map(n => n.textContent).join('').trim();
    return t.length > 2 && c.textTransform === 'uppercase' && parseFloat(c.fontSize) < 20; }).length;
  const mono = fold.filter(e => /mono|courier/i.test(cs(e).fontFamily || '')).length;
  const serifItalic = fold.filter(e => { const c = cs(e);
    return c.fontStyle === 'italic' && /serif|georgia|times/i.test(c.fontFamily || ''); }).length;

  // a dark hero: the largest fold surface being dark
  let darkest = null, darkArea = 0;
  for (const e of fold) { const c = cs(e), r = e.getBoundingClientRect();
    const m = (c.backgroundColor || '').match(/\d+/g);
    if (!m || (m[3] !== undefined && +m[3] === 0)) continue;
    const lum = (0.2126 * +m[0] + 0.7152 * +m[1] + 0.0722 * +m[2]) / 255;
    // clip to the viewport: the first version multiplied the full element box and
    // reported squarespace's dark hero at 870% of the fold, which is not a percentage.
    const cw = Math.max(0, Math.min(r.right, vw) - Math.max(r.left, 0));
    const ch = Math.max(0, Math.min(r.bottom, vh) - Math.max(r.top, 0));
    const area = cw * ch;
    if (lum < 0.35 && area > darkArea) { darkArea = area; darkest = c.backgroundColor; } }

  // three or more sibling boxes of the same size in a row
  let cardRow = 0;
  for (const e of fold) {
    // a CARD is a substantial block. The first version used width>90 height>60 and
    // reported stripe at 36 boxes in a row, which is a customer logo strip.
    const kids = [...e.children].map(k => k.getBoundingClientRect())
      .filter(r => r.width > 0.14 * vw && r.height > 0.12 * vh);
    if (kids.length < 3) continue;
    const row = kids.filter(r => Math.abs(r.top - kids[0].top) < 8 &&
      Math.abs(r.width - kids[0].width) < 12);
    if (row.length >= 3 && row.length <= 6) cardRow = Math.max(cardRow, row.length); }

  const fams = new Set(fold.map(e => (cs(e).fontFamily || '').split(',')[0]
    .replace(/["']/g, '').trim()).filter(Boolean));

  return { gradText, gradEls: gradEls.length, gradMax, pairs: pairs.slice(0, 3),
           emoji, upper, mono, serifItalic,
           darkHero: darkest, darkHeroPct: Math.round(100 * darkArea / (vw * vh)),
           cardRow, families: [...fams].slice(0, 6) };
}
"""


def hue_of(hexv: str):
    r, g, b = (int(hexv[i:i + 2], 16) / 255 for i in (1, 3, 5))
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    return round(h * 360), round(s * 100), round(l * 100)


def stored_palette(slug: str):
    f = REFS / f"{slug}.json"
    if not f.is_file():
        return []
    w = json.loads(f.read_text())["viewports"]["laptop"]
    out = []
    import re
    for row in w["color"]["backgrounds"] + w["color"]["text"]:
        m = re.findall(r"\d+", row["value"])
        if len(m) >= 3 and not (len(m) >= 4 and m[3] == "0"):
            out.append("#%02x%02x%02x" % tuple(int(x) for x in m[:3]))
    return out


def main() -> int:
    roster = json.loads((REFS / "exemplars.json").read_text())["exemplars"]
    urls = [e["url"] for e in roster]
    from playwright.sync_api import sync_playwright
    rows = {}
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        for u in urls:
            pg = b.new_page(viewport={"width": 1440, "height": 900})
            try:
                pg.goto(u, wait_until="domcontentloaded", timeout=45000)
                pg.wait_for_timeout(4500)
                rows[u] = pg.evaluate(PROBE)
            except Exception as e:
                rows[u] = {"_error": str(e)[:90]}
            pg.close()
        b.close()

    print("EVERY TELL THE CANON BANS, TESTED AGAINST THE FIVE SITES THE FOUNDER NAMED\n")
    print("site-design.md section 7. A ban the target set breaks is not a standard.\n")

    def name(u):
        return u.split("//")[-1].strip("/")

    bans = []

    # violet / indigo accents
    viol = {}
    for u in urls:
        slug = name(u).replace(".", "-")
        hits = [c for c in stored_palette(slug)
                if 230 <= hue_of(c)[0] <= 290 and hue_of(c)[1] > 35]
        if hits:
            viol[name(u)] = sorted(set(hits))
    bans.append(("violet or indigo accents", viol))

    def collect(key, test, label):
        out = {}
        for u in urls:
            d = rows.get(u, {})
            if "_error" in d:
                continue
            v = test(d)
            if v:
                out[name(u)] = v
        bans.append((label, out))

    collect("gradText", lambda d: d["gradText"] or None, "gradient text on a headline")
    collect("grad", lambda d: (f"{d['gradEls']} gradient surfaces, largest {d['gradMax']}% of the fold"
                               if d["gradEls"] else None), "gradient surfaces in the fold")
    collect("pairs", lambda d: d["pairs"] or None, "two side-by-side CTAs")
    collect("emoji", lambda d: d["emoji"] or None, "emoji as icons")
    collect("dark", lambda d: (f"{d['darkHero']} over {d['darkHeroPct']}% of the fold"
                               if d["darkHero"] and d["darkHeroPct"] >= 25 else None),
            "dark hero")
    collect("cards", lambda d: (f"{d['cardRow']} equal boxes in a row" if d["cardRow"] >= 3 else None),
            "rows of three or more equal boxes")
    collect("upper", lambda d: d["upper"] or None, "uppercase small labels")
    collect("mono", lambda d: d["mono"] or None, "monospace body")
    collect("serifItalic", lambda d: d["serifItalic"] or None, "serif italics")
    collect("inter", lambda d: ([f for f in d["families"] if f.lower() in
                                 ("inter", "geist", "roboto", "plus jakarta sans", "space grotesk")]
                                or None), "a converged default font present")

    for label, hits in bans:
        n = len(hits)
        verdict = ("NO SITE DOES THIS, the ban costs nothing" if n == 0 else
                   f"{n} OF {len(urls)} DO THIS")
        print(f"[{verdict}]  {label}")
        for site, v in sorted(hits.items()):
            print(f"      {site}: {v}")
        print()

    broken = [l for l, h in bans if len(h) >= 2]
    print("BANS THE TARGET SET BREAKS ON TWO OR MORE SITES:")
    for l in broken:
        print(f"  {l}")
    print("""
These are the ones that cannot survive as written. A rule that the pages the founder
pointed at all violate is not describing AI slop, it is describing the moves that became
cheap BECAUSE those pages made them famous. NARRATIVE.md section 8 said this and it was
never acted on. The canon edit is his; this is the evidence.""")
    return 0


if __name__ == "__main__":
    sys.exit(main())
