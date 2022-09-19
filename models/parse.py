from pydantic import BaseModel, validator


class ParseModel(BaseModel):
    arg1: str
    arg2: int

    @validator('arg1')
    def is_palindrome_validator(cls, v, values, **kwargs):
        if v and not v == v[::-1]:
            raise ValueError("String is not a palindrome.")
        return v

    @validator('arg2')
    def even_digit_validator(cls, v, values, **kwargs):
        if v and not v % 2 == 0:
            raise ValueError("Odd number.")
        return v
