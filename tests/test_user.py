from pydantic import ValidationError
import pytest
from src.app.models.user import User


def test_user_empty_email():
    with pytest.raises(ValidationError):
        User(name="John Doe", email = "", age=19)

def test_user_null_email():
    with pytest.raises(ValidationError):
        User(name="John Doe", age=19, email="test")

def test_user_too_young():
    with pytest.raises(ValidationError):
        User(name="John Doe", email = "test@example.com", age=17)
    
def test_valid_user():
    user = User(name="John Doe", email = "test@example.com", age=19)
    assert user.age == 19
    assert user.name == "John Doe"
    assert user.email == "test@example.com"

def test_user_invalid_name():
    with pytest.raises(ValidationError):
        User(name="Jo", email = "test@example.com", age=19)