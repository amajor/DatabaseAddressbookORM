#!/usr/bin/env python3

from connection import Base, engine, session
from classPerson import Person
from classAddresses import Addresses
from classAssociation import Association
from initialize import initialize_base


def setup():
    Base.metadata.create_all(engine)

    ############################
    #  CREATE DATA FOR TABlES  #
    ############################

    # Build user data
    user1 = Person(
        person_name='Major',
        person_DOB='1983-12-08',
        active_phone_number='6161111515'
    )
    user2 = Person(
        person_name='Smith',
        person_DOB='1972-1-22',
        active_phone_number='8881234567'
    )
    user3 = Person(
        person_name='Jones',
        person_DOB='1962-5-14',
        active_phone_number='7771234567'
    )
    user4 = Person(
        person_name='DeVries',
        person_DOB='1982-7-3',
        active_phone_number='9997654323'
    )

    # Build address data
    address1 = Addresses(
        street_address='123 State Street',
        city='Anytown',
        state='Michigan',
        zip_code='11111'
    )
    address2 = Addresses(
        street_address='456 Main Street',
        city='Chicago',
        state='Illinois',
        zip_code='60007'
    )
    address3 = Addresses(
        street_address='89 Another Street',
        city='Chicago',
        state='Illinois',
        zip_code='60007'
    )

    # Build associations between addresses and persons
    association1 = Association(start_date='2000-01-01', end_date='2015-03-26')
    association1.address = address1
    user1.addresses.append(association1)

    association2 = Association(start_date='2015-03-26')
    association2.address = address2
    user1.addresses.append(association2)

    association3 = Association(start_date='2010-05-17')
    association3.address = address3
    user2.addresses.append(association3)

    association4 = Association(start_date='2012-02-02')
    association4.address = address3
    user3.addresses.append(association4)

    association5 = Association(start_date='2015-03-29')
    association5.address = address1
    user4.addresses.append(association5)

    # Add the data to the tables
    session.add(user1)
    session.add(user2)
    session.add(user3)
    session.add(user4)

    # Commit the changes
    session.commit()
    print("Successfully populated tables")


def drop_all_tables():
    initialize_base()

    Association.__table__.drop()
    Person.__table__.drop()
    Addresses.__table__.drop()
    print("Successfully dropped tables")


drop_all_tables()
setup()

for user in session.query(Person).filter(Person.person_name.like("Major")):
    print(user.person_name)
    for association in user.addresses:
        print("  ", association.address.street_address)
