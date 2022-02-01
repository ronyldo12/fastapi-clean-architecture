from domain.validation_return import ValidationReturn

class UserCreateParamaters():
    
    name: str
    email: str
    password: str

    def __init__(self):
        self.name = ""
        self.email = ""
        self.password = ""

    def validate(self) -> ValidationReturn:
        v_return = ValidationReturn()
        if self.name == "" :
            v_return.error("The name is required")
        if self.email == "" :
            v_return.error("The email is required")
        if self.password == "" :
            v_return.error("The password is required")
        return v_return    


        