from api.parameters.user_create_api_parameters import UserCreateAPIParamaters
from domain.user_create_parameters import UserCreateParamaters
from application.appllication import userHandler
from fastapi import FastAPI,Response

app = FastAPI()


@app.post("/users")
async def create_user(user: UserCreateAPIParamaters,response: Response):
    return userHandler.create(user,response)


@app.get("/users")
async def list_user(response: Response):
    return userHandler.list(response)
