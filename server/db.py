import mysql.connector
import os
import time


def get_connection():
    db_config = {
        "host": os.getenv("MYSQL_HOST"),
        "user": os.getenv("MYSQL_USER"),
        "password": os.getenv("MYSQL_PASSWORD"),
        "database": os.getenv("MYSQL_DATABASE"),
    }

    retries = 10
    while retries > 0:
        try:
            conn  = mysql.connector.connect(**db_config)
            print("Connected to MySQL database")
            return conn
        except mysql.connector.Error as err:
            retries -= 1
            print(f"Retrying in 5 seconds... ({retries} retries left)")
            time.sleep(5)

    raise Exception("Could not connect to MySQL database after multiple attempts")