from database.database_service import DatabaseService


class EstoqueRastreadoService:

    @staticmethod
    def inserir(
        licitacao_item_id,
        numero_licitacao,
        cod_item,
        nome_material,
        lote,
        codigo_unico,
        data_validade,
        numero_nf
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
            
                NumeroNF,
            
                Status
            
            )
            VALUES (

                ?, ?, ?, ?, ?, ?, ?, ?,
            
                'DISPONIVEL'
            )
        """, (
            licitacao_item_id,
        
            numero_licitacao,
        
            cod_item,
        
            nome_material,
        
            lote,
        
            codigo_unico,
        
            codigo_barras,
        
            numero_nf
        ))

        conn.commit()

        conn.close()

    @staticmethod
    def registrar_retirada(
        id_item,
        paciente_nome,
        paciente_registro,
        data_retirada
    ):
    
        conn = DatabaseService.get_connection()
    
        cursor = conn.cursor()
    
        cursor.execute("""
            UPDATE EstoqueRastreado
            SET
    
                Status = 'RETIRADO',
    
                PacienteNome = ?,
    
                PacienteRegistro = ?,
    
                DataRetirada = ?
    
            WHERE Id = ?
        """, (
    
            paciente_nome,
    
            paciente_registro,
    
            data_retirada,
    
            id_item
    
        ))
    
        conn.commit()
    
        conn.close()

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
    
                PacienteId = NULL,
    
                PacienteRegistro = NULL,
    
                PacienteNome = NULL,
    
                Sala = NULL,
    
                DataDevolucao = ?
    
            WHERE Id = ?
        """, (
            data_devolucao,
            id_item
        ))
    
        conn.commit()
    
        conn.close()
