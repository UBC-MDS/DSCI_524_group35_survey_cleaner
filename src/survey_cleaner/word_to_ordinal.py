"""
A module for converting categorical survey responses to ordinal numbers.

"""


def word_to_ordinal(data, mapping):
    """
    Convert a list of text responses to ordinal values
    based on a user-defined mapping.

    This function is particularly useful for cleaning survey data containing
    Likert scale responses (e.g., "Very Good", "Good", "Bad"). It transforms
    qualitative string data into quantitative numeric data for analysis.

    Parameters
    ----------
    data : list of str
        A list of string responses to be converted.
    mapping : dict
        A dictionary defining the mapping from text to ordinal numbers.
        Keys must be the text categories (str) and values must be
        the corresponding numeric ranking (int).

    Returns
    -------
    list of int
        A list containing the converted ordinal values corresponding to the
        input data.

    Examples
    --------
    >>> responses = ["Very Good", "Good", "Bad"]
    >>> scale_map = {"Very Good": 2, "Good": 1, "Normal": 0, "Bad": -1, "Very Bad": -2}
    >>> word_to_ordinal(responses, scale_map)
    [2, 1, -1]

    >>> feedback = ["Strongly Agree", "Neutral", "Disagree"]
    >>> simple_map = {"Strongly Agree": 5, "Agree": 4, "Neutral": 3, "Disagree": 2, "Strongly Disagree": 1}
    >>> word_to_ordinal(feedback, simple_map)
    [5, 3, 2]

    """
    pass