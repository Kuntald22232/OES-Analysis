from pydantic import BaseModel

class Result(BaseModel):
    studentName: str
    marks: int