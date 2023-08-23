# Don’t assign default values for dynamic types such as datetimes.
from pydantic import BaseModel

import time
from datetime import datetime


class Model(BaseModel):
    # Don't do this.
    # This example shows you why it doesn't work.
    d: datetime = datetime.now()


o1 = Model()
print(o1.d)

time.sleep(1)  # wait for a second

o2 = Model()
print(o2.d)

print(o1.d < o2.d) # False always same datetime value
