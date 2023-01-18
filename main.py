
import os
import openai
import logging
from openAiCompletion import openAiCompletion

def main():

    client = openAiCompletion(os.getenv('OPENAI_KEY') )

    # Configure logging
    logging.basicConfig(filename="error.log", level=logging.ERROR)

    while True:
        # Prompt for the prompt
        print ("\n\nHow can I help you today?")
        print ("Leave input empty and press 'Return' to exit.\n\n")
        prompt = str(input())

        if prompt == "":
            break
        
        try:
            response = client.generate_response(prompt)
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
            print("An error occurred, please try again.")

if __name__ == "__main__":
    main()
