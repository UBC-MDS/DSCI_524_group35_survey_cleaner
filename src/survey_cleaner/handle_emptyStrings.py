"""
A module for cleaning whitespace in survey response text data.

This module provides functionality to normalize whitespace in text responses,
including collapsing multiple spaces and removing leading/trailing whitespace.
"""


def handle_emptyStrings(text):
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
    >>> handle_emptyStrings("  Hello   World  ")
    'Hello World'

    >>> handle_emptyStrings("Hello\\n\\nWorld")
    'Hello World'

    >>> handle_emptyStrings("Hello\\t\\tWorld")
    'Hello World'

    >>> handle_emptyStrings("   Multiple   spaces   between   words   ")
    'Multiple spaces between words'

    >>> handle_emptyStrings(None)
    None

    >>>handle_emptyStrings("")
    ''

    >>> handle_emptyStrings("NoWhitespace")
    'NoWhitespace'

    >>> handle_emptyStrings(123)
    Traceback (most recent call last):
        ...
    TypeError: Input must be a string or None, not int

    """
    pass
