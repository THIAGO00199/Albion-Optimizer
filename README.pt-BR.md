# Albion Optimizer — Calculadora de craft e lucro de poções

Otimizador em linha de comando para receitas de poções do Albion Online. Compara opções de fabricação usando preços e premissas informados pelo próprio jogador.

## Funcionalidades

- Receitas de poções dos tiers T2–T8.
- Cálculo de quantidades de craft e materiais.
- Modelagem da taxa de retorno de recursos (RRR) a partir do bônus de produção informado.
- Custos de estação, impostos de venda, taxas, materiais, receita, lucro e ROI estimado.
- Cálculo de eficiência de Focus quando os dados da receita estão disponíveis.
- Ranking de estratégias conforme preços de mercado e restrições informados pelo jogador.

## Executar

Requisitos: Python 3.10+; a implementação atual usa apenas a biblioteca padrão do Python.

```bash
python3 main.py
```

O programa solicita prata disponível, reserva desejada, premissas de Focus/Premium, bônus de produção, impostos, preços de materiais e preços de venda. É possível comparar várias receitas ou calcular uma poção específica.

## Premissas e limitações

- Preços e taxas são informados pelo usuário; não há consulta de mercado em tempo real.
- Receitas e quantidades são dados locais e podem precisar de atualização após patches do jogo.
- Esta versão assume cinco poções por craft.
- O retorno de recursos é tratado como valor esperado; arredondamentos exatos no jogo e alguns valores de receita/Focus ainda precisam de validação.
- Lucro e ROI são estimativas, não garantias de resultado no mercado.

---

[Português](./README.pt-BR.md) · [English](./README.md) · [Español](./README.es.md)
