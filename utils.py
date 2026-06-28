#!/usr/bin/env python3
"""
Script to generate the resume from YAML using Jinja2
This script creates filled/resume_miranda.tex from raw/resume_miranda.tex and resume_miranda.yaml
"""
from pathlib import Path
import os
import yaml
from jinja2 import Environment, FileSystemLoader

def load_yaml(filepath):
    """Load YAML file and convert jobs data to list format for Jinja2"""
    with open(filepath, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)

    selected_sections = {'jobs', 'education'}  #, 'publications', 'projects', etc
    selected_sections = selected_sections.intersection(data.keys())
    for section in selected_sections:
        subsections = []
        for subsection_key in sorted(data[section].keys(), key=lambda x: int(x)):
            subsection = data[section][subsection_key].copy()
            if 'items' in subsection:
                subsection['items'] = list(subsection['items'].values())
            else:
                subsection['items'] = []
            subsections.append(subsection)
        data[section] = subsections

    return data

def render_template(template_path, data):
    """Render Jinja2 template with the given data"""
    template_dir = os.path.dirname(template_path)
    env = Environment(
        loader=FileSystemLoader(template_dir),
        autoescape=False,  # Important: don't escape LaTeX
    )
    template = env.get_template(os.path.basename(template_path))
    return template.render(**data)

def main():

    #filename_resume = 'resume_miranda.yaml'
    #filename_template = 'raw/resume_miranda.tex'
    #filename_filled = 'filled/resume_miranda.tex'

    filename_layout = 'layout_en.yml'
    filename_resume = 'resume_en.yaml'
    filename = 'resume.tex'
    filename_template = Path('clean', filename)  # TODO: clean from raw template
    filename_filled = Path('filled', filename)

    # Clean template
    # TODO

    # load layout data, no preprocessing
    #data_layout = {}  # for resume_miranda.yaml
    with open(filename_layout, 'r', encoding='utf-8') as f:
        data_layout = yaml.safe_load(f)

    # load resume data, preprocessing selected sections
    data_resume = load_yaml(filename_resume)

    # join all data
    data = {**data_layout, **data_resume}

    # fill template with data
    rendered = render_template(filename_template, data)

    #os.makedirs('filled', exist_ok=True)
    with open(filename_filled, 'w', encoding="utf-8") as f:
        f.write(rendered)
    print(f"Successfully generated {filename_filled}")

    # TODO: remove whitespaces in curly braces
if __name__ == "__main__":
    main()
