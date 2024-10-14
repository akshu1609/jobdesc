import unittest
from unittest.mock import patch, MagicMock
import openai  # Add this import for RateLimitError
from utils.main import generate_job_description  # Adjust the import based on your file structure

class TestJobDescriptionGenerator(unittest.TestCase):

    @patch('openai.ChatCompletion.create')
    def test_generate_job_description(self, mock_create):
        # Setup the mock to return a specific response
        mock_response = MagicMock()
        mock_response.choices = [MagicMock()]
        mock_response.choices[0].message = {'content': 'Sample Job Description'}
        mock_create.return_value = mock_response

        result = generate_job_description("Software Engineer", "Google", "Develop applications", "Python, JavaScript", "Mid-Level", "Formal")
        
        # Assert the result matches the mocked response
        self.assertEqual(result, "Sample Job Description")

    @patch('openai.ChatCompletion.create')
    def test_generate_job_description_rate_limit(self, mock_create):
        # Simulate a rate limit error
        mock_create.side_effect = [openai.error.RateLimitError("Rate limit exceeded"),
                                    MagicMock(choices=[MagicMock(message={'content': 'Sample Job Description'})])]
        
        # Here we expect it to return the mock description after handling the error
        result = generate_job_description("Software Engineer", "Google", "Develop applications", "Python, JavaScript", "Mid-Level", "Formal")
        self.assertEqual(result, "Sample Job Description")

if __name__ == '__main__':
    unittest.main()
