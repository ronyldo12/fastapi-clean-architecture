import hashlib
from domain.entity import Entity
from domain.validation_return import ValidationReturn


class User(Entity):
    name: str
    email: str
    password: str
   
    def validate(self) -> ValidationReturn:
        v_return = ValidationReturn()
        if self.name == "" :
            v_return.error("The name is required")
        if self.email == "" :
            v_return.error("The email is required")
        if self.password == "" :
            v_return.error("The password is required")
        return v_return   


    def define_password(self, plain_text_password: str):
        self.password = hashlib.sha1(plain_text_password)