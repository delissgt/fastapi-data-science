from typing import Optional

from pydantic import BaseModel


class UserProfile(BaseModel):
    nickname: str
    location: Optional[str] = None
    subscribed_newsletter: bool = False  # True


user = UserProfile(nickname="jojo")
user_ful = UserProfile(nickname="jooj", location="aaa", subscribed_newsletter=True)
print("user", user)
print("user_ful", user_ful)
#  nickname='jojo' location=None subscribed_newsletter=True

