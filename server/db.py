import mysql.connector
from os import getenv
import time


def get_connection():
    db_config = {
        "host": getenv("MYSQL_HOST"),
        "user": getenv("MYSQL_USER"),
        "password": getenv("MYSQL_PASSWORD"),
        "database": getenv("MYSQL_DATABASE"),
    }

    retries = 10
    while retries > 0:
        try:
            conn = mysql.connector.connect(**db_config)
            print("Connected to MySQL database")
            return conn
        except mysql.connector.Error as err:
            retries -= 1
            print(f"Retrying in 5 seconds... ({retries} retries left)")
            time.sleep(5)

    raise Exception(f"{err}")
