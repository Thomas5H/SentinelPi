from fastapi import FastAPI
from pydantic import BaseModel  #lets us describe what an event looks like

app = FastAPI()
#every event must have these three text fields
class Event(BaseModel):
    host: str
    event_type: str
    message: str

@app.get("/")
def home():
    return {"message": "SentinelPi is running"}

#receives a security event and confirms it arrived
@app.post("/events")
def receive_event(event: Event):
    return {"status": "received", "event": event}