entries = list()

def add_entry():
    # get info from user
    entry_content = input("what have you learned today?")
    entry_date = input("Enter today's date: ")

    # append info as dictionary into entries list
    entries.append({"content": entry_content, "date": entry_date})


def view_entries():
    for entry in entries:
        print(f'{entry["date"]}\n{entry["content"]}\n\n')