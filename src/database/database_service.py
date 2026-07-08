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
            cls.BASE_DIR / "database" / "create_database.sql",
            cls.BASE_DIR / "database" / "views.sql",
            cls.BASE_DIR / "database" / "seed_data.sql"
        ]

        for arquivo in arquivos:

            print(f"\nCarregando: {arquivo}")
        
            with open(
                arquivo,
                "r",
                encoding="utf-8"
            ) as f:
        
                sql = f.read()
        
            for comando in sql.split(";"):
        
                comando = comando.strip()
        
                if not comando:
                    continue
        
                print("\nEXECUTANDO:")
                print(comando[:300])
        
                try:
                    conn.execute(comando)
        
                except Exception as e:
        
                    print("\nERRO NO COMANDO:")
                    print(comando)
                    print("\nERRO:")
                    print(e)
        
                    raise

        conn.commit()
        conn.close()

        print("Banco inicializado com sucesso.")
