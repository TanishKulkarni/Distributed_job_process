from fastapi import FastAPI

from app.database.database import Base
from app.database.database import engine

from app.api.health import router as health_router
from app.api.jobs import router as job_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Distributed Job Platform")

app.include_router(health_router)

app.include_router(job_router)