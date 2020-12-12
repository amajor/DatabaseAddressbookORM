from connection import session
from classPerson import Person
from classAddresses import Addresses
from formatters import format_phone


print('\nPEOPLE:\n==========')
for person in session.query(Person):
    print(
        person.person_id,
        person.person_name,
        person.person_DOB,
        format_phone(person.active_phone_number)
    )

print('\nADDRESSES:\n==========')
for address in session.query(Addresses):
    print(
        address.address_id,
        address.street_address,
        address.city,
        address.state,
        address.zip_code
    )
