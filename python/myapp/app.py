from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session

from myapp.db import get_engine
from myapp.model import Airport

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello from myapp!"}


@app.get("/airport")
def get_airports():
    with Session(get_engine()) as session:
        airports = session.query(Airport).all()
    return [airport.as_dict() for airport in airports]


@app.get("/airport/{airport_icao}")
def get_airport(airport_icao: str):
    with Session(get_engine()) as session:
        airport = session.query(Airport) \
            .filter(Airport.icao == airport_icao) \
            .one_or_none()
    if not airport:
        raise HTTPException(status_code=404,
                            detail=f'Airport with ICAO "{airport_icao}" is not '
                                   f'known.')
    return airport.as_dict()


@app.post("/airport")
def create_airport():
    raise HTTPException(status_code=501, detail="To be implemented")
