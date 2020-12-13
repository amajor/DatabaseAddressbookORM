#!/usr/bin/env python3
from create import create_new_contact
from formatters import clear_terminal_screen
from initialize import initialize_base
from search import search_exact_name, search_partial_name, search_phone_area_code, search_phone_prefix, search_age_range

MENU = '''
===================================
|                                 |
|  1 - Search by Exact Name       |
|  2 - Search by Partial Name     |
|                                 |
|  3 - Search by Phone Area Code  |
|  4 - Search by Phone Prefix     |
|                                 |
|  5 - Search by Age              |
|                                 |
|  6 - Create/Update Contact      |
|                                 |
|  0 - Quit                       |
|                                 |
===================================
'''


# Define the main program that will run.
def main():
    clear_terminal_screen()

    # Get user input
    print(MENU)
    menu_choice = input("Menu Choice: ")

    while True:
        if menu_choice == "1":
            search_exact_name()
        elif menu_choice == "2":
            search_partial_name()
        elif menu_choice == "3":
            search_phone_area_code()
        elif menu_choice == "4":
            search_phone_prefix()
        elif menu_choice == "5":
            search_age_range()
        elif menu_choice == "6":
            create_new_contact()
        elif menu_choice == "0":
            quit()
        else:
            print("\n*** Not a valid choice. Please choose from the menu. ***\n\n")

        # Present the menu again to the user.
        print(MENU)
        menu_choice = input("Menu Choice: ")


# Run the main program
main()
