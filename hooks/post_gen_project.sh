#!/bin/bash
echo -e "Project created in ./{{cookiecutter.project_slug}}!"
{% if cookiecutter.start_development_environment_after_creation == 'Yes' -%}
echo -e "Starting development environment..."
make start{% endif %}
