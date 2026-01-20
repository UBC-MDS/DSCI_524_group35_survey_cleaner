import pandas as pd


def word_to_ordinal(
    data, mapping=None, likert=None, case_insensitive=True
):
    """
    Convert a list of text responses to ordinal values
    based on a mapping or a pre-defined scale.

    This function transforms qualitative string data (e.g., "Very Good") into
    quantitative numeric data. It supports custom mappings or built-in standard
    scales (Likert scales). It also handles case sensitivity robustness.

    Parameters
    ----------
    data : list of str or pd.Series
        A list of string responses to be converted.
    mapping : dict, optional
        A dictionary mapping text categories (str) to ordinal numbers (int).
        If None, `likert` must be provided.
    likert : str, optional
        The name of a pre-defined likert scale to use. Supported types:
        
        - "agreement": {"Strongly Agree": 5, "Agree": 4, ...}
        - "satisfaction": {"Very Satisfied": 5, "Satisfied": 4, ...}
        - "frequency": {"Always": 5, "Often": 4, ...}
        - "likelihood": {"Very Likely": 5, "Likely": 4, ...}
        
        If None, `mapping` must be provided.
    case_insensitive : bool, default True
        If True, the conversion will ignore case differences between `data`
        and the `mapping` keys (e.g., "Good" maps to "good").

    Returns
    -------
    list or pd.Series
        Converted ordinal values.

    Raises
    ------
    ValueError
        If neither `mapping` nor `likert` is provided, or if both are provided.
        If a value in `data` acts as a key that is not found in the mapping.
    TypeError
        If input data is not a list or pandas Series.

    Examples
    --------
    >>> # Example 1: Using a custom mapping
    >>> word_to_ordinal(["Good", "Bad"], mapping={"Good": 1, "Bad": 0})
    [1, 0]

    >>> # Example 2: Using a built-in scale
    >>> feedback = ["Strongly Agree", "Agree"]
    >>> word_to_ordinal(feedback, likert="agreement")
    [5, 4]
    """
    # 1. Input Validation
    if not isinstance(data, (list, pd.Series)):
        raise TypeError("Input data must be a list or pandas Series")

    if mapping is None and likert is None:
        raise ValueError("Provide either mapping or likert scale")

    if mapping is not None and likert is not None:
        raise ValueError("Provide either mapping or likert, not both")

    # 2. Define Standard Likert Scales (5-point)
    # Mapping logic: Positive/High intensity = 5, Negative/Low intensity = 1
    likert_scales = {
        "agreement": {
            "strongly agree": 5, "agree": 4, "neither agree nor disagree": 3,
            "disagree": 2, "strongly disagree": 1
        },
        "satisfaction": {
            "very satisfied": 5, "satisfied": 4, "neutral": 3,
            "dissatisfied": 2, "very dissatisfied": 1
        },
        "frequency": {
            "always": 5, "often": 4, "sometimes": 3, "rarely": 2, "never": 1
        },
        "likelihood": {
            "very likely": 5, "likely": 4, "neutral": 3,
            "unlikely": 2, "very unlikely": 1
        }
    }

    # 3. Determine Target Mapping
    if likert:
        if likert not in likert_scales:
            valid = ", ".join(likert_scales.keys())
            raise ValueError(f"Unknown likert scale. Valid options: {valid}")
        target_mapping = likert_scales[likert]
    else:
        target_mapping = mapping

    # 4. Handle Case Insensitivity
    if case_insensitive:
        target_mapping = {k.lower(): v for k, v in target_mapping.items()}

    # 5. Process Data for Lookup
    if isinstance(data, pd.Series):
        lookup_data = data.astype(str)
        if case_insensitive:
            lookup_data = lookup_data.str.lower()
    else:
        lookup_data = [str(x) for x in data]
        if case_insensitive:
            lookup_data = [x.lower() for x in lookup_data]

    # 6. Validate Data Content
    unique_inputs = set(lookup_data)
    valid_keys = set(target_mapping.keys())
    unknowns = unique_inputs - valid_keys

    if unknowns:
        raise ValueError(f"Values not found in mapping: {unknowns}")

    # 7. Apply Mapping
    if isinstance(data, pd.Series):
        return lookup_data.map(target_mapping)
    else:
        return [target_mapping[x] for x in lookup_data]
