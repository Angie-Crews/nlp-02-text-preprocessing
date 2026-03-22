# P2 Text Preprocessing: Chocolate Deep-Dive

[![Python 3.14+](https://img.shields.io/badge/python-3.14%2B-blue?logo=python)](#)
[![MIT](https://img.shields.io/badge/license-see%20LICENSE-yellow.svg)](LICENSE)

This project demonstrates practical text preprocessing for applied NLP.

Phase 4 introduced a chocolate-focused corpus. Phase 5 extends that work by analyzing chocolate review language across dark, milk, and white chocolate records.

## What This Project Does

- Loads text data from the `data/` folder.
- Applies preprocessing steps: tokenization, lowercasing, punctuation removal, stop-word removal.
- Builds token frequency summaries with Polars.
- Produces visualizations with Matplotlib.
- Extends analysis in Phase 5 with:
  - token comparisons by chocolate type,
  - bigram (two-word phrase) frequency analysis.

## Project Structure

- `src/nlp/text_preprocessing_case.py` - original example pipeline.
- `src/nlp/text_preprocessing_crews.py` - Phase 4 technical modification.
- `src/nlp/text_preprocessing_phase5.py` - Phase 5 chocolate deep-dive.
- `notebooks/text_preprocessing_case.ipynb` - notebook for the original example.
- `notebooks/text_preprocessing_crews.ipynb` - notebook for Phase 4.
- `notebooks/text_preprocessing_phase5.ipynb` - notebook for Phase 5.
- `docs/phase5-project.md` - narrative summary of the final Phase 5 story.

## Setup

Use `uv` from the project root.

PowerShell (Windows):

```powershell
uv self update
uv python pin 3.14
uv sync --extra dev --extra docs --upgrade
```

bash/zsh (macOS/Linux):

```bash
uv self update
uv python pin 3.14
uv sync --extra dev --extra docs --upgrade
```

## Run The Project

Run the Phase 5 module:

```shell
uv run python -m nlp.text_preprocessing_phase5
```

Optional: run the earlier modules.

```shell
uv run python -m nlp.text_preprocessing_case
uv run python -m nlp.text_preprocessing_crews
```

## Notebook Workflow

Open and run all cells in:

- `notebooks/text_preprocessing_phase5.ipynb`

## Documentation

Build docs:

```shell
uv run zensical build
```

Serve docs locally:

```shell
uv run zensical serve
```

## Key Results (Phase 5)

Token count summary:

| Stage | Count |
|---|---:|
| Raw tokens | 143 |
| After punctuation removal | 145 |
| After stop-word removal | 95 |

This is a 33.6% reduction from raw to cleaned tokens.

Key visualization artifacts:

- `docs/images/phase5_top_terms.png`
- `docs/images/phase5_top_bigrams.png`

## Insights

- Flavor vocabulary becomes clearer after cleaning, with stronger signal terms like cocoa, creamy, sweetness, and vanilla.
- Bigram analysis adds context beyond single tokens by highlighting repeated flavor phrases.
- Comparing terms by chocolate type improves interpretability for domain-specific storytelling.
