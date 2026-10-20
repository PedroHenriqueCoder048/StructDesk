from fastapi import FastAPI
from .routers.user import user

app = FastAPI()

app.include_router(user)

@app.get("/")
async def root():
    return {"menssage":"Hello bigger applications"}