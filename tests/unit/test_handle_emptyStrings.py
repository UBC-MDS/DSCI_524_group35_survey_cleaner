"""
Tests for the handle_emptyStrings module.

This module contains unit tests for the handle_emptyStrings function,
which normalizes whitespace in survey response text data.
"""

import pytest
from survey_cleaner.handle_emptyStrings import handle_emptyStrings


def test_handle_emptyStrings_removes_leading_and_trailing():
    """Test that leading and trailing whitespace is removed."""
    assert handle_emptyStrings("  Hello   World  ") == "Hello World"
    assert handle_emptyStrings("   Test   ") == "Test"
    assert handle_emptyStrings("\n\nStart") == "Start"
    assert handle_emptyStrings("End\t\t") == "End"


def test_handle_emptyStrings_collapses_internal_spaces():
    """Test that multiple internal spaces are collapsed to single space."""
    assert handle_emptyStrings("   Multiple   spaces   between   words   ") == "Multiple spaces between words"
    assert handle_emptyStrings("A    B    C") == "A B C"
    assert handle_emptyStrings("Too     many      spaces") == "Too many spaces"


def test_handle_emptyStrings_handles_tabs_and_newlines():
    """Test that tabs and newlines are converted to single spaces."""
    assert handle_emptyStrings("Hello\n\nWorld") == "Hello World"
    assert handle_emptyStrings("Hello\t\tWorld") == "Hello World"
    assert handle_emptyStrings("Line1\nLine2\nLine3") == "Line1 Line2 Line3"
    assert handle_emptyStrings("Tab\t \n Space") == "Tab Space"


def test_handle_emptyStrings_handles_none():
    """Test that None input returns None."""
    assert handle_emptyStrings(None) is None


def test_handle_emptyStrings_handles_empty_string():
    """Test that empty string returns empty string."""
    assert handle_emptyStrings("") == ""
    assert handle_emptyStrings("   ") == ""
    assert handle_emptyStrings("\n\t  ") == ""


def test_handle_emptyStrings_raises_typeerror_for_non_string():
    """Test that non-string input raises TypeError."""
    with pytest.raises(TypeError, match="Input must be a string or None"):
        handle_emptyStrings(123)
    with pytest.raises(TypeError, match="Input must be a string or None"):
        handle_emptyStrings([1, 2, 3])
    with pytest.raises(TypeError, match="Input must be a string or None"):
        handle_emptyStrings({'key': 'value'})


def test_handle_emptyStrings_handles_string_with_no_whitespace():
    """Test that strings without whitespace are returned unchanged."""
    assert handle_emptyStrings("NoWhitespace") == "NoWhitespace"
    assert handle_emptyStrings("SingleWord") == "SingleWord"
    assert handle_emptyStrings("123") == "123"
