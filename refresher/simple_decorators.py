def get_admin_password():
    return "1234"

def make_function_secure(function):
    def secure_function():
        if user["access_level"] == "admin":
            return function()
        else:
            return "user has insufficient access level"
    
    return secure_function


get_admin_password = make_function_secure(get_admin_password)
user = {"user": "a","access_level": "admin"}
print(get_admin_password())