from fastapi import FastAPI
from src.common.infrastructure import CorsConfig

app = FastAPI()

CorsConfig.setup_cors(app)

@app.get("/")
def root():
    return {"Hello": "World"}