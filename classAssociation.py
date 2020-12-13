from sqlalchemy.orm import relationship
from connection import Base
from sqlalchemy import Column, Integer, Date, ForeignKey


class Association(Base):
    __tablename__ = 'people_address'

    person_id = Column(Integer, ForeignKey('people_master.person_id'), primary_key=True)
    address_id = Column(Integer, ForeignKey('addresses.address_id'), primary_key=True)
    start_date = Column(Date)
    end_date = Column(Date)

    person = relationship("Person", back_populates="addresses")
    address = relationship("Addresses", back_populates="persons")
