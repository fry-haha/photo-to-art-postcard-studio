# Contributing

Photo To Art Postcard Studio is in visual and physical-prototype development. Small, focused contributions are welcome when they improve repeatability without flattening every photograph into the same template.

## Before opening a change

- Describe the visual or production failure the change addresses.
- Preserve photographic identity, protected subjects, and front/back pairing.
- Do not add invented dates, lyrics, coordinates, or decorative metadata.
- Keep reference-derived ideas at the level of principles; do not copy a distinctive composition.
- Do not add source photographs or third-party assets without clear redistribution rights and attribution.
- Keep public-facing examples separate from print-production files.

## Skill changes

Keep shared rules concise in `SKILL.md`. Put substantial conditional guidance in the relevant file under `references/`, and avoid duplicating the same rule across files.

Validate the Skill after editing:

```bash
python /path/to/skill-creator/scripts/quick_validate.py .
```

## Python utilities

Install dependencies with:

```bash
python -m pip install -r requirements.txt
```

Run a script with `--help`, test it on a disposable copy, and avoid hard-coded user paths or private assets. New utilities should be deterministic and should not silently overwrite their inputs.

## Licensing

By contributing, you agree that contributions to Skill instructions, references, and scripts are provided under the repository's PolyForm Noncommercial 1.0.0 terms. Do not contribute material you do not have permission to share.
