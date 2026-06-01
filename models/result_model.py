from pydantic import BaseModel

class SubjectResult(BaseModel):
    subject: str
    marks: int