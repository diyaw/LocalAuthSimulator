import unittest
import requests


class TestServerInteractions(unittest.TestCase):
    def test_authorization_response(self):
        # Test that the Authorization Server responds with a 200 status code
        response = requests.get('http://localhost:8000')
        self.assertEqual(response.status_code, 200)
        print("Authorization Server Test 1: Status Code - Passed")

        # Test that the Authorization Server response
        expected_message = 'Authorization Server: You are authorized.'
        self.assertEqual(response.text, expected_message)
        print("Authorization Server Test 2: Response Message - Passed")

    def test_resource_api_response(self):
        # Test that the Resource API responds with a 200 status code
        response = requests.get('http://localhost:9000')
        self.assertEqual(response.status_code, 200)
        print("Resource API Test 1: Status Code - Passed")

        # Test that the Resource API response contains the expected message
        expected_message = 'Resource API: Here is your requested data.'
        self.assertEqual(response.text, expected_message)
        print("Resource API Test 2: Response Message - Passed")


if __name__ == '__main__':
    unittest.main()
