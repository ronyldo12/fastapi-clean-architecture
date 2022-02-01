from warnings import catch_warnings
from domain.user_create_parameters import UserCreateParamaters
from domain.user import User
from usecase.user_interface import UserRepositoryInteface, UserUseCaseInterface
from exceptions.not_found_exception import NotFoundException
from exceptions.validation_exception import ValidationException

class UserUseCase(UserUseCaseInterface):

    def __init__(self, userRepository: UserRepositoryInteface) -> None:
        self.userRepository = userRepository
        super().__init__()

    def list(self):
        return self.userRepository.list()

    def create(self,userCreateParameters: UserCreateParamaters) -> User:
        validation = userCreateParameters.validate()
        if validation.passed ==  False:
            raise ValidationException(validation.messages)

        try:
            if  self.userRepository.get_by_email(userCreateParameters.email) :   
                raise  ValidationException("the e-mail "+userCreateParameters.email+" is already in use")
        except NotFoundException:
            pass


        user = User()
        user.new_id()
        user.email = userCreateParameters.email
        user.define_password(userCreateParameters.password)
        user.name = userCreateParameters.name
        
        user.validate()
        if validation.passed ==  False:
            raise ValidationException(validation.messages)

        return self.userRepository.create(user)


