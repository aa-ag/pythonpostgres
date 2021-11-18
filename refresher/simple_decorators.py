user = {"user": "a","access_level": "admin"}

def get_admin_password():
    return "1234"

def check_access_level(function):
    if user["access_level"] == "admin":
        return function


get_admin_password = check_access_level(get_admin_password)
print(get_admin_password())