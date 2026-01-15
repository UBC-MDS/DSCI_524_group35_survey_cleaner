import pytest

from survey_cleaner.normalize_binary import normalize_binary

@pytest.mark.parametrize(
    "true_input_response, true_expected_response",
    [
        (True, 1),
        ("T", 1),
        ("t", 1),
        ("Yes", 1),
        ("yEs", 1),
        ("YES", 1),
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


@pytest.mark.parametrize(
    "false_input_response, false_expected_response",
    [
        (False, 0),
        ("F", 0),
        ("f", 0),
        ("No", 0),
        ("no", 0),
        ("NO", 0),
        ("nO", 0),
        ("False", 0),
        ("false", 0),
        (0, 0)
    ]
)

def test_normalize_binary_false(false_input_response, false_expected_response):
    """
    test normalize_binary checking if input values return 0 when False values
    are inputted.
    """
    assert normalize_binary(false_input_response) == false_expected_response


@pytest.mark.parametrize(
    "invalid_input_response",
    [
        (""),
        (" "),
        (None),
        (-1),
        (2),
        (" No "),
        (" No"),
        ("No "),
        ("maybe"),
        ("Maybe")
    ]
)

def test_normalize_binary_invalid(invalid_input_response):
    """
    test normalize_binary checking if any input values are invalid
    """
    with pytest.raises(ValueError):
        normalize_binary(invalid_input_response)
