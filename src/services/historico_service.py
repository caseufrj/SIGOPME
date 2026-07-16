from database.database_service import DatabaseService


class HistoricoService:

    @staticmethod
    def registrar(

        estoque_id=None,

        tipo=None,
        acao=None,

        numero_licitacao=None,

        fornecedor=None,
        documento=None,

        cod_item=None,
        nome_material=None,

        lote=None,
        codigo_unico=None,

        paciente_nome=None,
        paciente_registro=None,

        sala=None,

        usuario="Sistema",

        observacao=""

    ):

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""

            INSERT INTO HistoricoMovimentacao (

                EstoqueId,

                Tipo,
                Acao,

                NumeroLicitacao,

                Fornecedor,
                Documento,

                CodItem,
                NomeMaterial,

                Lote,
                CodigoUnico,

                PacienteNome,
                PacienteRegistro,

                Sala,

                Usuario,

                DataMovimento,

                Observacao

            )

            VALUES (

                ?,

                ?,
                ?,

                ?,

                ?,
                ?,

                ?,
                ?,

                ?,
                ?,

                ?,
                ?,

                ?,
                ?,

                datetime('now'),

                ?

            )

        """, (

            estoque_id,

            tipo,
            acao,

            numero_licitacao,

            fornecedor,
            documento,

            cod_item,
            nome_material,

            lote,
            codigo_unico,

            paciente_nome,
            paciente_registro,

            sala,

            usuario,

            observacao

        ))

        conn.commit()

        conn.close()
