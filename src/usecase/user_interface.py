from abc import ABC,abstractmethod

from domain.user_create_parameters import UserCreateParamaters
from domain.user import User

class UserUseCaseInterface(ABC):

    def create(self,userCreateParameters: UserCreateParamaters) -> User:
        raise NotImplemented

    def list(self):
        raise NotImplemented

class UserRepositoryInteface(ABC):
    def create(self,user: User) -> User:
        raise NotImplemented
    def list(self):
        raise NotImplemented
    def get_by_id(self,user_id: str) -> User:  
        raise NotImplemented  
    def get_by_email(self,email: str) -> User:  
        raise NotImplemented  