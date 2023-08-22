from typing import Dict

from exercises_chapter3.project_base.models.user import User
from exercises_chapter3.project_base.models.post import Post


class DummyDatabase:
    users: Dict[int, User] = {}
    posts: Dict[int, Post] = {}


db = DummyDatabase()
