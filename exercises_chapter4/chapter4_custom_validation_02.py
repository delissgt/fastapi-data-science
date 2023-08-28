from pydantic import BaseModel, EmailStr, ValidationError, root_validator, model_validator


class UserRegistration(BaseModel):
    email: EmailStr
    password: str
    password_confirmation: str

    # # @root_validator()
    @model_validator(mode='after')  # before, after , wrap(no use)
    def passwords_match(cls, values):
        print("Values", values)
        print("Value---s", type(values))
        password = values.password
        password_confirmation = values.password_confirmation

        if password != password_confirmation:
            raise ValidationError("Passwords don't match")

        return values


my_account = UserRegistration(email="e@mail.com", password="passpass", password_confirmation="passpass")

print(my_account)
