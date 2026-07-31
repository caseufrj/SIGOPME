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
        paciente_nome,
        sala,
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
                PacienteNome,
                Sala,
                Especialidade,
                Observacao,
                Usuario
            
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        
        """, (
        
            (
            numero_solicitacao,
            data_solicitacao,
            cirurgia,
            paciente_registro,
            paciente_nome,
            sala,
            especialidade,
            observacao,
            usuario
        )

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
            SELECT
        
                Id,
                LicitacaoItemId,
                NumeroLicitacao,
                CodItem,
                NomeMaterial,
                Lote,
                CodigoUnico,
                CodigoBarras,
                Quantidade,
                Status,
                PacienteId,
                PacienteRegistro,
                PacienteNome,
                Sala,
                DataEntrada,
                DataRetirada,
                DataUtilizacao,
                DataDevolucao,
                DataExtravio,
                DataPagamento,
                Observacao
        
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

        resultados = cursor.fetchall()

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

    @staticmethod
    def listar_protocolos_abertos():
    
        conn = DatabaseService.get_connection()
    
        cursor = conn.cursor()
    
        cursor.execute("""
            SELECT

                s.Id,
            
                s.PacienteRegistro,
            
                s.PacienteNome,
            
                si.NomeItem,
            
                si.Lote,
            
                si.Status
            
            FROM Solicitacoes s
            
            INNER JOIN SolicitacaoItens si
                ON si.SolicitacaoId = s.Id
            
            WHERE si.Status IN (
                'SOLICITADO',
                'RETIRADO'
            )
            
            ORDER BY s.Id DESC
        """)
    
        dados = cursor.fetchall()
    
        conn.close()
    
        return dados

    @staticmethod
    def buscar_protocolo_por_item(
        cod_item,
        lote
    ):
    
        conn = DatabaseService.get_connection()
    
        cursor = conn.cursor()
    
        cursor.execute("""
            SELECT
    
                s.Id,
    
                s.PacienteRegistro,
    
                s.PacienteNome,
    
                si.Status
    
            FROM Solicitacoes s
    
            INNER JOIN SolicitacaoItens si
                ON si.SolicitacaoId = s.Id
    
            WHERE
    
                si.CodItem = ?
                AND si.Lote = ?
    
                AND si.Status IN (
                    'SOLICITADO',
                    'RETIRADO'
                )
    
            ORDER BY s.Id DESC
    
            LIMIT 1
    
        """, (
    
            cod_item,
            lote
    
        ))
    
        dados = cursor.fetchone()
    
        conn.close()
    
        return dados

    @staticmethod
    def buscar_protocolo_por_item(
        cod_item,
        lote
    ):
    
        conn = DatabaseService.get_connection()
    
        cursor = conn.cursor()
    
        cursor.execute("""
            SELECT
    
                s.Id,
                s.PacienteRegistro,
                s.PacienteNome,
                si.Status
    
            FROM Solicitacoes s
    
            INNER JOIN SolicitacaoItens si
                ON si.SolicitacaoId = s.Id
    
            WHERE
    
                si.CodItem = ?
                AND si.Lote = ?
    
                AND si.Status IN (
                    'SOLICITADO',
                    'RETIRADO'
                )
    
            ORDER BY s.Id DESC
    
            LIMIT 1
        """, (
    
            cod_item,
            lote
    
        ))
    
        resultado = cursor.fetchone()
    
        conn.close()
    
        return resultado

    @staticmethod
    def atualizar_protocolo(
        protocolo_id,
        registro,
        nome,
        data_retirada
    ):
    
        conn = DatabaseService.get_connection()
    
        cursor = conn.cursor()
    
        cursor.execute("""
            UPDATE Solicitacoes
            SET
    
                PacienteRegistro = ?,
                PacienteNome = ?,
                DataSolicitacao = ?
    
            WHERE Id = ?
        """, (
    
            registro,
            nome,
            data_retirada,
            protocolo_id
    
        ))
    
        conn.commit()
        conn.close()

