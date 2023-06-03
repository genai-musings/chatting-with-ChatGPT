# chatting-with-ChatGPT

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
