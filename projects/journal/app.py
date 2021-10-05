from database import add_entry, view_entries

welcome_message = "Hi, welcome to your journal!"

menu = """
Please press the 1, 2 or 3 keys to select one of the following options:

"1" to add a new entry
"2" to view entries
"3" to exit\n
"""

print(welcome_message)

while (user_input := input(menu)) != "3":
    if user_input == "1":
        add_entry()
    elif user_input == "2":
        view_entries()
    else:
        print("Invalid option, please try again.")