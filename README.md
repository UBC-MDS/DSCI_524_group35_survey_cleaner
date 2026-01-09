# Welcome to survey_cleaner

|        |        |
|--------|--------|
| Package | [![Latest PyPI Version](https://img.shields.io/pypi/v/survey_cleaner.svg)](https://pypi.org/project/survey_cleaner/) [![Supported Python Versions](https://img.shields.io/pypi/pyversions/survey_cleaner.svg)](https://pypi.org/project/survey_cleaner/)  |
| Meta   | [![Code of Conduct](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](CODE_OF_CONDUCT.md) |

*TODO: the above badges that indicate python version and package version will only work if your package is on PyPI.
If you don't plan to publish to PyPI, you can remove them.*

survey_cleaner is a project that (describe what it does here).

## Functions

- **normalize_number**: converts numerical responses that have been written as a word to numerical format ("one" to 1).
- **clean_whitespace**: removes any leading or trailing whitespace in
responses and also double spaces within text.
- **normalize_binary**: converts binary responses such as True and False, T and F, or Yes and No to a binary format (0 and 1).
- **word_to_ordinal**: gives ranking words such as Best, Better, Good, Bad, Worst a numerical rating so that responses can be organized by their numerical values.

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
