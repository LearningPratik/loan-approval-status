from fastapi import FastAPI
from pydantic import BaseModel

class Status(BaseModel):
    married: str
    gender: str
    self_employed: str
    education: str
    amount: float
    credit_history: float