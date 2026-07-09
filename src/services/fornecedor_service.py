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
                Contato,
                Email
            FROM Fornecedores
            WHERE Ativo = 1
            ORDER BY Nome
        """)

        dados = cursor.fetchall()

        conn.close()

        return dados

    @staticmethod
    def inserir(
        nome,
        cnpj,
        telefone,
        contato,
        email
    ):

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO Fornecedores (
                Nome,
                Cnpj,
                Telefone,
                Contato,
                Email
            )
            VALUES (?, ?, ?, ?, ?)
        """, (
            nome,
            cnpj,
            telefone,
            contato,
            email
        ))

        conn.commit()
        conn.close()

    @staticmethod
    def excluir(id_registro):

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            UPDATE Fornecedores
            SET Ativo = 0
            WHERE Id = ?
        """, (id_registro,))

        conn.commit()
        conn.close()
