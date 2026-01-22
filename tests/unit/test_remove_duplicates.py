import pytest
import pandas as pd
import os

from survey_cleaner.remove_duplicates import remove_duplicates
from pytest_lazy_fixtures import lf

# Define fixture inputs for test functions
@pytest.fixture
def text_data():
    csv_path = os.path.join(os.path.dirname(__file__), '..', 'fixtures', 'example_text.csv')
    df = pd.read_csv(csv_path)
    df['completed_at'] = pd.to_datetime(df['completed_at'])
    return df

@pytest.fixture
def text_data_output():
    csv_path = os.path.join(os.path.dirname(__file__), '..', 'fixtures', 'example_output.csv')
    df = pd.read_csv(csv_path)
    df['completed_at'] = pd.to_datetime(df['completed_at'])
    return df

@pytest.fixture
def series_data(text_data):
    return text_data["respondent_id"]

# Define parametrized inputs for test_input
@pytest.mark.parametrize(
    "responses, id_col, datetime_col",
    [
        (lf("series_data"), "respondent_id", "completed_at"),
        (lf("text_data"), 2, "completed_at"),
        (lf("text_data"), "respondent_id", 2)
    ]
)


# Input validation
def test_input(responses, id_col, datetime_col):
    """
    Test remove_duplicates raises TypeError for invalid input types.

    Parametrized test cases:
    - Series instead of DataFrame for responses
    - Integer instead of string for id_col
    - Integer instead of string for datetime_col

    All cases should raise TypeError.
    """
    with pytest.raises(TypeError):
        remove_duplicates(responses, id_col, datetime_col)

def test_columns_not_in(text_data):
    """
    Test KeyError when given a column name not in responses.
    """
    with pytest.raises(KeyError):
        remove_duplicates(text_data, "participant", "completed_at")


# Output validation
def test_duplicate_removal(text_data, text_data_output):
    """
    Test function removes duplicate response.
    """
    no_dups = remove_duplicates(text_data, "respondent_id", "completed_at")
    
    # Sort both by respondent_id and reset index for comparison
    no_dups_sorted = no_dups.sort_values("respondent_id").reset_index(drop=True)
    expected_sorted = text_data_output.sort_values("respondent_id").reset_index(drop=True)

    pd.testing.assert_frame_equal(no_dups_sorted, expected_sorted)

def test_no_duplicate_ids(text_data):
    """
    Test no duplicate ids in output DataFrame.
    """
    no_dups = remove_duplicates(text_data, "respondent_id", "completed_at")
    assert no_dups["respondent_id"].is_unique

def test_same_columns(text_data):
    """
    Test output df has same columns as input df.
    """
    no_dups = remove_duplicates(text_data, "respondent_id", "completed_at")
    assert list(no_dups.columns) == list(text_data.columns)


def test_empty_dataframe():
    """
    Test that function handles empty DataFrame correctly.

    When given an empty DataFrame, the function should return an empty
    DataFrame without raising errors.
    """
    empty_df = pd.DataFrame(columns=["respondent_id", "completed_at", "answer"])
    result = remove_duplicates(empty_df, "respondent_id", "completed_at")
    assert result.empty
    assert list(result.columns) == ["respondent_id", "completed_at", "answer"]
