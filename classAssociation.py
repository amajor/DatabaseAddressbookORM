from sqlalchemy.orm import relationship
from connection import Base
from sqlalchemy import Column, Integer, Date, ForeignKey


class Association(Base):
    __tablename__ = 'people_address'

    id = Column(
        Integer,
        nullable=False,
        primary_key=True,
        unique=True,
        autoincrement=True
    )

    person_id = Column(
        Integer,
        ForeignKey('people_master.person_id'),
        nullable=False,
        primary_key=True,
        default=1
    )
    address_id = Column(
        Integer,
        ForeignKey('addresses.address_id'),
        nullable=False,
        primary_key=True,
        default=1
    )
    start_date = Column(Date)
    end_date = Column(Date)

    person = relationship("Person", back_populates="addresses")
    address = relationship("Addresses", back_populates="persons")
