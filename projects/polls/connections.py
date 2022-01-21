import os
from psycopg2.pool import SimpleConnectionPool
from settings import postgres_url

pool = SimpleConnectionPool(minconn=1, maxconn=10, dsn=postgres_url)