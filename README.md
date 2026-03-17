# CC2.2: Text Preprocessing -- Phase 1: Start and Run

[![Python 3.14+](https://img.shields.io/badge/python-3.14%2B-blue?logo=python)](#)
[![MIT](https://img.shields.io/badge/license-see%20LICENSE-yellow.svg)](./LICENSE)

Professional Python project for Web Mining and Applied NLP.

## Example Output Artifact

![Word Cloud Example](docs/images/word_cloud_example.png)

## Assignment Updates

## Assignment Goal

Set up the project, run the example text preprocessing pipeline, review the code, and submit your updated work.

## Project Scope

- Notebook exploration: notebooks/text_preprocessing_case.ipynb
- Python module: src/nlp/text_preprocessing_case.py
- Project metadata: pyproject.toml and zensical.toml
- Input data: data/text_data_case.txt

## Steps to Complete the Assignment

1. Clone your repository and open it in VS Code.
2. Set up the environment and dependencies with uv.
3. Install pre-commit hooks and run checks.
4. Run the example module.
5. Open the notebook, select the kernel, and run all cells.
6. Update authorship and repository metadata.
7. Make one technical modification and verify it still runs.
8. Commit and push your changes.

## Commands

Run from the project root.

```shell
uv self update
uv python pin 3.14
uv sync --extra dev --extra docs --upgrade

uvx pre-commit install
git add -A
uvx pre-commit run --all-files

uv run python -m nlp.text_preprocessing_case

uv run ruff format .
uv run ruff check . --fix
uv run zensical build

git add -A
git commit -m "complete assignment"
git push -u origin main
```

## Completion Checklist

- Pipeline runs successfully.
- Notebook runs end-to-end.
- Metadata is updated with your information.
- Pre-commit checks pass.
- Changes are pushed to GitHub.


# CC2.2: Text Preprocessing -- Phase 2: Change Authorship

## Authorship Updates

✅ **Authorship Updated Across All Files:**

- [zensical.toml](zensical.toml) — Site, repo, and social links point to Angie-Crews
- [LICENSE](LICENSE) — Added Angie Crews as copyright holder
- [CITATION.cff](CITATION.cff) — Angie Crews listed as primary author
- [notebooks/text_preprocessing_case.ipynb](notebooks/text_preprocessing_case.ipynb) — Author and repo links updated
- GitHub About section — Linked to your GitHub Pages site
