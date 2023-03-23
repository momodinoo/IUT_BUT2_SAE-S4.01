import os
import mysql.connector

from dotenv import load_dotenv, dotenv_values


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
        if self.database is None:
            self.database = mysql.connector.connect(**self.config)

        return self.database

    def get_cursor(self):
        return self.database.get_cursor()
