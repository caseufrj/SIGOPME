from database.database_service import DatabaseService


class LicitacaoService:

    @staticmethod
    def listar_todos():

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                CodItem,
                NomeMaterial,
                Fornecedor,
                Ata,
                QtdLicitada
            FROM Licitacoes
            ORDER BY NomeMaterial
        """)

        resultado = cursor.fetchall()

        conn.close()

        return resultado

    @staticmethod
    def buscar_por_codigo(codigo):

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                CodItem,
                NomeMaterial,
                Fornecedor,
                Ata,
                QtdLicitada
            FROM Licitacoes
            WHERE CodItem LIKE ?
        """, (f"%{codigo}%",))

        resultado = cursor.fetchall()

        conn.close()

        return resultado

    @staticmethod
    def buscar_por_fornecedor(fornecedor):

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                CodItem,
                NomeMaterial,
                Fornecedor,
                Ata,
                QtdLicitada
            FROM Licitacoes
            WHERE Fornecedor LIKE ?
        """, (f"%{fornecedor}%",))

        resultado = cursor.fetchall()

        conn.close()

        return resultado

    @staticmethod
    def buscar_por_ata(ata):

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                CodItem,
                NomeMaterial,
                Fornecedor,
                Ata,
                QtdLicitada
            FROM Licitacoes
            WHERE Ata LIKE ?
        """, (f"%{ata}%",))

        resultado = cursor.fetchall()

        conn.close()

        return resultado

    @staticmethod
    def pesquisar(texto):
    
        conn = DatabaseService.get_connection()
    
        cursor = conn.cursor()
    
        cursor.execute("""
            SELECT
                CodItem,
                NomeMaterial,
                Fornecedor,
                Ata,
                QtdLicitada
            FROM Licitacoes
            WHERE
                CodItem LIKE ?
                OR NomeMaterial LIKE ?
                OR Fornecedor LIKE ?
                OR Ata LIKE ?
            ORDER BY NomeMaterial
        """, (
            f"%{texto}%",
            f"%{texto}%",
            f"%{texto}%",
            f"%{texto}%"
        ))
    
        resultado = cursor.fetchall()
    
        conn.close()
    
        return resultado
