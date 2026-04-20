#!/usr/bin/env python3
"""Unit tests for slugify function in tools/research_wiki.py."""

import os
import sys
import unittest

# Make the tools/ directory importable as a module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'tools'))
from research_wiki import slugify

class TestSlugify(unittest.TestCase):
    """Test cases for the slugify function."""

    def test_standard_input(self):
        """Test with standard title, author, and year."""
        self.assertEqual(slugify("Deep Residual Learning for Image Recognition", "He", 2016), "he2016_deep_residual_learning")

    def test_stop_words_and_special_characters(self):
        """Test that stop words are filtered and special characters are removed from title."""
        self.assertEqual(slugify("A Study of Deep Learning! with Attention?", "Vaswani", 2017), "vaswani2017_study_deep_learning")

    def test_missing_author(self):
        """Test behavior when author is missing."""
        self.assertEqual(slugify("Attention Is All You Need", year=2017), "unknown2017_attention_all_you")

    def test_missing_year(self):
        """Test behavior when year is missing."""
        self.assertEqual(slugify("Attention Is All You Need", author_last="Vaswani"), "vaswani0000_attention_all_you")

    def test_missing_both_author_and_year(self):
        """Test behavior when both author and year are missing."""
        self.assertEqual(slugify("Attention Is All You Need"), "unknown0000_attention_all_you")

    def test_author_with_special_characters(self):
        """Test that special characters in author name are removed."""
        self.assertEqual(slugify("Title", "O'Neill", 2024), "oneill2024_title")

    def test_short_words_filtering(self):
        """Test that words with length <= 2 are filtered out of keywords."""
        self.assertEqual(slugify("Go to ML", "User", 2024), "user2024_untitled")

    def test_empty_title(self):
        """Test behavior with an empty title."""
        self.assertEqual(slugify("", "Author", 2024), "author2024_untitled")

    def test_title_with_only_stop_words(self):
        """Test behavior with a title containing only stop words."""
        self.assertEqual(slugify("A and The", "Author", 2024), "author2024_untitled")

    def test_keyword_limit(self):
        """Test that at most 3 keywords are used."""
        self.assertEqual(slugify("One Two Three Four Five", "Author", 2024), "author2024_one_two_three")

    def test_lowercase_normalization(self):
        """Test that everything is lowercased in the slug."""
        self.assertEqual(slugify("BIG TITLE", "AUTHOR", 2024), "author2024_big_title")

if __name__ == "__main__":
    unittest.main()
