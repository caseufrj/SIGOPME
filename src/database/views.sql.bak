-- ==========================================
-- ITENS EM CONSIGNAÇÃO
-- ==========================================

CREATE VIEW IF NOT EXISTS vw_ItensConsignacao AS
SELECT
    l.CodItem,
    l.NomeMaterial,
    l.Fornecedor,
    l.Ata,

    COALESCE(SUM(
        CASE
            WHEN m.TipoMovimento = 'ENTRADA_CONSIGNACAO'
            THEN m.Quantidade
            ELSE 0
        END
    ), 0)

    -

    COALESCE(SUM(
        CASE
            WHEN m.TipoMovimento = 'UTILIZADO'
            THEN m.Quantidade
            ELSE 0
        END
    ), 0)

    -

    COALESCE(SUM(
        CASE
            WHEN m.TipoMovimento = 'DEVOLVIDO'
            THEN m.Quantidade
            ELSE 0
        END
    ), 0)

    -

    COALESCE(SUM(
        CASE
            WHEN m.TipoMovimento = 'EXTRAVIADO'
            THEN m.Quantidade
            ELSE 0
        END
    ), 0)

    AS EmConsignacao

FROM Licitacoes l
LEFT JOIN Movimentacoes m
    ON l.CodItem = m.CodItem

GROUP BY
    l.CodItem,
    l.NomeMaterial,
    l.Fornecedor,
    l.Ata;

-- ==========================================
-- ITENS EM PAGAMENTO
-- ==========================================

CREATE VIEW IF NOT EXISTS vw_ItensPagamento AS
SELECT
    l.CodItem,
    l.NomeMaterial,
    l.Fornecedor,

    COALESCE(SUM(
        CASE
            WHEN m.TipoMovimento = 'UTILIZADO'
            THEN m.Quantidade
            ELSE 0
        END
    ), 0)

    -

    COALESCE(SUM(
        CASE
            WHEN m.TipoMovimento = 'PAGO'
            THEN m.Quantidade
            ELSE 0
        END
    ), 0)

    AS EmPagamento

FROM Licitacoes l
LEFT JOIN Movimentacoes m
    ON l.CodItem = m.CodItem

GROUP BY
    l.CodItem,
    l.NomeMaterial,
    l.Fornecedor;

-- ==========================================
-- SALDO DO PEDIDO
-- ==========================================

CREATE VIEW IF NOT EXISTS vw_SaldoPedido AS
SELECT
    l.CodItem,
    l.NomeMaterial,
    l.Fornecedor,
    l.QtdLicitada,

    l.QtdLicitada

    -

    COALESCE(SUM(
        CASE
            WHEN m.TipoMovimento IN (
                'ENTRADA_CONSIGNACAO',
                'ENTRADA_VENDA'
            )
            THEN m.Quantidade
            ELSE 0
        END
    ), 0)

    AS SaldoPedido

FROM Licitacoes l
LEFT JOIN Movimentacoes m
    ON l.CodItem = m.CodItem

GROUP BY
    l.Id;

-- ==========================================
-- SALDO FINANCEIRO
-- ==========================================

CREATE VIEW IF NOT EXISTS vw_SaldoFinanceiro AS
SELECT
    l.CodItem,
    l.NomeMaterial,
    l.Fornecedor,

    (
        (l.QtdLicitada * l.ValorUnd)

        -

        (
            COALESCE(SUM(
                CASE
                    WHEN m.TipoMovimento = 'PAGO'
                    THEN m.Quantidade
                    ELSE 0
                END
            ), 0) * l.ValorUnd
        )

        -

        (
            COALESCE(SUM(
                CASE
                    WHEN m.TipoMovimento = 'EXTRAVIADO'
                    THEN m.Quantidade
                    ELSE 0
                END
            ), 0) * l.ValorUnd
        )
    )

    AS SaldoFinanceiro

FROM Licitacoes l
LEFT JOIN Movimentacoes m
    ON l.CodItem = m.CodItem

GROUP BY
    l.Id;

-- ==========================================
-- ATAS VIGENTES
-- ==========================================

CREATE VIEW IF NOT EXISTS vw_AtasVigentes AS
SELECT
    Ata,
    NumeroLicitacao,
    Fornecedor,
    Vigencia,
    Especialidade
FROM Licitacoes
WHERE Ativo = 1;

-- ==========================================
-- DASHBOARD RESUMO
-- ==========================================

CREATE VIEW IF NOT EXISTS vw_DashboardResumo AS
SELECT

    COUNT(DISTINCT Ata) AS TotalAtas,

    COUNT(DISTINCT Fornecedor) AS TotalFornecedores,

    COUNT(DISTINCT CodItem) AS TotalItens

FROM Licitacoes
WHERE Ativo = 1;
