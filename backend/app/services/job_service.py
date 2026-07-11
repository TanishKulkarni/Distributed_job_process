from sqlalchemy.orm import Session

from app.models.job import Job
from app.schemas.job import JobCreate


def create_job(db: Session, job: JobCreate):

    new_job = Job(
        job_name=job.job_name,
        payload=job.payload
    )

    db.add(new_job)
    db.commit()
    db.refresh(new_job)

    return new_job


def get_jobs(db: Session):

    return db.query(Job).all()


def get_job(db: Session, job_id: int):

    return db.query(Job).filter(Job.id == job_id).first()


def delete_job(db: Session, job_id: int):

    job = db.query(Job).filter(Job.id == job_id).first()

    if job:
        db.delete(job)
        db.commit()

    return job