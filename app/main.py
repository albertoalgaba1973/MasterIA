from fastapi import FastAPI

from app.routers import estimations

app = FastAPI(title="Estimador CAG",description="API para estimar transcripciones usando el modelo CAG",version="1.0.0")
app.include_router(estimations.router)
