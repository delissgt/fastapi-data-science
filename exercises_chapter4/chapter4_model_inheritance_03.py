from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    content: str

    def excerpt(self) -> str:
        return f"{self.content[:140]}..."


my_post = PostBase(title="my-title", content="qqaazzwwssxxeeddccrrffvvttggbbyyhhnnuujjmmiikkoollppññqwertyuiopasdfghjklñzxcvbnm12345678900987654321qazwsxedcrfvtgbyhnujmikolpñ11223344556677889900998877665544332211qqaazzwwssxx")

print("mp", my_post)

print(my_post.title)
print("mmpp", my_post.excerpt())

