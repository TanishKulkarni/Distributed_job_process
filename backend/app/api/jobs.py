from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.database import get_db
from app.database.models import Job
from app.schemas.job import JobCreate

router = APIRouter()


@router.post("/jobs")
def create_job(job: JobCreate, db: Session = Depends(get_db)):

    new_job = Job(
        job_name=job.job_name,
        payload=job.payload
    )

    db.add(new_job)

    db.commit()

    db.refresh(new_job)

    return new_job