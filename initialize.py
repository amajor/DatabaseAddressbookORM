from classAddresses import Addresses
from classAssociation import Association
from classPerson import Person
from connection import Base, engine, session


def initialize_base():
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)
    session.add(Person())
    session.add(Addresses())
    session.add(Association())
    session.commit()
