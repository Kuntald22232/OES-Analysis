from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.analytics import router

app = FastAPI(
    title="OES Analytics Service"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://online-exam-2026.netlify.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    router,
    prefix="/analytics"
)


@app.get("/")
def home():

    return {
        "message": "OES Analytics Running"
    }