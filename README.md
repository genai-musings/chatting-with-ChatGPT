# chatting-with-ChatGPT

[![License: MPL 2.0](https://img.shields.io/badge/License-MPL%202.0-brightgreen.svg)](https://opensource.org/licenses/MPL-2.0)
[![Bandit](https://github.com/tom-halpin/chatting-with-ChatGPT/actions/workflows/bandit.yml/badge.svg)](https://github.com/tom-halpin/chatting-with-ChatGPT/actions/new?category=security)
[![Super-Linter](https://github.com/tom-halpin/chatting-with-ChatGPT/actions/workflows/linter.yml/badge.svg)](https://github.com/marketplace/actions/super-linter)
[![CodeQL](https://github.com/tom-halpin/chatting-with-ChatGPT/workflows/CodeQL/badge.svg?branch=main)
[![Markdown Links Check](https://github.com/tom-halpin/chatting-with-ChatGPT/actions/workflows/md-links.yml/badge.svg)](https://github.com/gaurav-nelson/github-action-markdown-link-check)
[![Spell-Checker](https://github.com/tom-halpin/chatting-with-ChatGPT/actions/workflows/spellcheck.yaml/badge.svg)](https://github.com/rojopolis/spellcheck-github-actions)
[![Unit-Tests](https://github.com/tom-halpin/chatting-with-ChatGPT/actions/workflows/test.yaml/badge.svg)](https://github.com/actions/setup-python)
[![Code-Coverage](https://github.com/tom-halpin/chatting-with-ChatGPT/actions/workflows/coverage.yaml/badge.svg)](https://github.com/actions/setup-python)

Repository for chatting with ChatGPT.

 This repository contains Python code, and associated unit tests, which uses the OpenAI API to perform language generation. The code takes the input from the user and generates a response using the "text-davinci-003" engine.

## To run program

Your OpenAI key is passed to program via an environment variable

```shell
export OPENAI_KEY="Your OpenAI key"
python main.py
```

To generate an OpenAI key browse to [OpenAI API Keys](https://platform.openai.com/account/api-keys) and select "Create new secret key".


## To run unit tests

```shell
pytest
```

## OpenAI API Reference

For more information on the API available see the [OpenAI API Reference Documentation](https://platform.openai.com/docs/api-reference).
