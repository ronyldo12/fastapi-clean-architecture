from fastapi import FastAPI
from api.parameters.user_create_api_parameters import UserCreateAPIParamaters
from domain.user_create_parameters import UserCreateParamaters
from api.handlers.user_handler import UserHandler
from repository.user_memory_repository import UserMemoryRepository
from usecase.user_usecase import UserUseCase



app = FastAPI()
userMemoryRepositry = UserMemoryRepository()
userUseCase = UserUseCase(userMemoryRepositry)
userHandler = UserHandler(userUseCase)

@app.post("/users")
async def create_user(user: UserCreateAPIParamaters):
    return userHandler.create(user)
