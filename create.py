import re
from datetime import date
from classAddresses import Addresses
from classAssociation import Association
from classPerson import Person
from connection import session
from formatters import print_user, validate_date
from search import PEOPLE


def check_if_user_exists(name):
    matches = PEOPLE.filter(Person.person_name.like(name))
    if matches.count() > 0:
        return True
    else:
        return False


def create_new_contact():
    print("\n  Input user data below.\n")
    name = input("    Name:           ")
    street = input("    Street Address: ")
    city = input("    City:           ")
    state = input("    State:          ")

    zip_code = input("    Zip:            ")
    while not re.search(r'\d{5}', zip_code):
        print("\n  *** Invalid zip code.")
        print("    Please enter 5-digits with no formatting.")
        print("      Example: XXXXX")
        zip_code = input("\n    Zip:            ")

    phone = input("    Phone:          ")
    while not re.search(r'\d{10}', phone):
        print("\n  *** Invalid phone number.")
        print("    Please enter 10-digits with no formatting.")
        print("      Example: XXXXXXXXXX")
        phone = input("\n    Phone:          ")

    date_of_birth = input("    Birthday:       ")
    is_valid = validate_date(date_of_birth)
    while not is_valid:
        print("    Please enter in the format YYYY-MM-DD.")
        print("      Example: 1985-12-3 or 2010-1-13")
        date_of_birth = input("\n    Birthday:       ")
        is_valid = validate_date(date_of_birth)

    user_exists = check_if_user_exists(name)
    if user_exists:
        print("..... update the user ......")
        # print("\nSuccessfully updated {}!\n".format(name))

        # Display newly added user
        # print_user(person)

    else:
        new_user = Person(
            person_name=name,
            person_DOB=date_of_birth,
            active_phone_number=phone
        )
        new_address = Addresses(
            street_address=street,
            city=city,
            state=state,
            zip_code=zip_code
        )
        new_association = Association(
            start_date=date.today().strftime("%Y-%-m-%-d")
        )
        new_association.address = new_address
        new_user.addresses.append(new_association)

        # Execute the query
        session.add(new_user)
        session.commit()
        print("\nSuccessfully added {}!\n".format(name))

        # Display newly added user
        print_user(new_user)
