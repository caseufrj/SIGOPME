from database.database_service import DatabaseService


class HistoricoService:

    @staticmethod
    def registrar(
        estoque_id,
        numero_licitacao,
        cod_item,
        nome_material,
        lote,
        codigo_unico,
        status_anterior,
        status_novo,
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
                NumeroLicitacao,
                CodItem,
                NomeMaterial,
                Lote,
                CodigoUnico,
                StatusAnterior,
                StatusNovo,
                PacienteNome,
                PacienteRegistro,
                Sala,
                Usuario,
                DataMovimento,
                Observacao

            )
            VALUES (

                ?, ?, ?, ?, ?, ?, ?, ?,
                ?, ?, ?, ?, datetime('now'),
                ?

            )
        """, (

            estoque_id,
            numero_licitacao,
            cod_item,
            nome_material,
            lote,
            codigo_unico,
            status_anterior,
            status_novo,
            paciente_nome,
            paciente_registro,
            sala,
            usuario,
            observacao

        ))

        conn.commit()

        conn.close()
