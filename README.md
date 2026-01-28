# Welcome to survey_cleaner

## Table of Contents
- [Welcome to survey\_cleaner](#welcome-to-survey_cleaner)
  - [Table of Contents](#table-of-contents)
  - [Functions](#functions)
  - [Python Ecosystem](#python-ecosystem)
  - [Installation](#installation)
  - [Usage Examples:](#usage-examples)
    - [Clean Whitespace](#clean-whitespace)
    - [Normalize Binary Responses](#normalize-binary-responses)
    - [Convert Ordinal Responses to Numeric](#convert-ordinal-responses-to-numeric)
    - [Remove Duplicate Responses](#remove-duplicate-responses)
  - [Developer Setup](#developer-setup)
  - [Build Documentation](#build-documentation)
    - [Building Documentation Locally](#building-documentation-locally)
  - [Deploy Documentation](#deploy-documentation)
    - [Workflow Overview](#workflow-overview)
    - [Documentation Build Workflow](#documentation-build-workflow)
    - [Documentation Publish Workflow](#documentation-publish-workflow)
    - [Viewing Published Documentation](#viewing-published-documentation)
  - [Contributing](#contributing)
  - [Contributors](#contributors)
  - [Copyright](#copyright)

|   | |
|---|---|
| **Deployment** | [![Publish to TestPyPI](https://github.com/UBC-MDS/DSCI_524_group35_survey_cleaner/actions/workflows/deploy.yml/badge.svg)](https://github.com/UBC-MDS/DSCI_524_group35_survey_cleaner/actions/workflows/deploy.yml) |
| **Meta** | [![Code of Conduct](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](CODE_OF_CONDUCT.md) |
| **Codecov** |[![codecov](https://codecov.io/github/ubc-mds/dsci_524_group35_survey_cleaner/graph/badge.svg?token=fYoyXiBsXh)](https://codecov.io/github/ubc-mds/dsci_524_group35_survey_cleaner) |


survey_cleaner is a project that aims to streamline the process of cleaning survey data by automating common cleaning tasks. Designed to generalize to survey data on different topics, survey_cleaner provides functions to remove duplicate responses, remove unnecessary whitespaces, normalize responses to binary format, and convert ordinal-type responses to numeric data. The package sets up a standardized cleaning framework that can be carried across multiple projects and helps users to reduce manual preprocessing time and minimize errors.

## Functions

- `remove_duplicates`: keeps only the latest survey response from each individual.
- `handle_emptyStrings`: handle None, raise TypeError for non-string inputs, collapse all whitespace into single spaces and strip leading/trailing whitespace, and write the corresponding docstring.
- `normalize_binary`: converts binary responses such as True and False, T and F, or Yes and No to a binary format (0 and 1).
- `word_to_ordinal`: gives ranking words such as Best, Better, Good, Bad, Worst a numerical rating so that responses can be organized by their numerical values. Likert scale are set up as default rankings but users can also provide their own rankings.

## Python Ecosystem

While there are a number of text cleaning packages available on PyPi such as [clean-text](https://pypi.org/project/clean-text/) which preprocesses raw text data on the web, there is no package that is specifically dedicated to cleaning survey response data which is something the `survey_cleaner` package addresses.


## Installation

Clone the repository to your local:

```bash
$ git clone https://github.com/UBC-MDS/DSCI_524_group35_survey_cleaner.git

$ cd DSCI_524_group35_survey_cleaner
```

It is recommended but not required to use the environment file to create a conda environment:

```bash
$ conda env create -f environment.yml

$ conda activate survey_cleaner
```

You can install this package into your preferred Python environment using pip:

```bash
$ pip install survey_cleaner
```

## Usage Examples:

### Clean Whitespace
```python
import pandas as pd
from survey_cleaner import handle_emptyStrings

# Removes leading/trailing whitespace and collapses multiple spaces
df['comments'] = handle_emptyStrings(df['comments'])
```
### Normalize Binary Responses
```python
from survey_cleaner import normalize_binary

# Converts Yes/No, True/False, T/F to 1/0
df['response'] = normalize_binary(df['response'])
```
### Convert Ordinal Responses to Numeric
```python
from survey_cleaner import word_to_ordinal

# Converts Best/Good/Bad/Worst to numeric ratings
df['rating'] = word_to_ordinal(df['rating'])
```
### Remove Duplicate Responses
```python
from survey_cleaner import remove_duplicates

responses = pd.DataFrame({
     'respondent_id': [1, 2, 1, 3],
     'completed_at': ['2024-01-01 10:00', '2024-01-01 11:00', 
                      '2024-01-01 12:00', '2024-01-01 13:00'],
     'answer': ['Yes', 'No', 'Maybe', 'Yes']
 })
 
clean_responses = remove_duplicates(responses, 'respondent_id', 'completed_at')
```

## Developer Setup
Clone the repository to your local:

```bash
$ git clone https://github.com/UBC-MDS/DSCI_524_group35_survey_cleaner.git

$ cd DSCI_524_group35_survey_cleaner
```

It is recommended but not required to use the environment file to create a conda environment:

```bash
$ conda env create -f environment.yml

$ conda activate survey_cleaner
```
You can install this package in development mode

```bash
$ pip install -e ".[docs]"
```

Run the test suite:
```bash
$ pytest tests/
```

## Build Documentation

### Building Documentation Locally

Install documentation dependencies
```bash
$ pip install -e ".[docs]"
```
Generate API documentation using quartodoc
```bash
quartodoc build
```
Preview the documentation
```bash
quarto preview
```
Render the final HTML output
```bash
quarto render
```
## Deploy Documentation

### Workflow Overview
| Workflow | Trigger | Purpose |
|----------|---------|---------|
| `build.yml` | Push/PR to main | Runs tests and builds package |
| `deploy.yml` | Push to main (after tests pass) | Deploys package to TestPyPI |
| `quartodoc.yml` | Push/PR to main | Builds API documentation with quartodoc |
| `quartodoc-publish.yml` | Push to main | Publishes documentation to GitHub Pages |

### Documentation Build Workflow

The `quartodoc.yml` workflow automatically:

1. Checks out the repository

2. Sets up Python environement

3. Installs package with Document dependencies

4. Runs `quartodoc build` to generate API docs

5. Validates the documentation build


### Documentation Publish Workflow
The `quartodoc-publish.yml` workflow automatically

1. Builds the documentation using Quarto

2. Deploys to GitHub Pages when changes are pushed to `main`

3. Makes documentation available to GitHub Pages URL

### Viewing Published Documentation
Once deployed, documentation is available at:
   - GitHub Pages: <https://ubc-mds.github.io/DSCI_524_group35_survey_cleaner/>

## Contributing
Interested in contributing? Check out the [contributing guidelines](CONTRIBUTING.md). Please note that this project is released with a [Code of Conduct](CODE_OF_CONDUCT.md). By contributing to this project, you agree to abide by its terms.

## Contributors
Natalie Truesdell, Amanpreet Binepal, Jay Li, Junli

## Copyright

- Copyright © 2026 Natalie Truesdell, Amanpreet Binepal, Jay Li, Junli.
- Free software distributed under the [MIT License](./LICENSE).
