from pathlib import Path
import sqlite3
import os


class DatabaseService:

    BASE_DIR = Path(os.getcwd())

    DB_PATH = BASE_DIR / "banco.db"

    @classmethod
    def get_connection(cls):

        return sqlite3.connect(cls.DB_PATH)

    @classmethod
    def initialize_database(cls):
    
        conn = cls.get_connection()
    
        arquivos = [
            "database/create_database.sql",
            "database/views.sql",
            "database/seed_data.sql"
        ]
    
        for arquivo in arquivos:
    
            with open(
                arquivo,
                "r",
                encoding="utf-8"
            ) as f:
    
                conn.executescript(f.read())
    
        conn.commit()
        conn.close()
    
        print("Banco inicializado com sucesso.")
