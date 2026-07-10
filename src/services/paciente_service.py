from database.database_service import DatabaseService


class PacienteService:

    @staticmethod
    def listar_todos():

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                Id,
                Registro,
                Nome,
                DataNascimento
            FROM Pacientes
            WHERE Ativo = 1
            ORDER BY Nome
        """)

        resultado = cursor.fetchall()

        conn.close()

        return resultado

    @staticmethod
    def pesquisar(texto):

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                Id,
                Registro,
                Nome,
                DataNascimento
            FROM Pacientes
            WHERE
                Ativo = 1
                AND (
                    UPPER(Registro) LIKE UPPER(?)
                    OR UPPER(Nome) LIKE UPPER(?)
                )
            ORDER BY Nome
        """, (
            f"%{texto}%",
            f"%{texto}%"
        ))

        resultado = cursor.fetchall()

        conn.close()

        return resultado

    @staticmethod
    def obter_por_id(id_registro):

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                Id,
                Registro,
                Nome,
                DataNascimento
            FROM Pacientes
            WHERE Id = ?
        """, (id_registro,))

        resultado = cursor.fetchone()

        conn.close()

        return resultado

    @staticmethod
    def inserir(
        registro,
        nome,
        data_nascimento
    ):

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO Pacientes (
                Registro,
                Nome,
                DataNascimento
            )
            VALUES (?, ?, ?)
        """, (
            registro,
            nome,
            data_nascimento
        ))

        conn.commit()

        conn.close()

    @staticmethod
    def atualizar(
        id_registro,
        registro,
        nome,
        data_nascimento
    ):

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            UPDATE Pacientes
            SET
                Registro = ?,
                Nome = ?,
                DataNascimento = ?
            WHERE Id = ?
        """, (
            registro,
            nome,
            data_nascimento,
            id_registro
        ))

        conn.commit()

        conn.close()

    @staticmethod
    def excluir(id_registro):

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            UPDATE Pacientes
            SET Ativo = 0
            WHERE Id = ?
        """, (id_registro,))

        conn.commit()

        conn.close()
