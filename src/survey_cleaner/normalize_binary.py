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
    if isinstance(response, bool):
        return int(response)

    if isinstance(response, int):
        if response == 0 or response == 1:
            return response
        else:
            raise ValueError("Integer responses must be 0 (False) or 1 (True)")

    if isinstance(response, str):
        valid_true_responses = {"true", "t", "yes"}
        valid_false_responses = {"false", "f", "no"}
        if not response:
            raise ValueError("String responses cannot be empty")
        if any(c.isspace() for c in response):
            raise ValueError("String responses cannot have whitespace")
        lower_response = response.lower()
        if lower_response in valid_true_responses:
            return 1
        elif lower_response in valid_false_responses:
            return 0
        else:
            raise ValueError("Invalid string response: (must be one of 'Yes', 'No', 'True', 'False', 'T', 'F')")

    raise ValueError("Invalid response format (Must be boolean, 0 or 1 integer, or the following strings: 'Yes', 'No', 'True', 'False', 'T', 'F')")
