from pydantic import BaseModel


class JobCreate(BaseModel):

    job_name: str

    payload: str


class JobResponse(BaseModel):

    id: int

    job_name: str

    payload: str

    status: str

    class Config:
        from_attributes = True