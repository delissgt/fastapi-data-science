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

    def name_dict(self):
        return self.model_dump(include={"first_name", "last_name"})


person = Person(
    first_name="John",
    last_name="Doe",
    gender=Gender.MALE,
    birthday="1991-01-01",
    interests=["travel", "sports"],
    address={
        "street_address": "12 squivel Street",
        "postal_code": "42123",
        "city": "TownDown City",
        "country": "US",
    }
)

# WORKING
# person_dict = person.dict() # deprecated use model_dump()
# person_dict = person.__dict__  # Error Address is not subscriptable
person_dict = person.model_dump()
print("person", person_dict)
print("name", person_dict["first_name"])
print("address", person_dict["address"]["street_address"])

# -------- include and exclude fields
person_include = person.model_dump(include={"first_name", "last_name"})
print("include", person_include)

person_exclude = person.model_dump(exclude={"birthday", "interests"})
print("exclude", person_exclude)

# nested structure include and exclude sub-fields
person_nested_include = person.model_dump(include={
    "first_name": ...,
    "last_name": ...,
    "address": {"city", "country"},
})

print("person nested include", person_nested_include)
# {'first_name': 'John', 'last_name': 'Doe', 'address': {'city': 'TownDown City', 'country': 'US'}}

# method for conversion data
print("name dict", person.name_dict())
