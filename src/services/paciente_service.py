from database.database_service import DatabaseService


class PacienteService:

    @staticmethod
    def obter_por_registro(registro):

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                Id,
                Registro,
                Nome
            FROM Pacientes
            WHERE Registro = ?
        """, (registro,))

        resultado = cursor.fetchone()

        conn.close()

        return resultado

    @staticmethod
    def obter_por_nome(nome):

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                Id,
                Registro,
                Nome
            FROM Pacientes
            WHERE Nome = ?
        """, (nome,))

        resultado = cursor.fetchone()

        conn.close()

        return resultado

    @staticmethod
    def inserir(
        registro,
        nome
    ):

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO Pacientes (
                Registro,
                Nome
            )
            VALUES (?, ?)
        """, (
            registro,
            nome
        ))

        conn.commit()

        conn.close()
