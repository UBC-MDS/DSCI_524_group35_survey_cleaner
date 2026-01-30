import pandas as pd


def remove_duplicates(
    responses: pd.DataFrame,
    id_col: str,
    datetime_col: str
) -> pd.DataFrame:
    """
    Remove duplicate responses from a DataFrame containing survey data.

    Parameters
    ----------
    responses : pd.DataFrame
        Pandas DataFrame to identify duplicate responses in.
    id_col : str
        Name of the column with the unique identifiers.
    datetime_col : str
        Name of the column containing
        the datetime when the survey was completed.

    Returns
    -------
    pd.DataFrame
        Cleaned, shuffled survey data
        containing only the most recent entry from each individual.


    Examples
    --------
    >>> import pandas as pd
    >>> df = pd.DataFrame({
    ...     'respondent_id': [1, 2, 1, 3],
    ...     'completed_at': ['2024-01-01 10:00', '2024-01-01 11:00',
    ...                      '2024-01-01 12:00', '2024-01-01 13:00'],
    ...     'answer': ['Yes', 'No', 'Maybe', 'Yes']
    ... })
    >>> df['completed_at'] = pd.to_datetime(df['completed_at'])
    >>> remove_duplicates(df, 'respondent_id', 'completed_at')
       respondent_id        completed_at answer
    1              2 2024-01-01 11:00:00     No
    2              1 2024-01-01 12:00:00  Maybe
    3              3 2024-01-01 13:00:00    Yes
    """
    # Input type validation
    if not isinstance(responses, pd.DataFrame):
        raise TypeError("responses must be a pandas DataFrame")
    if not isinstance(id_col, str):
        raise TypeError("id_col must be a string")
    if not isinstance(datetime_col, str):
        raise TypeError("datetime_col must be a string")

    # Test that columns exist in the dataframe
    if id_col not in responses.columns:
        raise KeyError(f"id_col '{id_col}' doesn't exist in the DataFrame")
    if datetime_col not in responses.columns:
        raise KeyError(
            f"datetime_col '{datetime_col}' doesn't exist in the DataFrame")

    # defensive programming
    if responses.empty:
        return responses.copy()
    if responses[id_col].isna().any():
        raise ValueError(f"'{id_col}' contains null values")

    # get rid of duplicates
    no_dups_df = responses.sort_values(
        by=datetime_col
    ).drop_duplicates(
        subset=[id_col],
        keep="last"
    )

    # return df as randomized instead of sorted
    shuffled_df = no_dups_df.sample(
        frac=1,
        random_state=524
    ).reset_index(drop=True)

    return shuffled_df
