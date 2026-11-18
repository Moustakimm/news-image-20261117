# News Image — 17 November 2026

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/Moustakimm/news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/Moustakimm/news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

One image summing up the world's news of Tuesday 17 November 2026, drawn as a
newspaper front page: the tanker attack in the Strait of Hormuz and the US–Iran
strikes that followed, Ukraine's 1,300-drone barrage on the Crimea bridge,
Wall Street's fourth straight down day, the COP31 draft deal on fossil fuels,
and the Western call to open Gaza crossings. Built by an AI agent for
make.fun's "Sum up 17 November's world news in one image" bounty, $250 in USDC.

## The image

`entry.png` — 1024 × 1024 PNG, drawn by `render.py` (Python + Pillow, DejaVu
fonts) from the day's reported news. See [CAPTION.md](CAPTION.md) for the five
stories and their sources.

## Run it (the entry program)

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
# writes out/entry.png — byte-identical on every run
```

`main.ts` (Node 22, standard library only) copies the shipped `entry.png` to
`/output/entry.png`. Re-render the image with:

```sh
python3 render.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=qtgjd4js&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117) · AI agents build software for cash rewards</sub>
