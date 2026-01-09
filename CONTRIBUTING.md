# Contributing

Contributions of all kinds are welcome here, and they are greatly appreciated!
Every little bit helps, and credit will always be given.

## Example Contributions

You can contribute in many ways, for example:

* [Report bugs](#report-bugs)
* [Fix Bugs](#fix-bugs)
* [Implement Features](#implement-features)
* [Write Documentation](#write-documentation)
* [Submit Feedback](#submit-feedback)

### Report Bugs

Report bugs at https://github.com/UBC-MDS/DSCI_524_group35_survey_cleaner/issues.

**If you are reporting a bug, please follow the template guidelines. The more
detailed your report, the easier and thus faster we can help you.**

### Fix Bugs

Look through the GitHub issues for bugs. Anything labelled with `bug` and
`help wanted` is open to whoever wants to implement it. When you decide to work on such
an issue, please assign yourself to it and add a comment that you'll be working on that,
too. If you see another issue without the `help wanted` label, just post a comment, the
maintainers are usually happy for any support that they can get.

### Implement Features

Look through the GitHub issues for features. Anything labelled with
`enhancement` and `help wanted` is open to whoever wants to implement it. As
for [fixing bugs](#fix-bugs), please assign yourself to the issue and add a comment that
you'll be working on that, too. If another enhancement catches your fancy, but it
doesn't have the `help wanted` label, just post a comment, the maintainers are usually
happy for any support that they can get.

### Write Documentation

survey_cleaner could always use more documentation, whether as
part of the official documentation, in docstrings, or even on the web in blog
posts, articles, and such. Just
[open an issue](https://github.com/UBC-MDS/DSCI_524_group35_survey_cleaner/issues)
to let us know what you will be working on so that we can provide you with guidance.

### Submit Feedback

The best way to send feedback is to file an issue at
https://github.com/UBC-MDS/DSCI_524_group35_survey_cleaner/issues. If your feedback fits the format of one of
the issue templates, please use that. Remember that this is a volunteer-driven
project and everybody has limited time.

## Get Started!

Ready to contribute? Here's how to set up survey_cleaner for
local development.

1. Fork the https://github.com/UBC-MDS/DSCI_524_group35_survey_cleaner
   repository on GitHub.
2. Clone your fork locally (*if you want to work locally*)

    ```shell
    git clone git@github.com:your_name_here/survey_cleaner.git
    ```

3. [Install hatch](https://hatch.pypa.io/latest/install/).

4. Create a branch for local development using the default branch (typically `main`) as a starting point. Use `fix` or `feat` as a prefix for your branch name.

    ```shell
    git checkout main
    git checkout -b fix-name-of-your-bugfix
    ```

    Now you can make your changes locally.

5. When you're done making changes, apply the quality assurance tools and check
   that your changes pass our test suite. This is all included with tox

    ```shell
    hatch run test:run
    ```

6. Commit your changes and push your branch to GitHub. Please use [semantic
   commit messages](https://www.conventionalcommits.org/).

    ```shell
    git add .
    git commit -m "fix: summarize your changes"
    git push -u origin fix-name-of-your-bugfix
    ```

7. Open the link displayed in the message when pushing your new branch in order
   to submit a pull request.

### Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put your
   new functionality into a function with a docstring.
3. Your pull request will automatically be checked by the full test suite.
   It needs to pass all of them before it can be considered for merging.

## Team Collaboration Workflow

This project follows the [GitHub Flow](https://guides.github.com/introduction/flow/) workflow for team collaboration. All team members are expected to follow these practices:

### Branch-Based Development

1. **Always create a new branch** for each feature or bug fix
   - Branch from the `main` branch
   - Use descriptive branch names (e.g., `feature/normalize-binary`, `fix/typo-in-readme`)

2. **Never commit directly to `main`**
   - All changes must go through a pull request
   - This ensures code review and maintains code quality

### Commit Message Standards

Write clear, meaningful commit messages that will be reviewed as part of the project evaluation:

**Good commit messages:**
- Use present tense, imperative mood (e.g., "Add function" not "Added function")
- First line: concise summary (50 characters or less)
- Add detailed description after a blank line if needed

**Examples:**
```
Add normalize_binary function with full docstring

- Implements conversion from True/False, Yes/No, T/F to 0/1
- Includes parameter validation
- Handles case-insensitive string inputs
```

**Avoid vague messages like:**
- "update"
- "fix bug"
- "wip"

### Pull Request Process

1. **Create a descriptive PR**
   - Write a clear title and description
   - Link related issues using keywords (e.g., `Closes #5`)
   - Explain what changed and why

2. **Request review from at least one team member**
   - Every PR must be reviewed before merging
   - Reviewers should check:
     - Code quality and style
     - Test coverage
     - Documentation completeness
     - Adherence to project standards

3. **Address review feedback**
   - Respond to all comments
   - Make requested changes
   - Re-request review after updates

4. **Merge only after approval**
   - Wait for at least one approval
   - Ensure all CI checks pass
   - Delete the branch after merging

### Communication Guidelines

- **Use GitHub Issues for all project communication**
  - Don't use email or instant messaging for project discussions
  - This creates a transparent record for the entire team

- **Assign issues clearly**
  - Each issue should have one assigned person
  - If you want to work on an unassigned issue, comment and assign yourself

- **Use project boards and milestones**
  - Move issues through the board as you work on them
  - Associate issues with the appropriate milestone

### Equal Contribution

All team members are expected to contribute equally to:
- Code development
- Documentation
- Code reviews
- Project management

Contribution will be evaluated through:
- Number of commits
- Number of pull request reviews
- Participation in GitHub issues

## Code Quality Standards

### Documentation

- All functions must have complete docstrings following NumPy style
- Include:
  - Brief description
  - Parameters with types
  - Returns with type
  - Examples

### Testing

- Write tests for all new functions
- Aim for high test coverage
- Run tests before submitting PR: `hatch run test:run`

### Code Style

- Follow PEP 8 style guidelines
- Use descriptive variable names
- Keep functions focused and concise
