#!/usr/bin/env python3
"""
Script to generate the resume from YAML using Jinja2
This script creates filled/resume_miranda.tex from raw/resume_miranda.tex and resume_miranda.yaml
"""
import os
import yaml
from jinja2 import Environment, FileSystemLoader

def load_yaml(filepath):
    """Load YAML file and convert jobs data to list format for Jinja2"""
    with open(filepath, 'r') as f:
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
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template(os.path.basename(template_path))
    return template.render(**data)

def main():
    data = load_yaml('resume_miranda.yaml')
    rendered = render_template('raw/resume_miranda.tex', data)

    os.makedirs('filled', exist_ok=True)
    with open('filled/resume_miranda.tex', 'w') as f:
        f.write(rendered)
    print("Successfully generated filled/resume_miranda.tex")

if __name__ == "__main__":
    main()
