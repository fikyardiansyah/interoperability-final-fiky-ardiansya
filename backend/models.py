from pydantic import BaseModel

class Event(BaseModel):
    title: str
    date: str
    location: str
    quota: int

class Participant(BaseModel):
    name: str
    email: str
    event_id: int
