############------------ IMPORTS ------------############
import psycopg2
import settings

############------------ GLOBAL VARIABLE(S) ------------############
url = settings.postgres_url


############------------ FUNCTION(S) ------------############
def get_all_users():
    connection = psycopg2.connect(url)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users;")
    first_user = cursor.fetchone()
    print(first_user)
    connection.close()


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    get_all_users()