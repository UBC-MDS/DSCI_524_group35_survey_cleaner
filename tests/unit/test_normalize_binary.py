import pytest

from survey_cleaner.normalize_binary import normalize_binary

@pytest.mark.parametrize(
    "true_input_response, true_expected_response",
    [
        (True, 1),
        ("T", 1),
        ("t", 1),
        ("Yes", 1),
        ("yes", 1),
        ("True", 1),
        ("true", 1),
        (1, 1)
    ]
)

def test_normalize_binary_true(true_input_response, true_expected_response):
    """
    test normalize_binary checking if input values return 1 when True values
    are inputted.
    """
    assert normalize_binary(true_input_response) == true_expected_response
