from database.database_service import DatabaseService


class EntradaService:

    @staticmethod
    def listar_todos():

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                Id,
                NumeroNF,
                SerieNF,
                DataEntrada,
                TipoEntrada,
                Fornecedor,
                CodItem,
                NomeMaterial,
                Quantidade
            FROM Entradas
            ORDER BY DataEntrada DESC
        """)

        dados = cursor.fetchall()

        conn.close()

        return dados
