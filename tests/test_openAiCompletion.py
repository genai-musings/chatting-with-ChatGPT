"""OpenAI Completion class unit tests."""
import os
import sys
import unittest
from unittest.mock import patch, MagicMock
import openai

# Add the parent directory to the sys.path to import the openAiCompletion module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Import the openAiCompletion class from openAiCompletion.py
from openAiCompletion import openAiCompletion

class TestOpenAiCompletion(unittest.TestCase):
    def setUp(self):
        # Initialize common values for testing
        self.api_key = 'api_key'
        self.engine = 'engine'
        self.client = openAiCompletion(api_key=self.api_key, engine=self.engine)

    # This test case tests that the generate_response method returns
    # the correct response when called with a valid prompt.
    # It uses the patch decorator to mock the openai.Completion.create method.
    @patch('openai.Completion.create')
    def test_generate_response(self, mock_create):
        # Set up a mock return value for openai.Completion.create
        mock_response = MagicMock()
        mock_response.choices = [MagicMock(text='mock_response')]
        mock_create.return_value = mock_response

        # Test the generate_response method
        response = self.client.generate_response('mock_prompt')
        self.assertEqual(response, 'mock_response')
        mock_create.assert_called_once_with(
            engine=self.engine,
            prompt='mock_prompt',
            max_tokens=2048,
            n=1,
            stop=None,
            temperature=0.7
        )

    # This test case checks that the generate_response method raises
    # an openai.OpenAIError when the API key is invalid.
    # It uses the patch decorator to mock the openai.Completion.create method.
    @patch('openai.Completion.create')
    def test_generate_response_with_invalid_api_key(self, mock_create):
        # Set the API key to None to simulate an invalid key
        openai.api_key = None
        self.client = openAiCompletion(api_key=None, engine=self.engine)
        # Simulate an OpenAIError when calling openai.Completion.create
        mock_create.side_effect = openai.OpenAIError('Invalid API key')

        # Test that an OpenAIError is raised with the expected message
        with self.assertRaises(openai.OpenAIError) as cm:
            self.client.generate_response('mock_prompt')
        the_exception = cm.exception
        self.assertEqual(str(the_exception), 'Invalid API key')

if __name__ == '__main__':
    unittest.main()
