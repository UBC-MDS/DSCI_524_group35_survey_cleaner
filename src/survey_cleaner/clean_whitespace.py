"""
A module for cleaning whitespace in survey response text data.

This module provides functionality to normalize whitespace in text responses,
including collapsing multiple spaces and removing leading/trailing whitespace.
"""


def clean_whitespace(text):
    """
    Clean and normalize whitespace in text input.

    This function removes leading and trailing whitespace and collapses
    all internal sequences of whitespace characters (spaces, tabs, newlines)
    into single spaces. This is particularly useful for cleaning free-text
    survey responses that may contain inconsistent formatting.

    Parameters
    ----------
    text : str or None
        The text string to clean. If None is provided, the function returns None.

    Returns
    -------
    str or None
        The cleaned text with normalized whitespace. Returns None if input is None.

    Raises
    ------
    TypeError
        If the input is not a string or None.

    Examples
    --------
    >>> clean_whitespace("  Hello   World  ")
    'Hello World'

    >>> clean_whitespace("Hello\\n\\nWorld")
    'Hello World'

    >>> clean_whitespace("Hello\\t\\tWorld")
    'Hello World'

    >>> clean_whitespace("   Multiple   spaces   between   words   ")
    'Multiple spaces between words'

    >>> clean_whitespace(None)
    None

    >>> clean_whitespace("")
    ''

    >>> clean_whitespace("NoWhitespace")
    'NoWhitespace'

    >>> clean_whitespace(123)
    Traceback (most recent call last):
        ...
    TypeError: Input must be a string or None, not int

    """
    pass
