from api.parameters.user_create_api_parameters import UserCreateAPIParamaters
from api.presenter.user_presenter import UserCreatePresenter,UserListPresenter
from domain.user_create_parameters import UserCreateParamaters
from usecase.user_usecase import UserUseCase
from fastapi import Response
import traceback

class UserHandler():

    def __init__(self, userUseCase: UserUseCase) -> None:
        self.userUseCase = userUseCase

    def create(self, userApiParmeters: UserCreateAPIParamaters,response: Response) -> UserCreatePresenter:
        try:
            userParmeters = UserCreateParamaters()
            userParmeters.email = userApiParmeters.email
            userParmeters.name = userApiParmeters.name
            userParmeters.password = userApiParmeters.password

            user = self.userUseCase.create(userParmeters)
            return UserCreatePresenter(user)
        
        except Exception as e:
            response.status_code = 500
            just_the_string = traceback.format_exc()
            return {
                "error": True,
                "message": str(e)+just_the_string
            }
            
    def list(self, response: Response) -> UserCreatePresenter:
        try:
            usersPresenter = UserListPresenter(self.userUseCase.list(),1)
            
            return usersPresenter
        
        except Exception as e:
            response.status_code = ''
            just_the_string = traceback.format_exc()
            return {
                "error": True,
                "message": str(e)+just_the_string
            }
         
        
