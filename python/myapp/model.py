from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Airport(Base):
    __tablename__ = "airport"
    id = Column(Integer, primary_key=True)
    icao = Column(String(4), index=True, unique=True)
    name = Column(String)

    def as_dict(self):
        return {
            'id': self.id,
            'icao': self.icao,
            'name': self.name,
        }

    def __repr__(self):
        return f"Airport(id={self.id}, icao={self.icao}, name={self.name})"
