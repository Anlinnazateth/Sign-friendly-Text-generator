"""Tests for the sign-friendly text converter."""

import os
import sys
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from utils import sign_friendly_convert


class TestBasicConversion:
    def test_removes_stopwords(self):
        result = sign_friendly_convert("I am going to the market")
        assert "going" in result["simplified"]
        assert "market" in result["simplified"]

    def test_keeps_content_words(self):
        result = sign_friendly_convert("The cat sat on the mat")
        assert "cat" in result["simplified"]
        assert "sat" in result["simplified"]
        assert "mat" in result["simplified"]

    def test_removes_punctuation(self):
        result = sign_friendly_convert("Hello, world! How are you?")
        assert "," not in result["simplified"]
        assert "!" not in result["simplified"]
        assert "?" not in result["simplified"]

    def test_example_from_readme(self):
        result = sign_friendly_convert("I will be going to the market tomorrow.")
        assert "going" in result["simplified"]
        assert "market" in result["simplified"]
        assert "tomorrow" in result["simplified"]


class TestEdgeCases:
    def test_empty_string(self):
        result = sign_friendly_convert("")
        assert result["simplified"] == ""
        assert result["word_count_original"] == 0
        assert result["word_count_simplified"] == 0

    def test_none_input(self):
        result = sign_friendly_convert(None)
        assert result["simplified"] == ""

    def test_single_content_word(self):
        result = sign_friendly_convert("cat")
        assert result["simplified"] == "cat"
        assert result["word_count_simplified"] == 1

    def test_all_stopwords(self):
        result = sign_friendly_convert("I am the a an is are was were")
        assert result["word_count_simplified"] == 0

    def test_only_punctuation(self):
        result = sign_friendly_convert("!!! ??? ...")
        assert result["simplified"] == ""

    def test_whitespace_only(self):
        result = sign_friendly_convert("   ")
        assert result["simplified"] == ""


class TestStatistics:
    def test_word_count(self):
        result = sign_friendly_convert("The quick brown fox")
        assert result["word_count_original"] == 4

    def test_reduction_percentage(self):
        result = sign_friendly_convert("I am going to the market tomorrow")
        assert 0 <= result["reduction_percentage"] <= 100

    def test_removed_words_tracked(self):
        result = sign_friendly_convert("I am happy")
        # "I" and "am" should be in removed_words
        removed_lower = [w.lower() for w in result["removed_words"]]
        assert "i" in removed_lower or "am" in removed_lower

    def test_return_type(self):
        result = sign_friendly_convert("Hello world")
        assert isinstance(result, dict)
        assert "original" in result
        assert "simplified" in result
        assert "removed_words" in result
        assert "word_count_original" in result
        assert "word_count_simplified" in result
        assert "reduction_percentage" in result
