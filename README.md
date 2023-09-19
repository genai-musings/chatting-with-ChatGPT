# chatting-with-ChatGPT

[![License: MPL 2.0](https://img.shields.io/badge/License-MPL%202.0-brightgreen.svg)](https://opensource.org/licenses/MPL-2.0)
[![Bandit](https://github.com/genai-musings/chatting-with-ChatGPT/actions/workflows/bandit.yml/badge.svg)](https://github.com/genai-musings/chatting-with-ChatGPT/actions/new?category=security)
[![Super-Linter](https://github.com/genai-musings/chatting-with-ChatGPT/actions/workflows/linter.yml/badge.svg)](https://github.com/marketplace/actions/super-linter)
[![CodeQL](https://github.com/genai-musings/chatting-with-ChatGPT/workflows/CodeQL/badge.svg?branch=main)
[![Markdown Links Check](https://github.com/genai-musings/chatting-with-ChatGPT/actions/workflows/md-links.yml/badge.svg)](https://github.com/gaurav-nelson/github-action-markdown-link-check)
[![Spell-Checker](https://github.com/genai-musings/chatting-with-ChatGPT/actions/workflows/spellcheck.yaml/badge.svg)](https://github.com/rojopolis/spellcheck-github-actions)
[![Unit-Tests](https://github.com/genai-musings/chatting-with-ChatGPT/actions/workflows/test.yaml/badge.svg)](https://github.com/actions/setup-python)
[![Code-Coverage](https://github.com/genai-musings/chatting-with-ChatGPT/actions/workflows/coverage.yaml/badge.svg)](https://github.com/actions/setup-python)
[![Docker-Build-Push](https://github.com/genai-musings/chatting-with-ChatGPT/actions/workflows/docker-build-push.yml/badge.svg)](https://hub.docker.com/)
[![Docker-Push-README](https://github.com/genai-musings/chatting-with-ChatGPT/actions/workflows/docker-push-readme.yml/badge.svg)](https://hub.docker.com/)

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

## To build and run an instance of a Docker image locally.

The username and password for Docker Hub are stored as secrets this GitHub repository.

**Note:** To set up the secrets in your GitHub repository, go to the repository page, navigate to the "Settings" tab, and then select "Secrets" from the left menu. Add a secret named DOCKERHUB_USERNAME with the Docker Hub username to be used, and another secret named DOCKERHUB_PASSWORD with the Docker Hub password to be used.

### Build

Build the Docker image.

```shell
docker build -t chatting-with-chatgpt .
```

### Run

Run the Docker image as a container.

```shell
export OPENAI_KEY="Your OpenAI key"
docker run -it -e OPENAI_KEY= "Your OpenAI Key" chatting-with-chatgpt
```

## To pull and run an instance of the Docker image from Docker Hub

### Pull

```shell
docker pull <dockerhub-username>/chatting-with-chatgpt:<tag>
```

Replace <dockerhub-username> with your Docker Hub username and <tag> with the specific tag of the Docker image you want to pull.

### Run

```shell
export OPENAI_KEY="Your OpenAI key"
docker run -it -e OPENAI_KEY= "Your OpenAI Key" <dockerhub-username>/chatting-with-chatgpt:<tag>
```

## OpenAI API Reference

For more information on the API available see the [OpenAI API Reference Documentation](https://platform.openai.com/docs/api-reference).
