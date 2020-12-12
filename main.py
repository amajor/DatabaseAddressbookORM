from connection import session
from classPerson import Person
from formatters import format_phone


for person in session.query(Person):
    print(
        person.person_id,
        person.person_name,
        person.person_DOB,
        format_phone(person.active_phone_number)
    )
