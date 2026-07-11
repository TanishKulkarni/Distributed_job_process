from fastapi import FastAPI

from app.database.database import Base
from app.database.database import engine
from app.api.jobs import router as jobs_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Distributed Job Processing Platform")

app.include_router(jobs_router)


@app.get("/")
def root():
    return {"message": "Backend Running 🚀"}