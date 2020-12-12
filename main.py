from connection import session
from classPerson import Person
from classAddresses import Addresses
from formatters import format_phone, print_user, print_address

print('\nPEOPLE:\n==========')
for person in session.query(Person):
    print_user(person)

print('\nADDRESSES:\n==========')
for address in session.query(Addresses):
    print_address(address)

print('\nFILTERING:\n==========')
for person in session.query(Person).filter(Person.person_name.like('%Ma%')):
    print(
        person.person_id,
        person.person_name,
        person.person_DOB,
        format_phone(person.active_phone_number)
    )
