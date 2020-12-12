from connection import Base
from sqlalchemy import Column, Integer, Sequence, String, Date


class Person(Base):
    __tablename__ = 'people_master'

    person_id = Column(Integer, Sequence('user_id_sequence'), primary_key=True)
    person_name = Column(String(50))
    person_DOB = Column(Date)
    active_phone_number = Column(String(10))
