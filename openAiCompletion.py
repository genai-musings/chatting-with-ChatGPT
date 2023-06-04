"""Open AI Completion class."""
import openai

class openAiCompletion:
    def __init__(self, api_key, engine="text-davinci-003"):
        openai.api_key = api_key
        self.engine = engine

    def generate_response(self, prompt, max_tokens=2048, n=1, stop=None, temperature=0.7):
        # The completions endpoint can be used for a wide variety of tasks.
        # It provides a simple but powerful interface to any of our models.
        # You input some text as a prompt, and the model will generate a text
        # completion that attempts to match whatever context or pattern you gave it.
        # API Documentation -> https://beta.openai.com/docs/guides/completion
        completion = openai.Completion.create(
            engine=self.engine,
            prompt=prompt,
            max_tokens=max_tokens,
            n=n,
            stop=stop,
            temperature=temperature
        )
        return completion.choices[0].text
