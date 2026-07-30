from database.database_service import DatabaseService
from protocolo_rastreabilidade import ProtocoloRastreabilidade

class ProtocoloRastreabilidadeService:

    @staticmethod
    def atualizar_protocolo(
        protocolo_id,
        data_retirada
    ):

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            UPDATE Solicitacoes
            SET DataSolicitacao = ?
            WHERE Id = ?
        """, (
            data_retirada,
            protocolo_id
        ))

        conn.commit()
        conn.close()

    @staticmethod
    def obter_protocolo_completo(protocolo):
    
        conn = DatabaseService.get_connection()
    
        cursor = conn.cursor()
    
        cursor.execute("""
            SELECT
    
                s.Id,
                s.PacienteRegistro,
                s.PacienteNome,
    
                si.CodItem,
                si.NomeItem,
                si.Lote,
                si.Status,
    
                s.DataSolicitacao
    
            FROM Solicitacoes s
    
            INNER JOIN SolicitacaoItens si
                ON si.SolicitacaoId = s.Id
    
            WHERE s.Id = ?
    
            LIMIT 1
    
        """, (protocolo,))
    
        resultado = cursor.fetchone()
    
        print(resultado)
    
        conn.close()
    
        if not resultado:
            return None
    
        return ProtocoloRastreabilidade(
    
            protocolo=resultado[0],
    
            registro=resultado[1] or "",
    
            paciente=resultado[2] or "",
    
            codigo_item=resultado[3] or "",
    
            nome_material=resultado[4] or "",
    
            lote=resultado[5] or "",
    
            status=resultado[6] or "",
    
            data_retirada=resultado[7]
    
        )
