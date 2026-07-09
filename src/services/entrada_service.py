from database.database_service import DatabaseService


class EntradaService:

    @staticmethod
    def listar_todos():

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                Id,
                NumeroNF,
                SerieNF,
                DataEntrada,
                TipoEntrada,
                Fornecedor,
                CodItem,
                NomeMaterial,
                Quantidade
            FROM Entradas
            ORDER BY DataEntrada DESC
        """)

        dados = cursor.fetchall()

        conn.close()

        return dados

    @staticmethod
    def inserir(
        numero_nf,
        serie_nf,
        data_emissao,
        data_entrada,
        tipo_entrada,
        fornecedor,
        codigo_item,
        nome_material,
        quantidade,
        observacao
    ):
        FornecedorService.obter_ou_criar(
            txt_fornecedor.get()
        )
        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO Entradas (
                NumeroNF,
                SerieNF,
                DataEmissao,
                DataEntrada,
                TipoEntrada,
                Fornecedor,
                CodItem,
                NomeMaterial,
                Quantidade,
                Observacao
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            numero_nf,
            serie_nf,
            data_emissao,
            data_entrada,
            tipo_entrada,
            fornecedor,
            codigo_item,
            nome_material,
            quantidade,
            observacao
        ))

        conn.commit()
        conn.close()
