from connection import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Addresses(Base):
    __tablename__ = 'addresses'

    address_id = Column(
        Integer,
        nullable=False,
        primary_key=True,
        unique=True,
        autoincrement=True
    )
    street_address = Column(String(50))
    city = Column(String(50))
    state = Column(String(50))
    zip_code = Column(String(6))

    # List of all users belonging to an address.
    persons = relationship("Association", back_populates="address")
