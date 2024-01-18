import unittest
from unittest.mock import Mock, patch
from lib.sign_up import *

class TestUserRepository(unittest.TestCase):

    def setUp(self):
        # Mocking the database connection for testing
        self.mock_connection = Mock()

        # Creating an instance of UserRepository with the mocked connection
        self.user_repository = UserRepository(self.mock_connection)

    def test_create_user(self):
        name = "name"
        email = "test@example.com"
        password = "password123"

        # Mocking hashlib.sha256 for consistent hashing in the test
        with patch('hashlib.sha256') as mock_sha256:
            mock_hexdigest = mock_sha256.return_value.hexdigest
            mock_hexdigest.return_value = "hashed_password"

            # Calling the create method
            self.user_repository.create(name, email, password)

            # Verifying that the execute method was called with the correct arguments
            self.mock_connection.execute.assert_called_once_with(
                'INSERT INTO users (name, email, password) VALUES (%s, %s, %s)',
                [name, email, "hashed_password"])

    def test_check_password(self):
        email = "test@example.com"
        password_attempt = "password123"

        # Mocking hashlib.sha256 for consistent hashing in the test
        with patch('hashlib.sha256') as mock_sha256:
            mock_hexdigest = mock_sha256.return_value.hexdigest
            mock_hexdigest.return_value = "hashed_password_attempt"

            # Mocking the execute method to return a row for the SELECT statement
            self.mock_connection.execute.return_value = [(email, "hashed_password_attempt")]

            # Calling the check_password method
            result = self.user_repository.check_password(email, password_attempt)

            # Verifying that the execute method was called with the correct arguments
            self.mock_connection.execute.assert_called_once_with(
                'SELECT * FROM users WHERE email = %s AND password = %s',
                [email, "hashed_password_attempt"])

            # Verifying that the method returns True when the password is correct
            self.assertTrue(result)

    def test_check_password_wrong_password(self):
        email = "test@example.com"
        password_attempt = "wrong_password"

        # Mocking hashlib.sha256 for consistent hashing in the test
        with patch('hashlib.sha256') as mock_sha256:
            mock_hexdigest = mock_sha256.return_value.hexdigest
            mock_hexdigest.return_value = "hashed_wrong_password_attempt"

            # Mocking the execute method to return an empty row for the SELECT statement
            self.mock_connection.execute.return_value = []

            # Calling the check_password method
            result = self.user_repository.check_password(email, password_attempt)

            # Verifying that the execute method was called with the correct arguments
            self.mock_connection.execute.assert_called_once_with(
                'SELECT * FROM users WHERE email = %s AND password = %s',
                [email, "hashed_wrong_password_attempt"])

            # Verifying that the method returns False when the password is incorrect
            self.assertFalse(result)

    def test_get_userId(self):
        email = "test@example.com"
        password_attempt = "password123"

        # Mocking hashlib.sha256 for consistent hashing in the test
        with patch('hashlib.sha256') as mock_sha256:
            mock_hexdigest = mock_sha256.return_value.hexdigest
            mock_hexdigest.return_value = "hashed_password_attempt"

            # Mocking the execute method to return a row for the SELECT statement
            self.mock_connection.execute.return_value = [{'id': 4}]

            # Calling the check_password method
            result = self.user_repository.get_userid(email, password_attempt)

            # Verifying that the execute method was called with the correct arguments
            self.mock_connection.execute.assert_called_once_with(
                'SELECT id FROM users WHERE email = %s AND password = %s',
                [email, "hashed_password_attempt"])

            # Verifying that the method returns True when the password is correct
            assert result == 4