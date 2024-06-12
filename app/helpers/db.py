import psycopg2
import sys
from config import db_host,db_name,db_user,db_password,db_port


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
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name,
        port=db_port
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
