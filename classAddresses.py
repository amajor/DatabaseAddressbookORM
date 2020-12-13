from connection import Base
from sqlalchemy import Column, Integer, Sequence, String
from sqlalchemy.orm import relationship


class Addresses(Base):
    __tablename__ = 'addresses'

    address_id = Column(Integer, Sequence('address_id_sequence'), primary_key=True)
    street_address = Column(String(50))
    city = Column(String(50))
    state = Column(String(50))
    zip_code = Column(String(6))

    # List of all users belonging to an address.
    persons = relationship("Association", back_populates="address")
