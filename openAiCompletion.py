import openai

class openAiCompletion:
    def __init__(self, api_key, engine="text-davinci-003"):
        """
        Initialize the openAICompletion class.

        Args:
            api_key (str): OpenAI API key for authentication.
            engine (str, optional): The engine to use for text generation. Default is "text-davinci-003".

        Constructor used to set the OpenAI API key and the default engine for text generation.
        """
        openai.api_key = api_key
        self.engine = engine

    def generate_response(self, prompt, max_tokens=2048, n=1, stop=None, temperature=0.7):
        """
        Generate a text response using the OpenAI Completion API.

        Args:
            prompt (str): Prompt for text generation.
            max_tokens (int, optional): Maximum number of tokens in the generated text. Default is 2048.
            n (int, optional): Number of alternative completions to generate. Default is 1.
            stop (str or list, optional): Stop sequence(s) to limit the generated text. Default is None.
            temperature (float, optional): Sampling temperature for controlling randomness. Default is 0.7.

        Returns:
            str: The generated text response.

        This method calls the OpenAI Completion API to generate text based on the provided prompt
        and other parameters. The generated text is returned as a string.
        """

        completion = openai.Completion.create(
            engine=self.engine,
            prompt=prompt,
            max_tokens=max_tokens,
            n=n,
            stop=stop,
            temperature=temperature
        )
        return completion.choices[0].text

