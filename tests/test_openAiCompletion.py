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
        # Use a mock API key for testing
        self.mock_api_key = 'mock_api_key'
        os.environ['OPENAI_API_KEY'] = self.mock_api_key
        self.client = openAiCompletion(api_key=self.mock_api_key)

    @patch('openai.Completion.create')
    def test_generate_response(self, mock_create):
        # Set up a mock return value for openai.Completion.create
        mock_response = MagicMock()
        mock_response.choices = [MagicMock(text='mock_response')]
        mock_create.return_value = mock_response

        # Test the generate_response method
        response = self.client.generate_response('gpt-4', 'mock_prompt')
        self.assertEqual(response, 'mock_response')
        mock_create.assert_called_once_with(
            model="gpt-4",
            prompt='mock_prompt'
        )

    @patch('openai.Completion.create')
    def test_generate_response_with_invalid_api_key(self, mock_create):
        # Simulate an OpenAIError when calling openai.Completion.create
        mock_create.side_effect = openai.OpenAIError('Invalid API key')

        # Test that an OpenAIError is raised with the expected message
        with self.assertRaises(openai.OpenAIError) as cm:
            self.client.generate_response('gpt-4', 'mock_prompt')
        the_exception = cm.exception
        self.assertEqual(str(the_exception), 'Invalid API key')

if __name__ == '__main__':
    unittest.main()
