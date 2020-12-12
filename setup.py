from connection import Base, engine, session


# USER TABLE
from classPerson import Person

# ADDRESS TABLE
from classAddresses import Addresses


############################
# BUILD TABLES IN DATABASE #
############################
Base.metadata.create_all(engine)

############################
#  CREATE DATA FOR TABlES  #
############################

# Build user data
user1 = Person(person_name='Major', person_DOB='1983-12-08', active_phone_number='6161111515')
user2 = Person(person_name='Smith', person_DOB='1972-1-22', active_phone_number='8881234567')
user3 = Person(person_name='Jones', person_DOB='1962-5-14', active_phone_number='7771234567')
user4 = Person(person_name='DeVries', person_DOB='1982-7-3', active_phone_number='9997654323')

# Add the data to the tables
session.add(user1)
session.add(user2)
session.add(user3)
session.add(user4)

# Commit the changes
session.commit()