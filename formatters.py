import os
from datetime import date


###################################
# Clears the terminal screen      #
###################################
def clear_terminal_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


###################################
# Prints the phone format         #
###################################
def print_phone_format():
    print("\n(AAA)PPP-LLLL\n")
    print("  Area Code   --> (AAA)")
    print("  Prefix      --> PPP")
    print("  Line Number --> LLLL")


###################################
# Return a formatted phone number #
###################################
def format_phone(phone):
    # Slice out Area Code
    area_code_slice = slice(3)
    area_code = phone[area_code_slice]

    # Slice out Prefix
    prefix_slice = slice(3, 6)
    prefix = phone[prefix_slice]

    # Slice out Line Number
    line_number_slice = slice(6, 10)
    line_number = phone[line_number_slice]

    # Return formatted number string
    return "({}){}-{}".format(area_code, prefix, line_number)


###############################################
# Print that a matching contact was not found #
###############################################
def print_person_not_found():
    print("++++++++++++++++++++++++++++++++++++++++")
    print("+\n+  No record found.")
    print("+\n++++++++++++++++++++++++++++++++++++++++\n")


###############################################
# Print the formatted address to the terminal #
###############################################
def print_address(address):
    print("++++\n++++    ADDRESS:  ", address.street_address)
    print("++++               {}, {} {}".format(address.city, address.state, address.zip_code))


###############################################
# Print the formatted person to the terminal  #
###############################################
def print_user(person):
    # Format the phone number
    formatted_phone = format_phone(person.active_phone_number)

    # Calculate the person's age
    age = date.today().year - person.person_DOB.year

    # Print record for user.
    print("+++++++++++++++++++++++++++++++++++++++++++++++")
    print("++++\n++++    NAME:     ", person.person_name)
    print("++++\n++++    PHONE:    ", formatted_phone)
    print("++++\n++++    BIRTHDAY: ", person.person_DOB)
    print("++++               ({} years old)".format(age))
    print("++++\n+++++++++++++++++++++++++++++++++++++++++++++++\n")
