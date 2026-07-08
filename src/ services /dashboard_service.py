from database.database_service import DatabaseService


class DashboardService:

    @staticmethod
    def total_atas_vigentes():

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            SELECT COUNT(DISTINCT Ata)
            FROM Licitacoes
            WHERE Ativo = 1
        """)

        total = cursor.fetchone()[0]

        conn.close()

        return total

    @staticmethod
    def total_fornecedores():

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            SELECT COUNT(DISTINCT Fornecedor)
            FROM Licitacoes
            WHERE Ativo = 1
        """)

        total = cursor.fetchone()[0]

        conn.close()

        return total

    @staticmethod
    def total_itens():

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            SELECT COUNT(DISTINCT CodItem)
            FROM Licitacoes
            WHERE Ativo = 1
        """)

        total = cursor.fetchone()[0]

        conn.close()

        return total

    @staticmethod
    def saldo_financeiro_total():

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                COALESCE(
                    SUM(QtdLicitada * ValorUnd),
                    0
                )
            FROM Licitacoes
            WHERE Ativo = 1
        """)

        total = cursor.fetchone()[0]

        conn.close()

        return total

    @staticmethod
    def total_em_consignacao():

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                COALESCE(SUM(
                    CASE
                        WHEN TipoMovimento = 'ENTRADA_CONSIGNACAO'
                        THEN Quantidade
                        ELSE 0
                    END
                ), 0)

                -

                COALESCE(SUM(
                    CASE
                        WHEN TipoMovimento = 'UTILIZADO'
                        THEN Quantidade
                        ELSE 0
                    END
                ), 0)

                -

                COALESCE(SUM(
                    CASE
                        WHEN TipoMovimento = 'DEVOLVIDO'
                        THEN Quantidade
                        ELSE 0
                    END
                ), 0)

                -

                COALESCE(SUM(
                    CASE
                        WHEN TipoMovimento = 'EXTRAVIADO'
                        THEN Quantidade
                        ELSE 0
                    END
                ), 0)

            FROM Movimentacoes
        """)

        total = cursor.fetchone()[0]

        conn.close()

        return total

    @staticmethod
    def total_em_pagamento():

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            SELECT

                COALESCE(SUM(
                    CASE
                        WHEN TipoMovimento = 'UTILIZADO'
                        THEN Quantidade
                        ELSE 0
                    END
                ), 0)

                -

                COALESCE(SUM(
                    CASE
                        WHEN TipoMovimento = 'PAGO'
                        THEN Quantidade
                        ELSE 0
                    END
                ), 0)

            FROM Movimentacoes
        """)

        total = cursor.fetchone()[0]

        conn.close()

        return total

    @staticmethod
    def total_extraviado():

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                COALESCE(
                    SUM(Quantidade),
                    0
                )
            FROM Movimentacoes
            WHERE TipoMovimento = 'EXTRAVIADO'
        """)

        total = cursor.fetchone()[0]

        conn.close()

        return total

    @staticmethod
    def ultimas_movimentacoes(limite=10):

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                DataMovimento,
                CodItem,
                TipoMovimento,
                Quantidade,
                Usuario
            FROM Movimentacoes
            ORDER BY DataMovimento DESC
            LIMIT ?
        """, (limite,))

        registros = cursor.fetchall()

        conn.close()

        return registros
