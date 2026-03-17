# ML Project Template

A production-ready Cookiecutter template for ML/AI projects.

Includes:

* Dependency management with Poetry
* Workflow orchestration scaffold with Metaflow (optional)
* Experiment tracking scaffold with MLflow (optional)
* Streamlit dashboard scaffold (optional)
* Pre-commit hooks (Black + Ruff + YAML checks)
* GitHub Actions CI
* Makefile for standard commands
* Minimal runnable scaffolds for flows, experiments, and dashboards

---

## Features

* Reproducible, isolated Python environment with Poetry

* Pre-configured project structure:

  ```
  {{cookiecutter.project_slug}}/  
      pyproject.toml  
      Makefile  
      .pre-commit-config.yaml  
      README.md  
      .env.example  
      src/  
          __init__.py  
          config.py  
          experiment.py  
      flows/main_flow.py  
      dashboard/app.py  
      .github/workflows/ci.yml  
  ```

* Quick scaffolding of new ML projects using Cookiecutter

* Experiment tracking with MLflow

* Pipeline orchestration with Metaflow

* Optional dashboard with Streamlit + Plotly

* Built-in code formatting and linting with pre-commit hooks

* CI testing ready for GitHub Actions

---

## Getting Started

1. **Install Cookiecutter** (if not already):

   ```
   pip install cookiecutter
   ```

2. **Generate a new ML project**:

   Clone this repo into your project directory. Then initialise the new project using:

   ```
   cookiecutter ./ml-project-template
   ```

   You will be prompted for:

   * project_name: Human-friendly project name
   * project_slug: Folder name / Python module name
   * author_name: Your name
   * python_version: e.g., 3.11
   * use_metaflow: yes/no
   * use_streamlit: yes/no
   * use_mlflow: yes/no
   * license: MIT or other

3. **Initialize the generated project**:

   ```
   cd <your_project_slug>
   poetry install
   poetry run pre-commit install
   ```

4. **Run project commands**:

   * Run Python module:

     ```
     make run
     ```

   * Run Metaflow pipeline:

     ```
     make flow
     ```

   * Run Streamlit dashboard:

     ```
     make dashboard
     ```

   * Run MLflow experiment scaffold:

     ```
     make experiment
     ```

   * Run tests:

     ```
     make test
     ```

   * Format and lint code:

     ```
     make format
     ```

---

## Project Structure

* `src/{{cookiecutter.project_slug}}/` → main Python package
* `flows/` → Metaflow pipelines
* `dashboard/` → Streamlit app
* `.pre-commit-config.yaml` → pre-commit hooks
* `.github/workflows/` → CI with GitHub Actions
* `Makefile` → unified commands for development workflow
* `.env.example` → example environment variables

---

## Philosophy

* Minimal but runnable: scaffold can run immediately after generation
* Extensible: easily add your own flows, dashboards, and ML logic
* Reproducible: each project uses isolated Poetry environment
* Production-friendly: includes CI, pre-commit hooks, experiment tracking

---

## Quick Tips

* To add a new ML project using this template:

  ```
   cookiecutter gh:your-username/ml-project-template
  ```

* To push a generated project to GitHub quickly:

  ```
   cd <your_project_slug>
   git init
   git add .
   git commit -m "Initial commit"
   gh repo create <repo-name> --public --source=. --remote=origin --push
  ```

* To view MLflow dashboard:

  ```
   mlflow ui
  ```

* Pre-commit hooks automatically run on commit for formatting and linting.

---

## License

{{cookiecutter.license}}

---

