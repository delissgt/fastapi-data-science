# fields can be Pydantic models themselves, allowing you to have sub-objects

from enum import Enum
from typing import List
from datetime import date

from pydantic import BaseModel


class Gender(str, Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    NON_BINARY = "NON BINARY"


class Address(BaseModel):
    street_address: str
    postal_code: str
    city: str
    country: str


class Person(BaseModel):
    first_name: str
    last_name: str
    gender: Gender
    birthday: date
    interests: List[str]
    address: Address
