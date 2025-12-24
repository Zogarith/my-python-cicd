import os
import unittest

# IMPORTANT: Set the test database URL BEFORE importing the app
# GitHub Actions maps the postgres service to localhost:5432
os.environ['postgresql://postgresql://my_cicd_db_user:dup6U837TMSvMAosp1Vd1tCLOtEoc8rx@dpg-d55o1iumcj7s73ff6320-a/my_cicd_db'] = 'postgres://user:pass@localhost:5432/myapp'

from app import app

class TestFlaskapp(unittest.TestCase):
    def setUp(self):
        # Create a test client
        self.app = app.test_client()
        self.app.testing = True

    def test_home_status_code(self):
        # This will now hit the real Postgres service in GitHub Actions
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)
        print("Integration Test Passed: App reached the Database!")

if __name__ == '__main__':
    unittest.main()