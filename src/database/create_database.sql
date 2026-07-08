PRAGMA foreign_keys = ON;

-- =========================
-- USUÁRIOS
-- =========================

CREATE TABLE IF NOT EXISTS Usuarios (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Login TEXT NOT NULL UNIQUE,
    SenhaHash TEXT NOT NULL,
    Perfil TEXT NOT NULL,
    Ativo INTEGER NOT NULL DEFAULT 1,
    DataCriacao DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- =========================
-- CONFIGURAÇÕES
-- =========================

CREATE TABLE IF NOT EXISTS Configuracoes (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    NomeHospital TEXT,
    CaminhoBackup TEXT,
    UltimoBackup DATETIME
);

-- =========================
-- LICITAÇÕES
-- =========================

CREATE TABLE IF NOT EXISTS Licitacoes (

    Id INTEGER PRIMARY KEY AUTOINCREMENT,

    NumeroLicitacao TEXT NOT NULL,
    TipoLicitacao TEXT,

    Ata TEXT,

    Consignado TEXT,
    Contrato TEXT,
    NumeroContrato TEXT,

    Processo TEXT,
    Vigencia TEXT,

    Fornecedor TEXT,
    Cnpj TEXT,

    CodConsig TEXT,
    CodItem TEXT NOT NULL,

    Sirep TEXT,

    NomeMaterial TEXT NOT NULL,

    QtdLicitada INTEGER NOT NULL,

    ValorUnd REAL NOT NULL,

    RP TEXT,
    SC TEXT,

    Especialidade TEXT,

    Ativo INTEGER DEFAULT 1,

    DataCriacao DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- =========================
-- TIPOS DE MOVIMENTAÇÃO
-- =========================

CREATE TABLE IF NOT EXISTS TiposMovimentacao (

    Id INTEGER PRIMARY KEY AUTOINCREMENT,

    Nome TEXT NOT NULL UNIQUE
);

-- =========================
-- MOVIMENTAÇÕES
-- =========================

CREATE TABLE IF NOT EXISTS Movimentacoes (

    Id INTEGER PRIMARY KEY AUTOINCREMENT,

    DataMovimento DATETIME NOT NULL,

    NumeroLicitacao TEXT NOT NULL,

    CodItem TEXT NOT NULL,

    TipoMovimento TEXT NOT NULL CHECK (
        TipoMovimento IN (
            'ENTRADA_CONSIGNACAO',
            'ENTRADA_VENDA',
            'RETIRADO',
            'UTILIZADO',
            'DEVOLVIDO',
            'EXTRAVIADO',
            'PAGO'
        )
    )

    Quantidade INTEGER NOT NULL,

    ValorUnitario REAL,

    DocumentoOrigem TEXT,

    Observacao TEXT,

    Usuario TEXT,

    DataCriacao DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- =========================
-- NOTAS FISCAIS
-- =========================

CREATE TABLE IF NOT EXISTS NotasFiscais (

    Id INTEGER PRIMARY KEY AUTOINCREMENT,

    NumeroNF TEXT NOT NULL,

    ChaveAcesso TEXT,

    DataNF DATETIME NOT NULL,

    Fornecedor TEXT NOT NULL,

    Cnpj TEXT,

    TipoNota TEXT NOT NULL,

    ValorTotal REAL,

    Status TEXT DEFAULT 'ABERTA',

    Observacao TEXT,

    DataCriacao DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- =========================
-- ITENS DA NF
-- =========================

CREATE TABLE IF NOT EXISTS NotaItens (

    Id INTEGER PRIMARY KEY AUTOINCREMENT,

    NotaFiscalId INTEGER NOT NULL,

    CodItem TEXT NOT NULL,

    NomeItem TEXT NOT NULL,

    Quantidade INTEGER NOT NULL,

    ValorUnitario REAL,

    ValorTotal REAL,

    FOREIGN KEY (NotaFiscalId)
    REFERENCES NotasFiscais(Id)
);

-- =========================
-- SOLICITAÇÕES
-- =========================

CREATE TABLE IF NOT EXISTS Solicitacoes (

    Id INTEGER PRIMARY KEY AUTOINCREMENT,

    NumeroSolicitacao TEXT,

    DataSolicitacao DATETIME NOT NULL,

    Cirurgia TEXT,

    PacienteRegistro TEXT,

    Especialidade TEXT,

    Observacao TEXT,

    Usuario TEXT,

    DataCriacao DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- =========================
-- ITENS SOLICITADOS
-- =========================

CREATE TABLE IF NOT EXISTS SolicitacaoItens (

    Id INTEGER PRIMARY KEY AUTOINCREMENT,

    SolicitacaoId INTEGER NOT NULL,

    CodItem TEXT NOT NULL,

    NomeItem TEXT NOT NULL,

    Quantidade INTEGER NOT NULL,

    Status TEXT NOT NULL CHECK (
        Status IN (
            'SOLICITADO',
            'RETIRADO',
            'UTILIZADO',
            'DEVOLVIDO',
            'EXTRAVIADO',
            'PAGO'
        )
    ),

    FOREIGN KEY (SolicitacaoId)
    REFERENCES Solicitacoes(Id)
);

-- =========================
-- ÍNDICES
-- =========================

CREATE INDEX IF NOT EXISTS IDX_LICITACOES_CODIGO
ON Licitacoes (CodItem);

CREATE INDEX IF NOT EXISTS IDX_LICITACOES_FORNECEDOR
ON Licitacoes (Fornecedor);

CREATE INDEX IF NOT EXISTS IDX_LICITACOES_ATA
ON Licitacoes (Ata);

CREATE INDEX IF NOT EXISTS IDX_MOVIMENTACOES_ITEM
ON Movimentacoes (CodItem);

CREATE INDEX IF NOT EXISTS IDX_MOVIMENTACOES_LICITACAO
ON Movimentacoes (NumeroLicitacao);

-- =========================
-- AUDITORIA
-- =========================

CREATE TABLE IF NOT EXISTS Auditoria (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,

    Usuario TEXT NOT NULL,

    Acao TEXT NOT NULL,

    Tabela TEXT NOT NULL,

    RegistroId INTEGER,

    DataHora DATETIME DEFAULT CURRENT_TIMESTAMP
);
