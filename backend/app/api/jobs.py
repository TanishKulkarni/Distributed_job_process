from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.schemas.job import JobCreate, JobResponse
from app.services.job_service import (
    create_job,
    get_jobs,
    get_job,
    delete_job,
)

router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"],
)


@router.post("/", response_model=JobResponse)
def create(job: JobCreate, db: Session = Depends(get_db)):
    return create_job(db, job)


@router.get("/", response_model=list[JobResponse])
def all_jobs(db: Session = Depends(get_db)):
    return get_jobs(db)


@router.get("/{job_id}", response_model=JobResponse)
def single_job(job_id: int, db: Session = Depends(get_db)):

    job = get_job(db, job_id)

    if not job:
        raise HTTPException(404, "Job not found")

    return job


@router.delete("/{job_id}")
def remove_job(job_id: int, db: Session = Depends(get_db)):

    job = delete_job(db, job_id)

    if not job:
        raise HTTPException(404, "Job not found")

    return {"message": "Job deleted"}