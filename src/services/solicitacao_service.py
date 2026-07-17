from database.database_service import DatabaseService


class SolicitacaoService:

    # =========================
    # SOLICITAÇÕES
    # =========================

    @staticmethod
    def inserir(
        numero_solicitacao,
        data_solicitacao,
        cirurgia,
        paciente_registro,
        especialidade,
        observacao,
        usuario
    ):

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO Solicitacoes (

                NumeroSolicitacao,
                DataSolicitacao,
                Cirurgia,
                PacienteRegistro,
                Especialidade,
                Observacao,
                Usuario

            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (

            numero_solicitacao,
            data_solicitacao,
            cirurgia,
            paciente_registro,
            especialidade,
            observacao,
            usuario

        ))

        solicitacao_id = cursor.lastrowid

        conn.commit()

        conn.close()

        return solicitacao_id


    @staticmethod
    def listar_todas():

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            SELECT

                Id,
                NumeroSolicitacao,
                DataSolicitacao,
                Cirurgia,
                PacienteRegistro,
                Especialidade,
                Usuario

            FROM Solicitacoes

            ORDER BY Id DESC
        """)

        dados = cursor.fetchall()

        conn.close()

        return dados


    @staticmethod
    def obter_por_id(id_solicitacao):

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM Solicitacoes
            WHERE Id = ?
        """, (id_solicitacao,))

        dados = cursor.fetchone()

        conn.close()

        return dados


    @staticmethod
    def excluir(id_solicitacao):

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            DELETE
            FROM Solicitacoes
            WHERE Id = ?
        """, (id_solicitacao,))

        conn.commit()

        conn.close()


    # =========================
    # RASTREABILIDADE
    # =========================

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


    @staticmethod
    def utilizado(
        id_item,
        data_utilizacao
    ):

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            UPDATE EstoqueRastreado
            SET

                Status = 'UTILIZADO',

                DataUtilizacao = ?

            WHERE Id = ?
        """, (
            data_utilizacao,
            id_item
        ))

        conn.commit()

        conn.close()


    @staticmethod
    def devolver(
        id_item,
        data_devolucao
    ):

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            UPDATE EstoqueRastreado
            SET

                Status = 'DISPONIVEL',

                DataDevolucao = ?

            WHERE Id = ?
        """, (

            data_devolucao,
            id_item

        ))

        conn.commit()

        conn.close()
