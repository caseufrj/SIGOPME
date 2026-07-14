from services.database_service import DatabaseService


class EstoqueRastreadoService:

    @staticmethod
    def inserir(
        licitacao_item_id,
        numero_licitacao,
        cod_item,
        nome_material,
        lote,
        codigo_unico
    ):

        codigo_barras = (
            f"{lote}.{codigo_unico}"
        )

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            SELECT 1
            FROM EstoqueRastreado
            WHERE CodigoBarras = ?
        """, (codigo_barras,))

        if cursor.fetchone():

            conn.close()

            raise Exception(
                "Código de barras já cadastrado."
            )

        cursor.execute("""
            INSERT INTO EstoqueRastreado (

                LicitacaoItemId,

                NumeroLicitacao,

                CodItem,

                NomeMaterial,

                Lote,

                CodigoUnico,

                CodigoBarras,

                Status

            )
            VALUES (

                ?, ?, ?, ?, ?, ?, ?,

                'DISPONIVEL'
            )

        """, (

            licitacao_item_id,

            numero_licitacao,

            cod_item,

            nome_material,

            lote,

            codigo_unico,

            codigo_barras

        ))

        conn.commit()

        conn.close()
