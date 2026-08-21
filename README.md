# Vitalic

Generate a stylish and professional _curriculum_ _vitae_ (resume) from fields in a YAML (or Markdown, not yet implemented) file. Page layout (margins, font size, etc) can be easily adjusted to account for more/less text and variying section sizes.

Take a look at the generated document [example](filled/resume.pdf)!

## Requirements

- Python, built with version 3.13.
- `xelatex`, included in standard TeX distributions like MiKTeX.
- Roboto Light font: optional, available at https://fonts.google.com/specimen/Roboto

## Usage

- Clone repository and run `uv sync`.
- Substitute for your own info in `resume_en.yaml`.
- Run `uv run utils.py` to generate final `filled/resume.tex`.
- In `filled` folder, run `xelatex resume.tex` to generate your `resume.pdf`
- Optionally, adjust values in `layout_en.yaml` and repeat last two steps.

<!--
wsl vitalic.sh
wsl bash -c "vitalic.sh argument1"
-->

<!--
- Generate PDF by running `generate.sh`.
- Optional (adjust layout yaml and repeat
-->

## Status

✅ Read all sections from YAML to raw template

✅ Fix whitespaces in curly braces

✅ Add logic for photo

⬜ Add extra sections with logic

⬜ Add metadata info with logic

⬜ Pass layout and resume info filenames as optional parameters

⬜ Add bash script to run full pipeline

⬜ Read from YAML **or markdown**

⬜ Add PDF analysis


<!--
## Backlog

- Add fields to layout YAML (e.g. metadata)

https://tex.stackexchange.com/questions/26529/how-can-i-generate-pdf-metadata-from-latex
-->
