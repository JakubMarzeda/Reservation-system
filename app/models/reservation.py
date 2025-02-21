from database import Base
from sqlalchemy import Column, Integer, ForeignKey, DateTime
from datetime import datetime

class Reservation(Base):
    __tablename__ = 'reservations'
    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    resource_id = Column(Integer, ForeignKey('resources.id'), nullable=False)
    start_time = Column(DateTime, nullable=False, default=datetime.utcnow())
    end_time = Column(DateTime, nullable=False)