import os
from sqlite3 import connect
from psycopg2.pool import SimpleConnectionPool
from settings import postgres_url
from contextlib import contextmanager

pool = SimpleConnectionPool(minconn=1, maxconn=10, dsn=postgres_url)

@contextmanager
def get_connection():
    connection = pool.getconn()
    try:
        yield connection
    finally:
        pool.putconn(connection)