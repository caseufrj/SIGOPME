import sqlite3
from pathlib import Path

DB_PATH = Path("database/banco.db")


class DatabaseService:

    @staticmethod
    def get_connection():
        return sqlite3.connect(DB_PATH)

    @staticmethod
    def initialize_database():

        if not DB_PATH.exists():
            print("Criando banco de dados...")

        conn = DatabaseService.get_connection()

        with open(
            "database/create_database.sql",
            "r",
            encoding="utf-8"
        ) as sql_file:

            sql_script = sql_file.read()
            conn.executescript(sql_script)

        conn.commit()
        conn.close()

        print("Banco inicializado.")
