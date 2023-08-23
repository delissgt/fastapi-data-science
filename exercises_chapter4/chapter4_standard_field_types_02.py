#  Model using complex types like, lists, tuples, or datetime classes
from datetime import date
from enum import Enum
from typing import List

from pydantic import BaseModel, ValidationError


class Gender(str, Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    NON_BINARY = "NON BINARY"


class Person(BaseModel):
    first_name: str
    last_name: str
    gender: Gender  # We used Enum class as a type for the gender field. This allows us to specify a set of valid values
    birthdate: date  # We used the date class as a type for the birthday field
    interests: List[str]  # We defined interests as a list of strings

