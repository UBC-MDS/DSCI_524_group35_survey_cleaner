"""
A module that normalizes binary responses written in
different formats such as True and False to a binary
format (0 or 1).

"""

def normalize_binary(response):
    """
    Convert response to binary format (0 or 1).

    Takes in a response such as True or False, T or F,
    Yes or No and converts it to a normalized binary
    format of 0 or 1.

    Parameters
    ----------
    response : bool, str, int
        The responses that must be normalized are:
        - Boolean: True, False
        - String: "T", "F", "Yes", "No", "True", "False" (case insensitive)
        The responses that don't have to be normalized are:
        - Integer: 0, 1
    Returns
    -------
    int
        0 or 1; the normalized binary format

    Examples
    --------
    >>> normalize_binary(True)
    1
    >>> normalize_binary("No")
    0
    >>> normalize_binary("T")
    1
    >>> normalize_binary(1)
    1
    >>> normalize_binary("False")
    0

    """
    pass
