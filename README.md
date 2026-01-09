# Welcome to survey_cleaner

|        |        |
|--------|--------|
| Package | [![Latest PyPI Version](https://img.shields.io/pypi/v/survey_cleaner.svg)](https://pypi.org/project/survey_cleaner/) [![Supported Python Versions](https://img.shields.io/pypi/pyversions/survey_cleaner.svg)](https://pypi.org/project/survey_cleaner/)  |
| Meta   | [![Code of Conduct](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](CODE_OF_CONDUCT.md) |


survey_cleaner is a project that aims to streamline the process of cleaning survey data by automating common cleaning tasks. Designed to generalize to survey data on different topics, survey_cleaner provides functions to remove duplicate responses, remove unnecessary whitespaces, normalize responses to binary format, and convert ordinal-type responses to numeric data. The package sets up a standardized cleaning framework that can be carried across multiple projects and helps users to reduce manual preprocessing time and minimize errors.

## Functions

- **remove_duplicates**: keeps only the latest survey response from each individual.
- **clean_whitespace**: removes any leading or trailing whitespace in
responses and also double spaces within text.
- **normalize_binary**: converts binary responses such as True and False, T and F, or Yes and No to a binary format (0 and 1).
- **word_to_ordinal**: gives ranking words such as Best, Better, Good, Bad, Worst a numerical rating so that responses can be organized by their numerical values.

## Python Ecosystem

While there are a number of text cleaning packages available on PyPi such as [clean-text](https://pypi.org/project/clean-text/) which preprocesses raw text data on the web, there is no package that is specifically dedicated to cleaning survey response data which is something the `survey_cleaner` package addresses.

## Contributors
Natalie Truesdell, Amanpreet Binepal, Jay Li, Junli

## Get started

You can install this package into your preferred Python environment using pip:

```bash
$ pip install survey_cleaner
```

TODO: Add a brief example of how to use the package to this section

To use survey_cleaner in your code:

```python
>>> import survey_cleaner
>>> survey_cleaner.hello_world()
```

## Copyright

- Copyright © 2026 Natalie Truesdell.
- Free software distributed under the [MIT License](./LICENSE).
