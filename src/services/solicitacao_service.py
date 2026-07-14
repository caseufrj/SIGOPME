from database.database_service import DatabaseService


class SolicitacaoService:

    @staticmethod
    def buscar_item(texto):

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM EstoqueRastreado
            WHERE

                CodigoBarras = ?

                OR Lote = ?

                OR CodigoUnico = ?

                OR CodItem = ?
        """, (
            texto,
            texto,
            texto,
            texto
        ))

        resultado = cursor.fetchone()

        conn.close()

        return resultado
