# Vitalic

> "Vitalic" kinda resembles "Vitae", right?... Anyway

Generate a stylish and professional _curriculum_ _vitae_ (resume) from fields in a YAML (or Markdown, not yet implemented) file. Page layout (margins, font size, etc) can be easily adjusted to account for more/less text and variying section sizes.

## Requirements

- Python, built with version 3.13.
- `xelatex`, included in standard TeX distributions like MiKTeX.

## Usage

- Clone repository and run `uv sync`.
- Substitute for your own info in `resume_en.yaml`.
- Run `uv run utils.py` to generate final `filled/resume.tex`.
- In `filled` folder, run `xelatex resume.tex` to generate your `resume.pdf`
- Optionally, adjust values in `layout_en.yaml` and repeat last two steps.

<!--
- Generate PDF by running `generate.sh`.
- Optional (adjust layout yaml and repeat
-->

## Status

✅ Read some sections from YAML to simple clean template

✅ Read some sections from YAML to stylish clean template

✅ Clean raw template

✅ Read some sections from YAML to stylish raw template

✅ Read all sections from YAML to stylish raw template

✅ Fix whitespaces in curly braces

✅ Add logic for photo

⬜ Add logic for extra sections

⬜ Pass layout and resume info filenames as optional parameters

⬜ Add metadata info

⬜ Read from YAML or markdown

⬜ Add bash script

⬜ Add PDF analysis


