from api.parameters.user_create_api_parameters import UserCreateAPIParamaters
from api.presenter.user_presenter import UserCreatePresenter
from domain.user_create_parameters import UserCreateParamaters
from usecase.user_usecase import UserUseCase


class UserHandler():

    def __init__(self, userUseCase: UserUseCase) -> None:
        self.userUseCase = userUseCase

    def create(self, userApiParmeters: UserCreateAPIParamaters) -> UserCreatePresenter:

        userParmeters = UserCreateParamaters()
        userParmeters.email = userApiParmeters.email
        userParmeters.name = userApiParmeters.name
        userParmeters.password = userApiParmeters.password

        user = self.userUseCase.create(userParmeters)
        return UserCreatePresenter(user)
        
