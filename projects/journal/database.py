entries = list()

def add_entry(entry_content, entry_date):
    # append info as dictionary into entries list
    entries.append({"content": entry_content, "date": entry_date})


def get_entries():
    return entries