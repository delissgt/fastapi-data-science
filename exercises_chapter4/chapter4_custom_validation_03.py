# how to transform a string with values separated by a comma into a proper list.

from typing import List

from pydantic import BaseModel, validator


class Model(BaseModel):
    values: List[int]

    @validator("values", pre=True)
    def split_string_values(cls, v):
        if isinstance(v, str):
            return v.split(",")
        return v


m = Model(values="1,2,3")
print("valuesssss", m.values)  # [1, 2, 3]
