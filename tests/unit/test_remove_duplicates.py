import pytest
import pandas as pd
import os

from survey_cleaner.remove_duplicates import remove_duplicates
from pytest_lazyfixture import lazy_fixture

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
        (lazy_fixture("series_data"), "respondent_id", "completed_at"),
        (lazy_fixture("text_data"), 2, "completed_at"),
        (lazy_fixture("text_data"), "respondent_id", 2)
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
    pd.testing.assert_frame_equal(no_dups, text_data_output)

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
