from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

@app.get("/")
async def root():
    return "Главная страница"

@app.get("/user/admin")
async def admin():
    return "Вы вошли как администратор"

@app.get("/user/{user_id}")
async def get_user(user_id: int = Path(..., description='Enter User ID', ge=1, le=100, example=1)):
    return f'Вы вошли как пользователь № {user_id}'

@app.get("/user/{username}/{age}")
async def get_user_age(
    username: Annotated[str, Path(description='Enter username', min_length=5, max_length=20, example='UrbanUser')],
    age: Annotated[int, Path(description='Enter age', ge=18, le=120, example=24)]
):
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'

# пример без Annotated
# @app.get("/user/{username}/{age}")
# async def get_user_age(
#     username: str = Path(..., description='Enter username', min_length=5, max_length=20, example='UrbanUser'),
#     age: int = Path(..., description='Enter age', ge=18, le=120, example=24)
# ):
#     return f'Информация о пользователе. Имя: {username}, Возраст: {age}'