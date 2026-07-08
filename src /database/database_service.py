import sqlite3
from pathlib import Path


class DatabaseService:

    DB_PATH = Path("database/banco.db")

    @classmethod
    def get_connection(cls):
        return sqlite3.connect(cls.DB_PATH)

    @classmethod
    def initialize_database(cls):

        conn = cls.get_connection()

        with open(
            "database/create_database.sql",
            "r",
            encoding="utf-8"
        ) as file:

            script = file.read()

        conn.executescript(script)

        conn.commit()
        conn.close()

        print("Banco inicializado.")
`
