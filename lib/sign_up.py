from lib.database_connection import DatabaseConnection
import hashlib

class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def create(self, name, email, password):
        # Hash the password
        binary_password = password.encode("utf-8")
        hashed_password = hashlib.sha256(binary_password).hexdigest()

        # Store the email and hashed password in the database
        self._connection.execute(
            'INSERT INTO users (name, email, password) VALUES (%s, %s, %s)',
            [name, email, hashed_password])
        
        #def generate_errors(self):
        #errors = []
        #if self.title == None or self.title == "":
        #    errors.append("Title can't be blank")
        #if self.author_name == None or self.author_name == "":
        #    errors.append("Author name can't be blank")
        #if len(errors) == 0:
        #    return None
        #else:
        #    return ", ".join(errors)

    def get_userid(self, email, password_attempt):
        # Hash the password attempt
        binary_password_attempt = password_attempt.encode("utf-8")
        hashed_password_attempt = hashlib.sha256(binary_password_attempt).hexdigest()

        User_ID = self._connection.execute(
            'SELECT id FROM users WHERE email = %s AND password = %s',
            [email, hashed_password_attempt])[0]
        User_ID = User_ID.get('id')
        
        return User_ID

    def get_username(self, email, password_attempt):
        binary_password_attempt = password_attempt.encode("utf-8")
        hashed_password_attempt = hashlib.sha256(binary_password_attempt).hexdigest()

        name = self._connection.execute(
            'SELECT name FROM users WHERE email = %s AND password = %s',
            [email, hashed_password_attempt])[0]
        name =name.get('name')

        return name

    def check_password(self, email, password_attempt):
        # Hash the password attempt
        binary_password_attempt = password_attempt.encode("utf-8")
        hashed_password_attempt = hashlib.sha256(binary_password_attempt).hexdigest()

        # Check whether there is a user in the database with the given email
        # and a matching password hash, using a SELECT statement.
        rows = self._connection.execute(
            'SELECT * FROM users WHERE email = %s AND password = %s',
            [email, hashed_password_attempt])

        # If that SELECT finds any rows, the password is correct.
        return len(rows) > 0
    