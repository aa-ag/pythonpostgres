user = {"user": "a","access_level": "guest"}

def get_admin_password():
    return "1234"

def make_function_secure(function):
    def secure_function():
        if user["access_level"] == "admin":
            return function()
    
    return secure_function


get_admin_password = make_function_secure(get_admin_password)
print(get_admin_password())