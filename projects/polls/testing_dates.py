import pytz
import json

user_timezone = input("Enter your timezone: ").strip()

try:
    pytz.timezone(user_timezone)
except pytz.exceptions.UnknownTimeZoneError:
    print("Unkown Time Zone.")
    raise