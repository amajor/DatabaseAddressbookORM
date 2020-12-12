from connection import Base
from sqlalchemy import Column, Integer, Sequence, String


class Addresses(Base):
    __tablename__ = 'addresses'

    address_id = Column(Integer, Sequence('address_id_sequence'), primary_key=True)
    street_address = Column(String(50))
    city = Column(String(50))
    state = Column(String(50))
    zip_code = Column(String(6))
