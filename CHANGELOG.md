# Chatting With ChatGPT

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.8.4] - 2024-11-11

- [CHANGED] Updates to README.md

## [1.8.3] - 2024-09-03

- [CHANGED] Updates to README.md
- [ADDED] Improved error handling if OPENAI_API_KEY environment variable is not set
- [FIXED] Vulnerability in library libaom3 used docker image as reported by Trivy => - CVE-2024-5171  │ CRITICAL
- [FIXED] Vulnerability in library linux-libc-dev used docker image as reported by Trivy

## [1.8.2] - 2024-08-14

- [FIXED] Updated code and documentation to use OPENAI_API_KEY environment variable
- [FIXED] Workaround for mocking issue with some unit tests

## [1.8.1] - 2024-08-13

- [FIXED] Vulnerability in docker image reported by Trivy => - CVE-2024-7348 │ HIGH

## [1.8.0] - 2024-08-12

- [ADDED] Upgraded to [version 1 of the OpenAI API](https://github.com/openai/openai-python/discussions/742)

## [1.7.0] - 2024-08-09

- [ADDED] Safety GitHub Action workflow to check Python dependencies for known security vulnerabilities.
- [ADDED] Trivy scan of the Docker image for vulnerabilities
- [FIXED] Vulnerability in docker imaged reported by Trivy

## [1.6.3] - 2023-12-08

- [CHANGED] Upgraded model to gpt-3.5-turbo-instruct.

## [1.6.2] - 2023-10-20

- [ADDED] Documentation in the form of code comments.

## [1.6.1] - 2023-10-17

- [CHANGED] Updates to README.md
- [CHANGED] Updates to Dockerfile maintainers and CODEOWNERS
- [ADDED] Ensured docker image pushed to Docker Hub before README.md

## [1.6.0] - 2023-09-19

- [ADDED] GitHub Action Linting to Super-Linter workflow
- [ADDED] Shell Script Linting to Super-Linter workflow
- [ADDED] Maintainer and description labels to Dockerfile
- [ADDED] Workflow to automatically update Image description on Docker Hub with contents of README.md
- [CHANGED] Updates to README.md

## [1.5.2] - 2023-08-04

- [FIXED] 403 error when validating OpenAI Keys page link from Markdown link checking action.

## [1.5.1] - 2023-08-03

- [FIXED] Issue with docker image tagging.

## [1.5.0] - 2023-07-21

- [ADDED] Dockerized application.

## [1.4.0] - 2023-07-09

- [ADDED] Adding CI related GitHub Actions

## [1.3.4] - 2023-06-20

- [FIXED] Permissions error in greetings.yml

## [1.3.3] - 2023-06-20

- [ADDED] Markdown link checker GitHub action
- [ADDED] JSON validation via SuperLinter
- [CHANGED] Replaced pylint and yamllint GitHub actions with SuperLinter GitHub action

## [1.3.2] - 2023-06-09

- [CHANGED] Fixed location of pull_request_template

## [1.3.1] - 2023-06-09

- [ADDED] License

## [1.3.0] - 2023-06-07

- [ADDED] GitHub Issue & PR Templates and associated GitHub Actions.
- [CHANGED] Moved tests to dedicated tests folder

## [1.2.0] - 2023-06-04

- [CHANGED] Unit tests also run for pull requests
- [ADDED] Markdown spelling check GitHub action
- [ADDED] Python Linting GitHub action
- [ADDED] YAML Linting GitHub action
- [ADDED] CONTRIBUTING.md

## [1.1.0] - 2023-05-24

- [ADDED] CHANGELOG.md
- [ADDED] GitHub Action to run unit tests

## [1.0.0] - 2023-01-18

- [ADDED] Initial Release

