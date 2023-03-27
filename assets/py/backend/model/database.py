import os
import mysql.connector

from dotenv import load_dotenv


class Database:

    def __init__(self):
        load_dotenv()

        self.config = {
            'user': os.getenv("DATABASE_USER"),
            'password': os.getenv("DATABASE_PASSWORD"),
            'host': os.getenv("DATABASE_HOST"),
            'database': os.getenv("DATABASE_DB"),
            'port': os.getenv("DATABASE_PORT"),
            'raise_on_warnings': True
        }

        self.database = None
        self.connect()

    def connect(self):
        self.database = mysql.connector.connect(**self.config)

    def get_cursor(self):
        return self.database.cursor()

    def query(self, sql):
        try:
            cursor = self.get_cursor()
            cursor.execute(sql)
        except (mysql.connector.errors.InterfaceError, mysql.connector.errors.OperationalError):
            self.connect()
            cursor = self.get_cursor()
            cursor.execute(sql)
        return cursor
