from fastapi import FastAPI
from .routers.routers import routers_user

app = FastAPI()

app.include_router(routers_user)

@app.get("/")
async def root():
    return {"menssage":"Hello bigger applications"}