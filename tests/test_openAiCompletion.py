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
        self.api_key = 'mock_api_key'
        self.engine = 'gpt-4'
        self.client = openAiCompletion(api_key=self.api_key)
"""
    @patch('openAiCompletion.OpenAI')  # Patch the method correctly
    def test_generate_response(self, mock_create):
        # Set up a mock return value for openai.ChatCompletion.create
        mock_response = MagicMock()
        mock_response.choices = [MagicMock(message=MagicMock(content='mock_response'))]
        mock_create.return_value = mock_response

        # Test the generate_response method
        response = self.client.generate_response(self.engine, 'mock_prompt')
        self.assertEqual(response, 'mock_response')

        # Ensure the method was called with correct parameters
        mock_create.assert_called_once_with(
            model=self.engine,
            messages=[{
                "role": "user",
                "content": 'mock_prompt',
            }]
        )
"""
    @patch('openAiCompletion.OpenAI')
    def test_generate_response_with_invalid_api_key(self, mock_openai):
        # Simulate an OpenAIError when calling openai.Completion.create
        mock_client = MagicMock()
        mock_openai.return_value = mock_client
        mock_client.chat.completions.create.side_effect = openai.OpenAIError(
            'Error code: 401 - {"error": {"message": "Incorrect API key provided: mock_api_key. '
            'You can find your API key at https://platform.openai.com/account/api-keys.", '
            '"type": "invalid_request_error", "param": None, "code": "invalid_api_key"}}'
        )

        # Test that an OpenAIError is raised with the expected message
        with self.assertRaises(openai.OpenAIError) as cm:
            self.client.generate_response(self.engine, 'mock_prompt')
        the_exception = cm.exception
        self.assertIn('Incorrect API key provided', str(the_exception))

if __name__ == '__main__':
    unittest.main()
