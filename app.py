import database
from database import get_best_preparation_for_bean


MENU_PROMPT = """-- Coffee Bean App --

Please choose one of these options:

1) Add a new bean.
2) See all Beans.
3) Find a bean by name.
4) See which preparation method is best for a bean.
5) Exit.
6) Delete a bean.
7) Filter beans by rating.

Your selection:"""


def menu():
    connection = database.connect()
    database.create_tables(connection)

    while (user_input := input(MENU_PROMPT)) != "5":
        if user_input == "1":
             prompt_add_new_bean(connection)
        elif user_input == "2":
            prompt_see_all_beans(connection)
        elif user_input == "3":
            prompt_find_bean(connection)
        elif user_input == "4":
            prompt_find_best_method(connection)
        elif user_input == "6":
            prompt_delete_bean(connection)
        elif user_input == "7":
            prompt_view_bean_by_rating(connection)
        else:
            print("Invalid input, please try again!")


def prompt_add_new_bean(connection):
    name = input("Enter bean name: ")
    method = input("Enter how you've prepared it: ")
    rating = int(input("Enter your rating score (0-100): "))

    database.add_bean(connection, name, method, rating)

def prompt_see_all_beans(connection):
    beans = database.get_all_beans(connection)

    for bean in beans:
        print(f"{bean[1]} {bean[2]} - {bean[3]}/100")

def prompt_find_bean(connection):
    name = input("Enter bean name to find: ")
    beans = database.get_beans_by_name(connection, name)

    for bean in beans:
        print(f"{bean[1]} {bean[2]} - {bean[3]}/100")

def prompt_find_best_method(connection):
    name = input("Enter bean name to find: ")
    best_method = database.get_best_preparation_for_bean(connection, name)

    print(f"The best preparation method for {name} is: {best_method[2]}")

def prompt_delete_bean(connection):
    choice = input("Delete by (1) ID or (2) Name? ")

    if choice == "1":
        bean_id = int(input("Enter bean ID: "))
        database.delete_bean_by_id(connection, bean_id)
        print("Bean deleted by ID.")

    elif choice == "2":
        name = input("Enter bean name: ")
        database.delete_bean_by_name(connection, name)
        print("Bean deleted by name.")

def prompt_view_bean_by_rating(connection):
    low = int(input("Enter minimum rating: "))
    high = int(input("Enter maximum rating: "))

    beans = database.get_beans_by_rating_range(connection, low, high)

    for bean in beans:
        print(f"{bean[1]} {bean[2]} - {bean[3]}/100")

menu()
