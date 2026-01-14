import pytest
import pandas as pd
import os
import numpy as np

from survey_cleaner.remove_duplicates import remove_duplicates

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

# Input validation
def test_non_dataframe_input(text_data):
    """
    test TypeError when responses is not a DataFrame
    """
    test_series = text_data["respondent_id"]
    with pytest.raises(TypeError):
        remove_duplicates(test_series, "respondent_id", "completed_at")

def test_columns_not_in(text_data):
    """
    test KeyError when given a column name not in responses
    """
    with pytest.raises(KeyError):
        remove_duplicates(text_data, "participant", "completed_at")


# Output validation
def test_duplicate_removal(text_data, text_data_output):
    """
    test function removes duplicate response
    """
    no_dups = remove_duplicates(text_data, "respondent_id", "completed_at")
    pd.testing.assert_frame_equal(no_dups, text_data_output)

def test_no_duplicate_ids(text_data):
    """
    test no duplicate ids in output df
    """
    no_dups = remove_duplicates(text_data, "respondent_id", "completed_at")
    assert no_dups["respondent_id"].is_unique

def test_same_columns(text_data):
    """
    test output df has same columns as input df
    """
    no_dups = remove_duplicates(text_data, "respondent_id", "completed_at")
    assert list(no_dups.columns) == list(text_data.columns)
