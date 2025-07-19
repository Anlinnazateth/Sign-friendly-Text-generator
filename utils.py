"""Sign-language-friendly text conversion utilities."""

import re
from typing import Dict, List

import nltk
from nltk.corpus import stopwords

# Download required NLTK data
nltk.download("stopwords", quiet=True)
nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)

STOP_WORDS = set(stopwords.words("english"))


def sign_friendly_convert(text: str) -> Dict:
    """Convert English text to sign-language-friendly text.

    Removes stopwords, punctuation, and non-alphabetic tokens to produce
    a simplified version suitable for sign language interpretation.

    Args:
        text: Input English sentence or paragraph.

    Returns:
        Dictionary with keys:
            - original: the input text
            - simplified: cleaned output text
            - removed_words: list of removed words
            - word_count_original: original word count
            - word_count_simplified: simplified word count
            - reduction_percentage: percentage of words removed
    """
    if not text or not text.strip():
        return {
            "original": text or "",
            "simplified": "",
            "removed_words": [],
            "word_count_original": 0,
            "word_count_simplified": 0,
            "reduction_percentage": 0.0,
        }

    # Tokenize using NLTK for better handling of punctuation
    try:
        tokens = nltk.word_tokenize(text)
    except LookupError:
        # Fallback to simple split if tokenizer data unavailable
        tokens = text.split()

    original_count = len(tokens)
    removed = []
    kept = []

    for token in tokens:
        # Remove punctuation and non-alphabetic tokens
        clean = re.sub(r"[^a-zA-Z]", "", token)
        if not clean:
            removed.append(token)
            continue
        if clean.lower() in STOP_WORDS:
            removed.append(token)
            continue
        kept.append(clean)

    simplified = " ".join(kept)
    simplified_count = len(kept)
    reduction = ((original_count - simplified_count) / original_count * 100) if original_count > 0 else 0.0

    return {
        "original": text,
        "simplified": simplified,
        "removed_words": removed,
        "word_count_original": original_count,
        "word_count_simplified": simplified_count,
        "reduction_percentage": round(reduction, 1),
    }
