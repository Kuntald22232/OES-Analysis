from fastapi import FastAPI
from routes.analytics import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="OES Analytics Service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router, prefix="/analytics")

@app.get("/")
def home():
    return {"message": "OES Analytics Running"}