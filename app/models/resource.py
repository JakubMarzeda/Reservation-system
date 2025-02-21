from email.policy import default

from database import Base
from sqlalchemy import Column, Integer, String

class Resource(Base):
    __tablename__ = 'resources'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    type_resource = Column(String, nullable=False)  # (np. sala konferencyjna, pojazd, sprzęt IT)
    location = Column(String, nullable=False)
    availability = Column(String, nullable=False) # (dni i godziny, np. "Poniedziałek-Piątek, 9:00-18:00")
    min_time_reservation = Column(Integer, default=30, nullable=True) # Minimalny czas rezerwacji w minutach
    max_usage_time = Column(Integer, default=8, nullable=True)  # Maksymalny czas użytkowania w godzinach
