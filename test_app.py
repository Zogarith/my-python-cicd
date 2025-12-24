import unittest
from app import app

class TestFlaskapp(unittest.TestCase):
    def setUp(self):
        # Create a test client for the app
        self.app = app.test_client()
        self.app.testing = True

    def test_home_status_code(self):
        # Sends an HTTP GET request to the index page
        result = self.app.get('/')
        # Asserts that the page returns a 200 OK status
        self.assertEqual(result.status_code, 200)

if __name__ == '__main__':
    unittest.main()