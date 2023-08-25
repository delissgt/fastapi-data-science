from datetime import date, datetime

from pydantic import BaseModel, validator, field_validator


class Person(BaseModel):
    first_name: str
    last_name: str
    birthdate: date

    @field_validator("birthdate") # validatos expects the name of the argument to validate
    def valid_birthdate(cls, v: date):  # cls = class itself , v = value to validate
        delta = date.today() - v
        age = delta.days / 365
        if age > 120:
            raise ValueError("You seem a bit too old!!")
        print("v", v)
        return v


person = Person(first_name="name", last_name="last", birthdate=datetime(2012, 12, 12))
print(f"person {person.valid_birthdate(person.birthdate)}")
print(f"personnnnn {person}")
