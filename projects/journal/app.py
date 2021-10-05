from database import add_entry, get_entries

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
        # get info from user
        entry_content = input("what have you learned today?  ")
        entry_date = input("Enter today's date:  ")
        add_entry(entry_content, entry_date)

    elif user_input == "2":
        entries = get_entries()
        for entry in entries:
            print(f'************\n{entry["date"]}\n{entry["content"]}\n\n')

    else:
        print("Invalid option, please try again.")