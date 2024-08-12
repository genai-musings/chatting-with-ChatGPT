from openai import OpenAI

class openAiCompletion:
    def __init__(self, api_key):
        """
        Initialize the openAICompletion class.

        Args:
            api_key (str): OpenAI API key for authentication.

        Constructor used to set the OpenAI API key for text generation.
        """
        self.client = OpenAI(api_key=api_key)

    def generate_response(self, model, prompt):
        """
        Generate a text response using the OpenAI Completion API.

        Args:
            model (str): Model to use
            prompt (str): Prompt for text generation.

        Returns:
            str: The generated text response.

        This method calls the OpenAI Completion API to generate text based on the provided prompt
        and other parameters. The generated text is returned as a string.
        """

        completion = self.client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
        )
        return completion.choices[0].message.content

