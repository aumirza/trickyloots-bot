import psycopg2
import sys
from urllib.parse import urlparse
from app.config import db_url


db_info = urlparse(db_url)


def create_table_if_not():
    query = """
  CREATE TABLE IF NOT EXISTS message_id  (
	source_id INT PRIMARY KEY,
	dest_id INT NOT NULL,
  date_time DATE NOT NULL DEFAULT CURRENT_DATE
);
  """
    cursor.execute(query)
    db.commit()


try:
    db = psycopg2.connect(
        host=db_info.hostname,
        user=db_info.username,
        password=db_info.password,
        database=db_info.path[1:],
        port=db_info.port
    )

    cursor = db.cursor()
    cursor.execute('SELECT version()')

    version = cursor.fetchone()[0]
    print(version)

    create_table_if_not()

except psycopg2.DatabaseError as e:
    print("Error while connecting to Postgres SQL", e)
    sys.exit()


def insert_query(query):
    cursor.execute(query)
    db.commit()


def select_query(query):
    cursor.execute(query)
    record = cursor.fetchone()
    return record[0]