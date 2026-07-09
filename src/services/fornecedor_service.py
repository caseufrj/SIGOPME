from database.database_service import DatabaseService


class FornecedorService:

    @staticmethod
    def listar_todos():

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                Id,
                Nome,
                Cnpj,
                Telefone,
                Email,
                Contato
            FROM Fornecedores
            WHERE Ativo = 1
            ORDER BY Nome
        """)

        dados = cursor.fetchall()

        conn.close()

        return dados
