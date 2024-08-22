from datetime import datetime

from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine, update
from sqlalchemy.orm import sessionmaker

from event import Event

app = FastAPI()
engine = create_engine("mysql+pymysql://root:calendar@localhost:3306/calendar_db",
                       echo=True)

Session = sessionmaker(bind=engine)
session = Session()

Event.metadata.create_all(engine)


class EventModel(BaseModel):
    name: str
    description: str | None
    event_date: datetime


@app.post('/events')
def create_event(event: EventModel):
    now = datetime.now()
    new_event = Event(name=event.name,
                      description=event.description,
                      event_date=event.event_date,
                      created_date=now,
                      updated_date=now)
    session.add(new_event)
    session.commit()


@app.get('/events')
def find_events():
    return session.query(Event).all()


@app.get("/events/{event_id}")
def find_event(event_id: int):
    return session.query(Event).get(event_id)


@app.put("/events/{event_id}")
def update_event(event_id: int, updated_event: EventModel):
    event: Event = session.query(Event).get(event_id)
    event.name = updated_event.name
    event.description = updated_event.description
    event.event_date = updated_event.event_date
    event.updated_date = datetime.now()

    session.commit()


@app.delete("/events/{event_id}")
def delete_event(event_id: int):
    event = session.query(Event).get(event_id)
    session.delete(event)
