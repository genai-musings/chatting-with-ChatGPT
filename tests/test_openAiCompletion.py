"""OpenAI Completion class unit tests."""
import os
import sys 
import unittest
from unittest.mock import patch, MagicMock
import openai
from openAiCompletion import openAiCompletion

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class TestOpenAiCompletion(unittest.TestCase):
    def setUp(self):
        self.api_key = 'api_key'
        self.engine = 'engine'
        self.client = openAiCompletion(api_key=self.api_key, engine=self.engine)

    # This test case tests that the generate_response method returns
    # the correct response when called with a valid prompt.
    # Using the patch decorator to mock the openai.Completion.create method.
    @patch('openai.Completion.create')
    def test_generate_response(self, mock_create):
        # set up mock return value
        mock_response = MagicMock()
        mock_response.choices = [MagicMock(text='mock_response')]
        mock_create.return_value = mock_response

        # test generate response
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
    # Using the patch decorator to mock the openai.Completion.create method.
    @patch('openai.Completion.create')
    def test_generate_response_with_invalid_api_key(self, mock_create):
        openai.api_key = None
        self.client = openAiCompletion(api_key=None, engine=self.engine)
        mock_create.side_effect = openai.OpenAIError('Invalid API key')
        with self.assertRaises(openai.OpenAIError) as cm:
            self.client.generate_response('mock_prompt')
        the_exception = cm.exception
        self.assertEqual(str(the_exception), 'Invalid API key')

if __name__ == '__main__':
    unittest.main()
