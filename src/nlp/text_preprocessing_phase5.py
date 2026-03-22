"""
text_preprocessing_phase5.py - Phase 5 project script.

Purpose

    Extend the chocolate preprocessing work by analyzing token patterns
    across chocolate types (dark, milk, white) and common bigrams.

Run from root project folder with:

  uv run python -m nlp.text_preprocessing_phase5
"""

import logging
from pathlib import Path
import re

from datafun_toolkit.logger import get_logger, log_header, log_path
import matplotlib.pyplot as plt
import polars as pl

print("Imports complete.")

LOG: logging.Logger = get_logger("CI", level="DEBUG")

ROOT_PATH: Path = Path.cwd()
DATA_PATH: Path = ROOT_PATH / "data"
DOCS_IMAGES_PATH: Path = ROOT_PATH / "docs" / "images"

log_header(LOG, "NLP")
LOG.info("START script.....")

log_path(LOG, "ROOT_PATH", ROOT_PATH)
log_path(LOG, "DATA_PATH", DATA_PATH)
log_path(LOG, "DOCS_IMAGES_PATH", DOCS_IMAGES_PATH)

input_path: Path = DATA_PATH / "text_data_phase5.txt"

text_list: list[str] = input_path.read_text(encoding="utf-8").splitlines()
text_list = [line.strip() for line in text_list if line.strip()]

print("Data loaded successfully.")
print(f"Loaded {len(text_list):,} text records.")

records: list[dict[str, str]] = []
for line in text_list:
    parts = [part.strip() for part in line.split("|", maxsplit=1)]
    if len(parts) == 2 and parts[0] and parts[1]:
        records.append({"chocolate_type": parts[0].lower(), "review_text": parts[1]})

reviews_df: pl.DataFrame = pl.DataFrame(records)
raw_text: str = " ".join(reviews_df["review_text"].to_list())
print(f"Raw text length: {len(raw_text):,} characters")

raw_tokens: list[str] = raw_text.split()
count_of_raw_tokens: int = len(raw_tokens)

lower_text: str = raw_text.lower()
no_punct_text: str = re.sub(r"[^a-z0-9\s]", " ", lower_text)

tokens_no_punct: list[str] = no_punct_text.split()
count_of_tokens_no_punct: int = len(tokens_no_punct)

STOP_WORDS: set[str] = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "but",
    "by",
    "for",
    "from",
    "has",
    "have",
    "in",
    "is",
    "it",
    "its",
    "of",
    "on",
    "or",
    "that",
    "the",
    "to",
    "was",
    "were",
    "will",
    "with",
    "after",
    "before",
    "during",
    "each",
    "over",
    "some",
    "when",
    "bar",
    "notes",
    "note",
    "flavor",
    "finish",
    "profile",
    "texture",
}


def preprocess_tokens(text: str) -> list[str]:
    """Return cleaned tokens for one review string."""
    lower_value: str = text.lower()
    clean_text: str = re.sub(r"[^a-z0-9\s]", " ", lower_value)
    tokens: list[str] = clean_text.split()
    return [tok for tok in tokens if len(tok) > 2 and tok not in STOP_WORDS]


token_rows: list[dict[str, str]] = []
for row in reviews_df.iter_rows(named=True):
    row_tokens = preprocess_tokens(row["review_text"])
    for token in row_tokens:
        token_rows.append({"chocolate_type": row["chocolate_type"], "token": token})

token_df: pl.DataFrame = pl.DataFrame(token_rows)
clean_tokens: list[str] = token_df["token"].to_list()
count_of_clean_tokens: int = len(clean_tokens)

summary_df: pl.DataFrame = pl.DataFrame(
    {
        "stage": [
            "raw tokens",
            "after punctuation removal",
            "after stop word removal",
        ],
        "count": [
            count_of_raw_tokens,
            count_of_tokens_no_punct,
            count_of_clean_tokens,
        ],
    }
)

print("Preprocessing summary:")
print(summary_df)

freq_df: pl.DataFrame = token_df.group_by("token").len().sort("len", descending=True)

by_type_df: pl.DataFrame = (
    token_df.group_by(["chocolate_type", "token"])
    .len()
    .sort(["chocolate_type", "len", "token"], descending=[False, True, False])
    .with_columns(pl.cum_count("token").over("chocolate_type").alias("rank"))
    .filter(pl.col("rank") <= 5)
)

bigrams: list[str] = [
    f"{clean_tokens[i]} {clean_tokens[i + 1]}" for i in range(len(clean_tokens) - 1)
]
bigram_df: pl.DataFrame = (
    pl.DataFrame({"bigram": bigrams})
    .group_by("bigram")
    .len()
    .sort("len", descending=True)
)

print("Top 15 most frequent cleaned tokens:")
print(freq_df.head(15))
print("Top tokens by chocolate type:")
print(by_type_df)
print("Top 10 bigrams:")
print(bigram_df.head(10))

DOCS_IMAGES_PATH.mkdir(parents=True, exist_ok=True)

# Save chart 1: top token frequencies.
top_df: pl.DataFrame = freq_df.head(10)
plt.figure(figsize=(10, 5))
plt.bar(top_df["token"], top_df["len"], color="#5c3d2e")
ax = plt.gca()
ax.tick_params(axis="x", labelrotation=40)
plt.title("Top Terms in Chocolate Reviews")
plt.xlabel("Token")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig(DOCS_IMAGES_PATH / "phase5_top_terms.png", dpi=150)
plt.close()

# Save chart 2: top bigrams for richer phrase-level insight.
top_bigram_df: pl.DataFrame = bigram_df.head(10)
plt.figure(figsize=(8, 5))
plt.bar(top_bigram_df["bigram"], top_bigram_df["len"], color="#8b6b4a")
ax = plt.gca()
ax.tick_params(axis="x", labelrotation=45)
plt.title("Top Chocolate Bigrams")
plt.xlabel("Bigram")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig(DOCS_IMAGES_PATH / "phase5_top_bigrams.png", dpi=150)
plt.close()

LOG.info("========================")
LOG.info("Pipeline executed successfully!")
LOG.info("========================")
LOG.info("END main()")
