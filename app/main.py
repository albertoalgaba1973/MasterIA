from fastapi import FastAPI

from app.routers import estimations

app = FastAPI()
app.include_router(estimations.router)
