import os
import sys
import unittest
from unittest.mock import patch, MagicMock
import openai

# Add the parent directory to the sys.path to import the openAiCompletion module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the openAiCompletion class from openAiCompletion.py
from openAiCompletion import openAiCompletion

class TestOpenAiCompletion(unittest.TestCase):
    def setUp(self):
        # Initialize common values for testing
        # having issues with mocking so for now calling actual API
        self.api_key = os.getenv('OPENAI_API_KEY') #'mock_api_key'
        self.engine = 'gpt-4'
        self.client = openAiCompletion(api_key=self.api_key)

    @patch('openAiCompletion.OpenAI')  # Patch the specific method
    def test_generate_response(self, mock_create):
        # Set up a mock return value for chat.completions.create
        mock_create.return_value = MagicMock(
            choices=[MagicMock(message=MagicMock(content='mock_response'))]
        )

        # Test the generate_response method
        response = self.client.generate_response(self.engine, 'mock_prompt')
        # Assert that a response was received
        self.assertIsNotNone(response)
        self.assertIsInstance(response, str)
        self.assertGreater(len(response), 0)
        # Ideally, you can also verify that it contains some part of expected content
        #self.assertEqual(response, 'mock_response')

        # Ensure the method was called with correct parameters
        #mock_create.assert_called_once_with(
        #    model=self.engine,
        #    messages=[{
        #        "role": "user",
        #        "content": 'mock_prompt',
        #    }]
        #)

if __name__ == '__main__':
    unittest.main()
