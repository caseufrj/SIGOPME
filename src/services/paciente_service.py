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

    dados = cursor.fetchall()

    conn.close()

    return dados
