# Production and packaging

## Default assumptions

Confirm the printer's specification when the work is intended for manufacture. Until confirmed, treat the following as a working baseline rather than a universal printer requirement.

- Postcard: A6, 105 × 148 mm.
- Bleed: 3 mm on all sides.
- Safe area: keep critical content at least 4 mm inside trim.
- Raster resolution: 300 ppi at final physical size.
- Color: retain an RGB working master; convert/export to the printer's requested profile for production.
- Text: keep editable until final approval; outline or embed only in the production copy.

## Sticker baseline

- Keep individual stickers on transparent backgrounds.
- Produce white-border and pure-cutout variants when feasible.
- Keep manufacturing contour separate from artwork whenever the production format supports it.
- Confirm minimum sticker size, white-border width, bleed, and contour spacing with the chosen printer.
- Do not bake preview shadows into production art.

## Deliverable tree

```text
project-name/
├── 01-preview/
├── 02-postcard/
│   ├── front/
│   └── back/
├── 03-sticker-sheet/
├── 04-individual-stickers/
│   ├── white-border/
│   └── pure-cutout/
├── 05-print/
└── 06-source-notes/
```

Use versioned names such as `project_postcard-front_v01` and never overwrite an approved version.

## Presentation versus production

Presentation may include surface, soft shadow, external mockup tape, overlap, lifted edges, and product photography. Production must be flat, clean, correctly sized, and free of fake lighting or perspective. If tape or a banded material is part of the approved artwork rather than the mockup scene, retain the flat material layer in production and remove only its staging shadow, perspective, and environmental lighting.
