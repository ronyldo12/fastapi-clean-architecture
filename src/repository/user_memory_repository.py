from xml.dom import NotFoundErr
from domain.user import User
from usecase.user_interface import UserRepositoryInteface
from exceptions.not_found_exception import NotFoundException


class UserMemoryRepository(UserRepositoryInteface):

    def __init__(self) -> None:
        self.users = []
        super().__init__()

    def create(self,user: User) -> User:
        self.users.append(user)
        return user

    def list(self):
        return self.users
    
    def get_by_id(self,user_id: str) -> User:
        for user in self.users:
            if user.id == user_id:
                return user
        raise NotFoundException("user not found")

    def get_by_email(self,email: str) -> User:
        for user in self.users:
            if user.email == email:
                return user
        raise NotFoundException("user not found")
