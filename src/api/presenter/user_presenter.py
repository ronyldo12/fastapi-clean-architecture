from domain.user import User


class UserCreatePresenter():

    id:str
    email: str
    name: str
    created_at: str

    def __init__(self,user: User) -> None:
        self.id = user.id
        self.name = user.name
        self.email = user.email
        self.created_at = user.created_at