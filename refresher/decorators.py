user = {"user": "a","access_level": "guest"}

def make_function_secure(function):
    def secure_function():
        if user["access_level"] == "admin":
            return function()
        else:
            return "user has insufficient access level"
    
    return secure_function


@make_function_secure
def get_admin_password():
    return "1234"


print(get_admin_password())