from classPerson import Person
from connection import session
from formatters import print_user, print_person_not_found, clear_terminal_screen, print_phone_format

PEOPLE = session.query(Person)


def print_results(matches):
    if matches.count() > 0:
        for contact in matches:
            print_user(contact)
    else:
        print_person_not_found()


def search_exact_name():
    name = input("Enter Name: ")
    clear_terminal_screen()

    # Provide output
    print("\nSearching for names spelled '{}'...\n".format(name))
    matches = PEOPLE.filter(Person.person_name.like(name))
    print_results(matches)


def search_partial_name():
    name = input("Enter Part of Name: ")
    clear_terminal_screen()

    # Provide output
    print("\nSearching for names with '{}'...\n".format(name))
    matches = PEOPLE.filter(Person.person_name.like('%{}%'.format(name)))
    print_results(matches)


def search_phone_area_code():
    print_phone_format()
    area_code = input("\nEnter 3-Digit Area Code: ")

    while not area_code.isnumeric():
        print("\n*** Not a valid area code. ***")
        area_code = input("\n  Enter 3-Digit Area Code: ")
    clear_terminal_screen()

    # Provide output
    print("\nSearching by '({})xxx-xxxx'...\n".format(area_code))
    matches = PEOPLE.filter(Person.active_phone_number.like("{}_______".format(area_code)))
    print_results(matches)


def search_phone_prefix():
    print_phone_format()
    prefix = input("\nEnter Phone Prefix: ")

    while not prefix.isnumeric():
        print("\n*** Not a valid prefix. ***")
        prefix = input("\nEnter Phone Prefix: ")
    clear_terminal_screen()

    # Provide output
    print("\nSearching by '(xxx){}-xxxx'...\n".format(prefix))
    matches = PEOPLE.filter(Person.active_phone_number.like("___{}____".format(prefix)))
    print_results(matches)
