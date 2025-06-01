from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

class CorsConfig:
    
    @staticmethod
    def setup_cors(app: FastAPI):
        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )