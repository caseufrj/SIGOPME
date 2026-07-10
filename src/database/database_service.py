from pathlib import Path
import sqlite3
import os

from database.schema import SCHEMA_SQL
from database.views_def import VIEWS_SQL
from database.seed import SEED_SQL

class DatabaseService:

    BASE_DIR = Path(os.getcwd())

    DB_PATH = BASE_DIR / "banco.db"

    @classmethod
    def get_connection(cls):

        return sqlite3.connect(cls.DB_PATH)
        
    @classmethod
    def initialize_database(cls):
    
        conn = cls.get_connection()
    
        try:
    
            conn.executescript(
                SCHEMA_SQL
            )
    
            conn.executescript(
                VIEWS_SQL
            )
    
            conn.executescript(
                SEED_SQL
            )
    
            conn.commit()
    
            print(
                "Banco inicializado com sucesso."
            )
    
        except Exception as e:
    
            print(
                f"Erro ao inicializar banco: {e}"
            )
    
            raise
    
        finally:
    
            conn.close()
