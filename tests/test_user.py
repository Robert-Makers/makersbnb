from lib.user import User

def test_user_constructs():
    user = User(1, 'John', 'email@gmail.com', 'password')
    assert user.id == 1
    assert user.name == 'John'
    assert user.password == 'password'
    assert user.email == 'email@gmail.com'

def test_format():
    user = User(1, 'John', 'email@gmail.com', 'password')
    assert str(user) == "User(1, 'John', 'email@gmail.com', 'password')"