from fastapi import APIRouter,Form
from ..models.user import User,Departament,Position
from ..database.config import FileDatabase

database = FileDatabase("users",User)

user = APIRouter(
    prefix="/user",
    tags=["user"])

@user.post("/")
async def create_user(
    id:int = Form(),
    name:str = Form(),
    age:int = Form(),
    departament: Departament= Form(),
    position:Position = Form()
    ):

    user = User(
        id=id,
        name= name,
        age=age,
        departament=departament,
        position=position
    )

    return user

routers_called= APIRouter(
    prefix="/called",
    tags=["called"])

@routers_called.post("/")
async def create_user(
    id:int = Form(),
    name:str = Form(),
    age:int = Form(),
    departament: Departament= Form(),
    position:Position = Form()
    ):

    user = User(
        id=id,
        name= name,
        age=age,
        departament=departament,
        position=position
    )

    return user

# @routers_user.get("/")
# async def create_user(user:User):
#     return 

# @routers_user.put("/")
# async def create_user(user:User):
#     return user

# @routers_user.delete("/")
# async def create_user(user:User):
#     return user

# routers_