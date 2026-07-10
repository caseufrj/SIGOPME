INSERT OR IGNORE INTO TiposMovimentacao (Nome)
VALUES ('ENTRADA_CONSIGNACAO');

INSERT OR IGNORE INTO TiposMovimentacao (Nome)
VALUES ('ENTRADA_VENDA');

INSERT OR IGNORE INTO TiposMovimentacao (Nome)
VALUES ('RETIRADO');

INSERT OR IGNORE INTO TiposMovimentacao (Nome)
VALUES ('UTILIZADO');

INSERT OR IGNORE INTO TiposMovimentacao (Nome)
VALUES ('DEVOLVIDO');

INSERT OR IGNORE INTO TiposMovimentacao (Nome)
VALUES ('EXTRAVIADO');

INSERT OR IGNORE INTO TiposMovimentacao (Nome)
VALUES ('PAGO');

INSERT OR IGNORE INTO Usuarios (
    Id,
    Nome,
    Login,
    SenhaHash,
    Perfil
)
VALUES (
    1,
    'Administrador',
    'admin',
    'admin',
    'ADMIN'
);

INSERT OR IGNORE INTO Configuracoes (
    Id,
    NomeHospital,
    VersaoSistema
)
VALUES (
    1,
    'HU-CAS/UFRJ',
    '0.1'
);
