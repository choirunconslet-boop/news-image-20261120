# news-image-20261120

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/choirunconslet-boop/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/choirunconslet-boop/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

One image summing up the world's news of Friday 20 November 2026,
built for the make.fun bounty `news-image-20261120`.

## The image

A newspaper front page, "THE WORLD", with nine stories:

1. **Lead — Shenzhen:** Trump, Putin and Xi sign a four-point
   "peace declaration" after their historic trilateral summit.
2. **Kyiv under fire:** Russia's overnight missile and drone attack
   hits three Kyiv bridges; three killed, nine hurt.
3. **Markets:** Anthropic closes its first day up 17% after the
   record $81.3 billion IPO; the Dow dips below 50,000.
4. **Drones for Kyiv:** Britain pledges 1,000 long-range drones in
   a £260 million package; nearly 40 partners back Kyiv.
5. **Also on 20 Nov:** Poland lifts its air-threat warning, the EU
   summons Russia's envoy, Trump pardons Pete Rose, Israel's Gaza
   operation, Houthi drones and the tanker fire, and the COP31 draft.

Every story was verified against live reporting dated 20 November
2026 — see SOURCES.md.

## Files

- `entry.png` — the finished front page (1024x1024, PNG).
- `main.ts` — the entry program (Node 22, standard library only):
  copies `entry.png` to `/output/entry.png`. Deterministic: the same
  bytes every run, no network.
- `render_frontpage.py` — the script that drew the front page with
  Pillow (skyline art, headlines, columns). Re-run it to rebuild
  `entry.png`: `python3 render_frontpage.py entry.png`.
- `SOURCES.md` — where every fact came from, and the dating care taken.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts   # writes out/entry.png
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=j32a98da&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>

License: MIT.
