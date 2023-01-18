# chatting-with-ChatGPT

Repository for chatting with ChatGPT

 This respository contains Python code and associated unit tests which uses the OpenAI API to perform language generation. The code takes the input from the user and generates a response using the "text-davinci-003" engine.

## To run program

Key is passed to program via an environment variable

```shell
export OPENAI_KEY="Your OpenAI key"
python main.py
```

## To run unit tests

```shell
pytest
```