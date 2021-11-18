all_users = [
    {"user": "a","access_level": "guest"},
    {"user": "b","access_level": "admin"}
]

def get_admin_password():
    return "1234"

def check_access_level():
    for a_user in all_users:
        if a_user["access_level"] != "admin":
            print(f'user {a_user["user"]} only has \"{a_user["access_level"]}\" level access')
        else:
            print(f'{a_user["user"]}\'s admin password is: {get_admin_password()}')

check_access_level()