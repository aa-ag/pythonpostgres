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
    all_users = cursor.fetchall()
    print(all_users)
    connection.close()


def create_a_user():
    connection = psycopg2.connect(url)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (id, name) VALUES (3, 'Bob Smith');")
    connection.commit()
    connection.close()


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    create_a_user()
    get_all_users()
    