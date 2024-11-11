"""main program entry point"""
import os
import sys
import logging
import openai

from openAiCompletion import openAiCompletion

def main():

    # Check if the OPENAI_API_KEY environment variable is set
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("Error: The environment variable 'OPENAI_API_KEY' is not set. Please set it before continuing.")
        print("       Refer to the README.md for instructions on how to create an OpenAI API Key.")
        sys.exit(1)  # Exit the application with a non-zero status code

    # If the environment variable is set, continue with the application
    client = openAiCompletion(api_key)

    # Configure logging
    logging.basicConfig(filename="error.log", level=logging.ERROR)

    while True:
        # Prompt for the prompt
        print ("\n\nHow can I help you today?")
        print ("Leave input empty and press 'Return' to exit.\n\n")
        prompt = str(input())

        if prompt == "":
            sys.exit(0)

        try:
            response = client.generate_response("gpt-4", prompt)
            print(response)
        except openai.OpenAIError as e:
            # Handle the exception
            # Log the error message and exception type
            logging.error(f"OpenAIError: {e}", exc_info=True)
            print(f"Error: {e}")
        except Exception as e:
            # Handle the exception
            # Log the error message and exception type
            logging.error(f"Error: {e}", exc_info=True)
            print(f"An error occurred, please try again:  {e}")

if __name__ == "__main__":
    main()
