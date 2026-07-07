# SIGOPME - Regras de Negócio

## Objetivo

Controlar OPME em consignação e venda, vinculados a licitações, atas, contratos e solicitações cirúrgicas.

---

# LICITAÇÕES

As licitações representam a origem dos saldos disponíveis.

Cada item deverá possuir:

- Número da Licitação
- Ata
- Fornecedor
- CNPJ
- Código do Item
- Nome do Material
- Quantidade Licitada
- Valor Unitário
- Especialidade
- Vigência

---

# TIPOS DE ENTRADA

## Entrada de Consignação

Ao lançar uma nota de consignação:

- Adicionar quantidade em consignação
- Reduzir saldo pedido
- Não alterar saldo financeiro

### Exemplo

Qtd Licitada: 100

Entrada Consignação: 10

Resultado:

Saldo Pedido: 90
Em Consignação: 10
Saldo Financeiro: sem alteração

---

## Entrada de Venda

Ao lançar uma nota de venda:

- Reduzir saldo pedido
- Reduzir saldo financeiro

### Exemplo

Qtd Licitada: 100

Entrada Venda: 10

Resultado:

Saldo Pedido: 90
Saldo Financeiro:
(100 - 10) × valor unitário

---

# SOLICITAÇÕES CIRÚRGICAS

Uma solicitação poderá conter vários itens.

Cada item deverá possuir:

- Código
- Nome
- Quantidade
- Status

---

# STATUS DOS ITENS

## SOLICITADO

Item solicitado para cirurgia.

Não altera saldos.

---

## RETIRADO

Item retirado da consignação.

Atualiza:

- Retirado

---

## UTILIZADO

Item efetivamente utilizado.

Atualiza:

- Utilizado
- Em Pagamento

---

## DEVOLVIDO

Item devolvido ao fornecedor.

Atualiza:

- Devolvido

---

## EXTRAVIADO

Item perdido ou não localizado.

Atualiza:

- Extraviado
- Saldo Financeiro

---

## PAGO

Item pago ao fornecedor.

Atualiza:

- Pago
- Reduz Em Pagamento
- Reduz Saldo Financeiro

---

# CÁLCULOS

## Em Consignação

Em Consignação =
Entrada Consignação
- Utilizado
- Devolvido
- Extraviado

---

## Em Pagamento

Em Pagamento =
Utilizado
- Pago

---

## Saldo Pedido

Saldo Pedido =
Qtd Licitada
- Entrada Consignação
- Entrada Venda

---

## Saldo Financeiro

Saldo Financeiro =
(Qtd Licitada × Valor Unitário)
- (Pago × Valor Unitário)
- (Extraviado × Valor Unitário)

---

# AUDITORIA

Toda movimentação deverá registrar:

- Data
- Hora
- Usuário
- Tipo de Movimentação
- Quantidade
- Observação

Nenhuma movimentação poderá ser excluída fisicamente.

Utilizar cancelamento ou estorno.
