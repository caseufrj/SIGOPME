# SIGOPME - Movimentações

## Objetivo

Toda alteração de saldo do sistema deverá ocorrer através de movimentações.

Nenhum saldo será digitado manualmente.

Todos os indicadores serão calculados automaticamente.

---

# Tipos de Movimentação

## ENTRADA_CONSIGNACAO

Material recebido em consignação.

Efeitos:

- Aumenta Em Consignação
- Reduz Saldo Pedido
- Não altera Saldo Financeiro

---

## ENTRADA_VENDA

Material recebido através de nota de venda.

Efeitos:

- Reduz Saldo Pedido
- Reduz Saldo Financeiro

---

## RETIRADO

Material separado para cirurgia.

Efeitos:

- Aumenta Retirado

---

## UTILIZADO

Material efetivamente utilizado.

Efeitos:

- Aumenta Utilizado
- Aumenta Em Pagamento

---

## DEVOLVIDO

Material devolvido ao fornecedor.

Efeitos:

- Reduz Em Consignação

---

## EXTRAVIADO

Material perdido.

Efeitos:

- Aumenta Extraviado
- Reduz Saldo Financeiro

---

## PAGO

Material faturado e pago.

Efeitos:

- Aumenta Pago
- Reduz Em Pagamento
- Reduz Saldo Financeiro
