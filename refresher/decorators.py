import functools as ft

user = {"user": "a","access_level": "guest"}

def make_function_secure_factory(access_level):
    def make_function_secure_decorator(function):
        @ft.wraps(function)
        def secure_function(*args, **kwargs):
            if user["access_level"] == "admin":
                return function(*args, **kwargs)
            else:
                return "user has insufficient access level"
        
        return secure_function
    return make_function_secure_decorator


@make_function_secure_factory
def get_admin_password(panel):
    if panel == "admin":
        return "1234"
    return "nope"


@make_function_secure_factory
def get_dashboard_password(panel):
    return "user: userpassword"


print(get_admin_password.__name__)