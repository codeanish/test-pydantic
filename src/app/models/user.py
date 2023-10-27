from pydantic import EmailStr, Field
from pydantic.dataclasses import dataclass

@dataclass
class User:
    name: str = Field(description="Full name", example='John Doe', min_length=3, max_length=50)
    email:  EmailStr = Field(description="Email Address", examples=['me@example.com'])
    age: int = Field(description="Age of the user in years", ge=18, lt=100)