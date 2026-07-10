from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime

from datetime import datetime

from app.database.database import Base


class Job(Base):

    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)

    job_name = Column(String)

    payload = Column(String)

    status = Column(String, default="PENDING")

    created_at = Column(DateTime, default=datetime.utcnow)