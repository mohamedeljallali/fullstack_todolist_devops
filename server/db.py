import mysql.connector
import os
import time

def get_connection():
    retries = 10
    for i in range(retries):
        try:
            conn = mysql.connector.connect(
                host=os.getenv("MYSQL_HOST", "localhost"),
                user=os.getenv("MYSQL_USER"),
                password=os.getenv("MYSQL_PASSWORD"),
                database=os.getenv("MYSQL_DATABASE")
            )
            print("Successfully connected to the database!")
            return conn
        except mysql.connector.Error as err:
            print(f"Database not ready yet... (Attempts left: {retries})")
            time.sleep(5)  # Wait before retrying
    raise Exception("Could not connect to the database after multiple attempts.")