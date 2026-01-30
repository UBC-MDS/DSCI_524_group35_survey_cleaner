import pytest
import pandas as pd
import os
from survey_cleaner.word_to_ordinal import word_to_ordinal


@pytest.fixture
def raw_survey_data():
    """Load raw survey data from csv file."""
    csv_path = os.path.join(os.path.dirname(__file__), '..',
                            'fixtures', 'ordinal_data.csv')
    return pd.read_csv(csv_path)


def test_input_type_validation():
    """Test TypeError on invalid input types."""
    with pytest.raises(TypeError,
                       match="Input data must be a list or pandas Series"):
        word_to_ordinal(123, likert="agreement")


def test_argument_conflict():
    """Test ValueError when both mapping and likert are provided."""
    with pytest.raises(ValueError, match="Provide either mapping or likert"):
        word_to_ordinal(["test"], mapping={"A": 1}, likert="agreement")


def test_likert_agreement(raw_survey_data):
    """Test standard 5-point Agreement scale (Strongly Agree=5)."""
    input_series = raw_survey_data["agreement"]
    # Expect: Strongly Agree(5) -> Strongly Disagree(1)
    expected = pd.Series([5, 4, 3, 2, 1], name="agreement")

    result = word_to_ordinal(input_series, likert="agreement")
    pd.testing.assert_series_equal(result, expected, check_names=False)


def test_likert_satisfaction(raw_survey_data):
    """Test standard 5-point Satisfaction scale (Very Satisfied=5)."""
    input_series = raw_survey_data["satisfaction"]
    expected = pd.Series([5, 4, 3, 2, 1], name="satisfaction")

    result = word_to_ordinal(input_series, likert="satisfaction")
    pd.testing.assert_series_equal(result, expected, check_names=False)


def test_likert_frequency(raw_survey_data):
    """Test standard 5-point Frequency scale (Always=5)."""
    input_series = raw_survey_data["frequency"]
    expected = pd.Series([5, 4, 3, 2, 1], name="frequency")

    result = word_to_ordinal(input_series, likert="frequency")
    pd.testing.assert_series_equal(result, expected, check_names=False)


def test_likert_likelihood(raw_survey_data):
    """Test standard 5-point Likelihood scale (Very Likely=5)."""
    input_series = raw_survey_data["likelihood"]
    expected = pd.Series([5, 4, 3, 2, 1], name="likelihood")

    result = word_to_ordinal(input_series, likert="likelihood")
    pd.testing.assert_series_equal(result, expected, check_names=False)


def test_invalid_likert_option():
    """Test ValueError for unknown likert scale names."""
    data = ["test"]
    with pytest.raises(ValueError, match="Unknown likert scale"):
        word_to_ordinal(data, likert="invalid_scale")


def test_custom_mapping():
    """Test functionality with a user-provided mapping."""
    data = ["High", "Low"]
    mapping = {"High": 10, "Low": 0}
    expected = [10, 0]
    assert word_to_ordinal(data, mapping=mapping) == expected


def test_case_sensitive_mapping():
    """Test case_insensitive=False requires exact case match."""
    data = ["Good", "Bad"]
    mapping = {"Good": 1, "Bad": 0}

    # Should work with exact case match
    result = word_to_ordinal(data, mapping=mapping, case_insensitive=False)
    assert result == [1, 0]

    # Should fail with mismatched case
    data_lowercase = ["good", "bad"]
    with pytest.raises(ValueError, match="Values not found in mapping"):
        word_to_ordinal(data_lowercase, mapping=mapping,
                        case_insensitive=False)


def test_no_mapping_provided():
    """Test ValueError when neither mapping nor likert is provided."""
    with pytest.raises(ValueError, match="Provide either mapping or likert scale"):
        word_to_ordinal(["test"])


def test_list_processing_and_case():
    """Test that list input correctly handles case insensitivity and string conversion."""
    data = ["Always", "never", 1]
    mapping = {"always": 3, "never": 1, "1": 5}
    result = word_to_ordinal(data, mapping=mapping, case_insensitive=True)
    assert result == [3, 1, 5]
    assert isinstance(result, list)


def test_unknown_values_error_message():
    """Check if the error message correctly lists unknown values."""
    with pytest.raises(ValueError, match="Values not found in mapping: {'unknown'}"):
        word_to_ordinal(["unknown"], likert="agreement")
