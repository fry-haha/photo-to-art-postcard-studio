# Photo To Art Postcard Studio

**Turn a personal photograph into a collectible art postcard with a designed front, a functional matching back, and source-aware color and material decisions.**

[![Version](https://img.shields.io/badge/version-0.1.0-334155)](VERSION)
[![Codex Skill](https://img.shields.io/badge/Codex-Skill-111827)](SKILL.md)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](requirements.txt)
[![License](https://img.shields.io/badge/license-PolyForm%20Noncommercial-7C3AED)](LICENSE.md)

Photo To Art Postcard Studio is a Codex Skill for turning real photographs into finished front-and-back postcard systems. It reads the photograph before styling it, protects faces and landmarks, chooses orientation from the subject, derives the back-side palette from the source, and uses tape or banded materials only when they perform a real compositional task.

中文简介：它不是给照片套一个固定明信片模板，而是先识别主体、不可裁切区域、自然横竖比例、颜色和材质，再生成一张有完整正面与背面的收藏型艺术明信片。

## Samples

| Coastal | Historical art space |
|---|---|
| ![Coastal front and back](samples/social/01-coastal-front-back-sample.png) | ![Historical gallery front and back](samples/social/02-historical-gallery-front-back-sample.png) |

| Music / vinyl | Lake |
|---|---|
| ![Vinyl front and back](samples/social/03-vinyl-front-back-sample.png) | ![Lake front and back](samples/social/04-lake-front-back-sample.png) |

| Architecture | Portrait |
|---|---|
| ![Architecture front and back](samples/social/05-architecture-front-back-sample.png) | ![Portrait front and back](samples/social/06-portrait-front-back-sample.png) |

## What it does

- preserves the recognizable identity of the source photograph;
- protects complete faces, landmarks, horizons, and other meaningful structures before cropping;
- selects horizontal or vertical composition from the subject instead of forcing one template;
- creates a matching postcard back for every approved front;
- derives the back-side hero color from water, sky, architecture, clothing, light, or another meaningful source region;
- abstracts useful source elements instead of repeating the same photograph as decorative thumbnails;
- supports three confirmed art directions: **Photo + Oil Fusion**, **Artist Travel Archive**, and **Museum Art Collection**;
- treats paper tape, washi, ribbon, fabric, vellum, acetate, and transparent film as different materials with different spatial roles;
- keeps postal function, writing space, print safety, and production files separate from social presentation mockups.

## Install in Codex

Open this repository, copy its URL, and ask Codex:

```text
Please use $skill-installer to install the skill from https://github.com/fry-haha/photo-to-art-postcard-studio.
```

中文安装提示词：

```text
请使用 $skill-installer，从 https://github.com/fry-haha/photo-to-art-postcard-studio 安装这个 Skill。
```

After installation, upload a photograph and invoke the Skill:

```text
Use $photo-to-merch-studio to turn this photograph into a collectible art postcard with a matching back.
```

中文最简用法：上传照片后说：

```text
使用 $photo-to-merch-studio，把这张照片做成一张有完整正反面的收藏型艺术明信片。
```

## The decision system

The Skill separates four decisions that generic postcard templates usually collapse:

1. **Subject protection** — identify what must remain complete and recognizable.
2. **Composition intelligence** — choose crop, orientation, scale, negative space, and depth from the photograph.
3. **Front/back continuity** — translate the front's color, material, line, and meaningful visual elements into a functional back.
4. **Material logic** — use tape and banded materials only to attach, connect, bridge, mask, cross an edge, or extend a real movement.

The source photograph is reference input, never a fourth style. For a three-direction test, the outputs are exactly D1, D2, and D3.

## Repository structure

```text
.
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── artistic-directions.md
│   ├── crop-and-frame-library.md
│   ├── postcard-back-systems-research.md
│   ├── production.md
│   ├── qa.md
│   ├── type-layouts.md
│   └── visual-system.md
├── scripts/
│   ├── add_tape_overlay.py
│   ├── check_raster.py
│   ├── extract_element.py
│   └── make_postcard_gallery.py
├── samples/social/
│   └── six front-and-back presentation samples
├── PHYSICAL-PRODUCT-PLAN.md
├── requirements.txt
└── VERSION
```

The installable Skill instructions, references, UI metadata, and reusable utilities live in the repository. Public samples demonstrate decisions; source photographs are not redistributed as a reusable stock-photo library.

## Optional Python utilities

The utilities are deterministic helpers for raster checks, contact-sheet construction, element extraction, and presentation-only tape studies. They do not replace the Skill's visual judgment.

```bash
python -m pip install -r requirements.txt
python scripts/check_raster.py input.png --width-mm 148 --height-mm 100 --ppi 300
```

Use `--help` on any script for its arguments. Generated artwork and source rights still require human review.

## Physical production status

The visual system is validated. Paper stock, duplex mounting, color proofing, emboss/deboss, raised varnish, and packaging remain prototype decisions. See [PHYSICAL-PRODUCT-PLAN.md](PHYSICAL-PRODUCT-PLAN.md); do not treat exploratory manufacturing notes as a final printer specification.

## Originality and responsible use

The system may learn high-level principles such as hierarchy, negative space, paper texture, asymmetry, archival typography, and material interaction. It must not copy a reference's exact composition, wording, color placement, or distinctive arrangement.

Review source-photo rights, likenesses, readable text, print proofs, and platform disclosure requirements before publishing or manufacturing. Examples may contain AI-generated or AI-edited image content.

## License

- Skill instructions, references, and scripts: [PolyForm Noncommercial License 1.0.0](LICENSE.md)
- Original example and visual assets: [CC BY-NC-SA 4.0](ASSETS_LICENSE.md), except third-party source material
- Commercial use: [separate permission is required](COMMERCIAL_USE.md)
- Project name and identity: see [PROJECT_IDENTITY.md](PROJECT_IDENTITY.md)
