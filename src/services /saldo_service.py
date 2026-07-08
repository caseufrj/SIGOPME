from database.database_service import DatabaseService


class SaldoService:

    @staticmethod
    def saldo_pedido(cod_item):

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                QtdLicitada
            FROM Licitacoes
            WHERE CodItem = ?
        """, (cod_item,))

        resultado = cursor.fetchone()

        if not resultado:
            conn.close()
            return 0

        qtd_licitada = resultado[0]

        cursor.execute("""
            SELECT
                COALESCE(SUM(Quantidade), 0)
            FROM Movimentacoes
            WHERE CodItem = ?
            AND TipoMovimento IN (
                'ENTRADA_CONSIGNACAO',
                'ENTRADA_VENDA'
            )
        """, (cod_item,))

        total_entradas = cursor.fetchone()[0]

        conn.close()

        return qtd_licitada - total_entradas

    @staticmethod
    def em_consignacao(cod_item):

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
                ), 0),

                COALESCE(SUM(
                    CASE
                        WHEN TipoMovimento = 'UTILIZADO'
                        THEN Quantidade
                        ELSE 0
                    END
                ), 0),

                COALESCE(SUM(
                    CASE
                        WHEN TipoMovimento = 'DEVOLVIDO'
                        THEN Quantidade
                        ELSE 0
                    END
                ), 0),

                COALESCE(SUM(
                    CASE
                        WHEN TipoMovimento = 'EXTRAVIADO'
                        THEN Quantidade
                        ELSE 0
                    END
                ), 0)

            FROM Movimentacoes
            WHERE CodItem = ?
        """, (cod_item,))

        entrada, utilizado, devolvido, extraviado = cursor.fetchone()

        conn.close()

        return entrada - utilizado - devolvido - extraviado

    @staticmethod
    def em_pagamento(cod_item):

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
                ), 0),

                COALESCE(SUM(
                    CASE
                        WHEN TipoMovimento = 'PAGO'
                        THEN Quantidade
                        ELSE 0
                    END
                ), 0)

            FROM Movimentacoes
            WHERE CodItem = ?
        """, (cod_item,))

        utilizado, pago = cursor.fetchone()

        conn.close()

        return utilizado - pago

    @staticmethod
    def total_pago(cod_item):

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                COALESCE(SUM(Quantidade), 0)
            FROM Movimentacoes
            WHERE CodItem = ?
            AND TipoMovimento = 'PAGO'
        """, (cod_item,))

        resultado = cursor.fetchone()[0]

        conn.close()

        return resultado

    @staticmethod
    def total_extraviado(cod_item):

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                COALESCE(SUM(Quantidade), 0)
            FROM Movimentacoes
            WHERE CodItem = ?
            AND TipoMovimento = 'EXTRAVIADO'
        """, (cod_item,))

        resultado = cursor.fetchone()[0]

        conn.close()

        return resultado

