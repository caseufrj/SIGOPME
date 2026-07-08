CREATE TABLE IF NOT EXISTS Usuarios (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Login TEXT NOT NULL UNIQUE,
    SenhaHash TEXT NOT NULL,
    Perfil TEXT NOT NULL,
    Ativo INTEGER NOT NULL DEFAULT 1,
    DataCriacao DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS Configuracoes (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    NomeHospital TEXT,
    CaminhoBackup TEXT,
    UltimoBackup DATETIME
);

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

    DataCriacao DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS TiposMovimentacao (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS Movimentacoes (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,

    DataMovimento DATETIME NOT NULL,

    NumeroLicitacao TEXT NOT NULL,

    CodItem TEXT NOT NULL,

    TipoMovimento TEXT NOT NULL,

    Quantidade INTEGER NOT NULL,

    Observacao TEXT,

    Usuario TEXT,

    DataCriacao DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS NotasFiscais (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,

    NumeroNF TEXT NOT NULL,

    ChaveAcesso TEXT,

    DataNF DATETIME NOT NULL,

    Fornecedor TEXT NOT NULL,

    Cnpj TEXT,

    TipoNota TEXT NOT NULL,

    ValorTotal REAL,

    Observacao TEXT,

    DataCriacao DATETIME DEFAULT CURRENT_TIMESTAMP
);

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

CREATE TABLE IF NOT EXISTS SolicitacaoItens (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,

    SolicitacaoId INTEGER NOT NULL,

    CodItem TEXT NOT NULL,

    NomeItem TEXT NOT NULL,

    Quantidade INTEGER NOT NULL,

    Status TEXT NOT NULL,

    FOREIGN KEY (SolicitacaoId)
        REFERENCES Solicitacoes(Id)
);

CREATE INDEX IF NOT EXISTS IDX_LICITACOES_CODITEM
ON Licitacoes(CodItem);

CREATE INDEX IF NOT EXISTS IDX_LICITACOES_FORNECEDOR
ON Licitacoes(Fornecedor);

CREATE INDEX IF NOT EXISTS IDX_LICITACOES_ATA
ON Licitacoes(Ata);

CREATE INDEX IF NOT EXISTS IDX_MOVIMENTACOES_CODITEM
ON Movimentacoes(CodItem);
