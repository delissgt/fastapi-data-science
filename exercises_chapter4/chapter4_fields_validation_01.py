from typing import Optional

from pydantic import BaseModel, Field, ValidationError


class Person(BaseModel):
    first_name: str = Field(..., min_length=3)  # required, should be at least 3 characters long
    last_name: str = Field(..., min_length=3)  # required, should be at least 3 characters long
    age: int = Field(None, ge=0, le=120)  # optional, should be an integer between 0 and 120

# the the field is required we use the ellipsis ...
