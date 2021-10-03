welcome_message = "Hi, welcome to your journal!"

menu = """
Please press the 1, 2 or 3 keys to select one of the following options:

"1" to add a new entry
"2" to view entries
"3" to exit
"""

while user_input := input(menu) != "3":
    if user_input == "1":
        print("Adding your entry...")
    elif user_input == "2":
        print("viewing")
    else:
        print("Invalid option, please try again.")