from domain.user import User


class UserCreatePresenter():
    id: str
    email: str
    fullname: str
    created_at: str

    def __init__(self,user: User) -> None:
        self.id = user.id
        self.fullname = user.name
        self.email = user.email
        self.created_at = user.created_at
        
        
class UserListPresenter():
    def __init__(self,usersDomain, page: int) -> None:
        self.page = page
        self.users = []
        for user in usersDomain:
            self.users.append(UserCreatePresenter(user))
              