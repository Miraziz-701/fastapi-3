from fastapi import FastAPI
from routers import auth
from models.db import init_models

app = FastAPI()
app.include_router(auth.router)



@app.on_event("startup")
async def on_startup():
    await init_models()