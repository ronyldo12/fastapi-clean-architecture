from pydantic import BaseModel


class UserCreateAPIParamaters(BaseModel):
        name: str 
        email: str
        password: str
