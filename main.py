#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================
ALBION ONLINE - CRAFTING OPTIMIZER
============================================================

MVP DO PROJETO

MENU:

1 - ANALISAR MELHOR PRODUÇÃO
    - pergunta sua prata
    - pergunta quanto você quer guardar
    - pergunta Focus
    - pergunta Premium
    - pergunta Production Bonus
    - pergunta taxas
    - pergunta preços dos materiais
    - pergunta preços de venda das poções
    - testa várias poções, encantamentos e quantidades
    - mostra as 3 melhores estratégias

2 - CALCULAR UMA POÇÃO
    - escolhe poção
    - escolhe encantamento
    - escolhe quantidade final
    - calcula crafts
    - calcula materiais
    - calcula custo
    - calcula RRR
    - calcula taxas
    - calcula lucro
    - calcula ROI
    - mostra Focus, tempo e peso quando disponíveis

3 - VER RECEITAS

0 - SAIR

============================================================
IMPORTANTE
============================================================

- Os preços são informados pelo usuário.
- As taxas são informadas pelo usuário.
- As receitas são dados fixos do programa.
- Todas as poções produzem 5 por craft nesta versão.
- RRR é tratado como retorno esperado em valor.
- O arredondamento exato do retorno de recursos do jogo
  ainda precisa ser validado.
"""


from __future__ import annotations

from dataclasses import dataclass
from typing import Optional
import math


# ============================================================
# MODELOS
# ============================================================

@dataclass(frozen=True)
class Ingrediente:
    nome: str
    quantidade: int


@dataclass(frozen=True)
class Receita:
    nome: str
    tier: int
    ingredientes: tuple[Ingrediente, ...]
    producao_por_craft: int = 5
    focus_base: Optional[float] = None
    tempo_craft: Optional[float] = None
    peso_pocao: Optional[float] = None


def I(nome: str, quantidade: int) -> Ingrediente:
    return Ingrediente(nome, quantidade)


# ============================================================
# RECEITAS
# ============================================================

RECEITAS = [

    # ========================================================
    # T2
    # ========================================================

    Receita(
        "Minor Healing Potion",
        2,
        (I("Arcane Agaric", 8),),
        5,
        56,
        0.1,
        0.1,
    ),

    Receita(
        "Minor Energy Potion",
        2,
        (I("Arcane Agaric", 8),),
        5,
        56,
        0.1,
        0.1,
    ),

    # ========================================================
    # T3
    # ========================================================

    Receita(
        "Minor Gigantify Potion",
        3,
        (I("Brightleaf Comfrey", 8),),
        5,
        56,
        0.1,
        0.1,
    ),

    Receita(
        "Minor Resistance Potion",
        3,
        (I("Brightleaf Comfrey", 8),),
        5,
        56,
        0.1,
        0.1,
    ),

    Receita(
        "Minor Sticky Potion",
        3,
        (I("Brightleaf Comfrey", 8),),
        5,
    ),

    Receita(
        "Minor Calming Potion",
        3,
        (
            I("Rugged Shadow Claws", 1),
            I("Brightleaf Comfrey", 16),
        ),
        5,
        56,
        0.3,
        0.1,
    ),

    Receita(
        "Minor Cleansing Potion",
        3,
        (
            I("Rugged Sylvian Root", 1),
            I("Brightleaf Comfrey", 16),
        ),
        5,
        56,
        0.3,
        0.1,
    ),

    Receita(
        "Minor Acid Potion",
        3,
        (
            I("Rugged Spirit Paws", 1),
            I("Brightleaf Comfrey", 16),
        ),
        5,
        56,
        0.3,
        0.1,
    ),

    # ========================================================
    # T4
    # ========================================================

    Receita(
        "Healing Potion",
        4,
        (
            I("Crenellated Burdock", 24),
            I("Hen Eggs", 6),
        ),
        5,
        210,
        0.5,
        0.3,
    ),

    Receita(
        "Energy Potion",
        4,
        (
            I("Crenellated Burdock", 24),
            I("Goat's Milk", 6),
        ),
        5,
        210,
        0.5,
        0.3,
    ),

    Receita(
        "Minor Poison Potion",
        4,
        (
            I("Crenellated Burdock", 8),
            I("Brightleaf Comfrey", 4),
        ),
        5,
        84,
        0.2,
        0.14,
    ),

    Receita(
        "Minor Berserk Potion",
        4,
        (
            I("Rugged Werewolf Fangs", 1),
            I("Crenellated Burdock", 16),
        ),
    ),

    Receita(
        "Minor Hellfire Potion",
        4,
        (
            I("Rugged Imp's Horn", 1),
            I("Goat's Milk", 16),
        ),
    ),

    Receita(
        "Minor Gathering Potion",
        4,
        (
            I("Rugged Runestone Tooth", 1),
            I("Goat's Butter", 16),
        ),
        5,
        61,
        0.3,
        0.1,
    ),

    Receita(
        "Minor Tornado in a Bottle",
        4,
        (
            I("Rugged Dawnfeather", 1),
            I("Crenellated Burdock", 16),
        ),
    ),

    # ========================================================
    # T5
    # ========================================================

    Receita(
        "Gigantify Potion",
        5,
        (
            I("Dragon Teasel", 24),
            I("Crenellated Burdock", 12),
            I("Goose Eggs", 6),
        ),
    ),

    Receita(
        "Resistance Potion",
        5,
        (
            I("Dragon Teasel", 24),
            I("Crenellated Burdock", 12),
            I("Goat's Milk", 6),
        ),
        5,
        294,
        0.7,
        0.42,
    ),

    Receita(
        "Sticky Potion",
        5,
        (
            I("Dragon Teasel", 24),
            I("Crenellated Burdock", 12),
            I("Goose Eggs", 6),
        ),
        5,
        294,
        0.7,
        0.42,
    ),

    Receita(
        "Calming Potion",
        5,
        (
            I("Fine Shadow Claws", 1),
            I("Dragon Teasel", 48),
            I("Crenellated Burdock", 24),
            I("Arcane Agaric", 12),
        ),
        5,
        294,
        1.3,
        0.42,
    ),

    Receita(
        "Cleansing Potion",
        5,
        (
            I("Fine Sylvian Root", 1),
            I("Dragon Teasel", 48),
            I("Brightleaf Comfrey", 24),
            I("Goat's Butter", 12),
        ),
        5,
        298,
        1.4,
        0.42,
    ),

    Receita(
        "Acid Potion",
        5,
        (
            I("Fine Spirit Paws", 1),
            I("Dragon Teasel", 48),
            I("Crenellated Burdock", 24),
            I("Goat's Milk", 12),
        ),
    ),

    # ========================================================
    # T6
    # ========================================================

    Receita(
        "Major Healing Potion",
        6,
        (
            I("Elusive Foxglove", 72),
            I("Goose Eggs", 18),
            I("Potato Schnapps", 18),
        ),
        5,
        768,
        1.8,
        0.87,
    ),

    Receita(
        "Major Energy Potion",
        6,
        (
            I("Elusive Foxglove", 72),
            I("Sheep's Milk", 18),
            I("Potato Schnapps", 18),
        ),
    ),

    Receita(
        "Poison Potion",
        6,
        (
            I("Elusive Foxglove", 24),
            I("Dragon Teasel", 12),
            I("Brightleaf Comfrey", 12),
            I("Sheep's Milk", 6),
        ),
        5,
        378,
        0.9,
        0.53,
    ),

    Receita(
        "Berserk Potion",
        6,
        (
            I("Fine Werewolf Fangs", 1),
            I("Elusive Foxglove", 48),
            I("Arcane Agaric", 24),
            I("Potato Schnapps", 12),
        ),
        5,
        298,
        1.4,
        0.42,
    ),

    Receita(
        "Hellfire Potion",
        6,
        (
            I("Fine Imp's Horn", 1),
            I("Sheep's Milk", 48),
            I("Elusive Foxglove", 24),
            I("Hen Eggs", 12),
        ),
        5,
        294,
        1.3,
        0.42,
    ),

    Receita(
        "Gathering Potion",
        6,
        (
            I("Fine Runestone Tooth", 1),
            I("Sheep's Butter", 48),
            I("Elusive Foxglove", 24),
            I("Dragon Teasel", 12),
        ),
        5,
        310,
        1.4,
        0.44,
    ),

    Receita(
        "Tornado in a Bottle",
        6,
        (
            I("Fine Dawnfeather", 1),
            I("Elusive Foxglove", 48),
            I("Dragon Teasel", 24),
            I("Hen Eggs", 12),
        ),
        5,
        294,
        1.3,
        0.42,
    ),

    # ========================================================
    # T7
    # ========================================================

    Receita(
        "Major Gigantify Potion",
        7,
        (
            I("Firetouched Mullein", 72),
            I("Elusive Foxglove", 36),
            I("Goose Eggs", 18),
            I("Corn Hooch", 18),
        ),
        5,
        1020,
        2.3,
        1.15,
    ),

    Receita(
        "Major Resistance Potion",
        7,
        (
            I("Firetouched Mullein", 72),
            I("Elusive Foxglove", 36),
            I("Crenellated Burdock", 36),
            I("Sheep's Milk", 18),
            I("Corn Hooch", 18),
        ),
        5,
        1272,
        2.9,
        1.44,
    ),

    Receita(
        "Major Sticky Potion",
        7,
        (
            I("Firetouched Mullein", 72),
            I("Elusive Foxglove", 36),
            I("Crenellated Burdock", 36),
            I("Goose Eggs", 18),
            I("Corn Hooch", 18),
        ),
        5,
        1272,
        2.9,
        1.44,
    ),

    Receita(
        "Major Calming Potion",
        7,
        (
            I("Excellent Shadow Claws", 1),
            I("Firetouched Mullein", 144),
            I("Elusive Foxglove", 72),
            I("Brightleaf Comfrey", 72),
            I("Arcane Agaric", 36),
            I("Corn Hooch", 36),
        ),
        5,
        1272,
        5.8,
        1.44,
    ),

    Receita(
        "Major Cleansing Potion",
        7,
        (
            I("Excellent Sylvian Root", 1),
            I("Firetouched Mullein", 144),
            I("Crenellated Burdock", 72),
            I("Brightleaf Comfrey", 72),
            I("Sheep's Butter", 36),
            I("Corn Hooch", 36),
        ),
        5,
        1283,
        5.9,
        1.45,
    ),

    Receita(
        "Major Acid Potion",
        7,
        (
            I("Excellent Spirit Paws", 1),
            I("Firetouched Mullein", 144),
            I("Elusive Foxglove", 72),
            I("Potato Schnapps", 72),
            I("Sheep's Milk", 36),
            I("Corn Hooch", 36),
        ),
        5,
        1296,
        5.9,
        1.46,
    ),

    # ========================================================
    # T8
    # ========================================================

    Receita(
        "Major Poison Potion",
        8,
        (
            I("Ghoul Yarrow", 72),
            I("Firetouched Mullein", 36),
            I("Dragon Teasel", 36),
            I("Cow's Milk", 18),
            I("Pumpkin Moonshine", 18),
        ),
    ),

    Receita(
        "Invisibility Potion",
        8,
        (
            I("Ghoul Yarrow", 72),
            I("Firetouched Mullein", 36),
            I("Dragon Teasel", 36),
            I("Cow's Milk", 18),
            I("Pumpkin Moonshine", 18),
        ),
    ),

    Receita(
        "Major Berserk Potion",
        8,
        (
            I("Excellent Werewolf Fangs", 1),
            I("Ghoul Yarrow", 144),
            I("Brightleaf Comfrey", 72),
            I("Potato Schnapps", 72),
            I("Corn Hooch", 36),
            I("Pumpkin Moonshine", 36),
        ),
        5,
        1307,
        6.0,
        1.47,
    ),

    Receita(
        "Major Hellfire Potion",
        8,
        (
            I("Excellent Imp's Horn", 1),
            I("Cow's Milk", 144),
            I("Ghoul Yarrow", 72),
            I("Firetouched Mullein", 72),
            I("Goose Eggs", 36),
            I("Pumpkin Moonshine", 36),
        ),
        5,
        1272,
        5.8,
        1.44,
    ),

    Receita(
        "Major Gathering Potion",
        8,
        (
            I("Excellent Runestone Tooth", 1),
            I("Cow's Butter", 144),
            I("Ghoul Yarrow", 72),
            I("Firetouched Mullein", 72),
            I("Elusive Foxglove", 36),
            I("Pumpkin Moonshine", 36),
        ),
        5,
        1319,
        6.0,
        1.48,
    ),

    Receita(
        "Major Tornado in a Bottle",
        8,
        (
            I("Excellent Dawnfeather", 1),
            I("Ghoul Yarrow", 144),
            I("Firetouched Mullein", 72),
            I("Corn Hooch", 72),
            I("Goose Eggs", 36),
            I("Pumpkin Moonshine", 36),
        ),
        5,
        1296,
        5.9,
        1.46,
    ),
]


# ============================================================
# ARCANE EXTRACT
# ============================================================

ARCANE_EXTRACT = {
    ("Minor Healing Potion", 1): 5,
    ("Minor Healing Potion", 2): 5,
    ("Minor Healing Potion", 3): 5,

    ("Healing Potion", 1): 15,
    ("Healing Potion", 2): 15,
    ("Healing Potion", 3): 15,

    ("Major Healing Potion", 1): 45,
    ("Major Healing Potion", 2): 45,
    ("Major Healing Potion", 3): 45,

    ("Minor Calming Potion", 1): 10,
    ("Minor Calming Potion", 2): 10,
    ("Minor Calming Potion", 3): 10,

    ("Berserk Potion", 1): 30,
    ("Berserk Potion", 2): 30,
    ("Berserk Potion", 3): 30,
}


def extract_name(encantamento: int) -> str:
    return {
        1: "Basic Arcane Extract",
        2: "Refined Arcane Extract",
        3: "Pure Arcane Extract",
    }[encantamento]


# ============================================================
# ENTRADAS
# ============================================================

def pedir_numero(mensagem: str) -> float:

    while True:

        raw = input(mensagem).strip()

        if not raw:
            return 0.0

        raw = raw.replace(",", ".")

        try:
            valor = float(raw)

        except ValueError:

            print("Digite um número válido.")
            continue

        if valor < 0:

            print("O valor não pode ser negativo.")
            continue

        return valor


def pedir_inteiro(
    mensagem: str,
    minimo: int = 1
) -> int:

    while True:

        raw = input(mensagem).strip()

        try:
            valor = int(raw)

        except ValueError:

            print("Digite um número inteiro.")
            continue

        if valor < minimo:

            print(
                f"Digite um número maior ou igual a {minimo}."
            )
            continue

        return valor


def pedir_sim_nao(
    mensagem: str,
    padrao: Optional[bool] = None
) -> bool:

    while True:

        if padrao is True:
            final = " [S/n]: "
        elif padrao is False:
            final = " [s/N]: "
        else:
            final = " [s/n]: "

        resposta = input(
            mensagem + final
        ).strip().lower()

        if resposta == "" and padrao is not None:
            return padrao

        if resposta in {"s", "sim", "y", "yes"}:
            return True

        if resposta in {"n", "nao", "não", "no"}:
            return False

        print("Digite s ou n.")


# ============================================================
# FUNÇÕES BÁSICAS
# ============================================================

def calcular_rrr(
    production_bonus: float
) -> float:

    if production_bonus <= 0:
        return 0.0

    return (
        production_bonus
        / (100.0 + production_bonus)
    )


def calcular_focus(
    focus_base: Optional[float],
    efficiency: float
) -> Optional[float]:

    if focus_base is None:
        return None

    if efficiency <= 0:
        return focus_base

    return (
        focus_base
        * (
            0.5
            ** (
                efficiency
                / 10000.0
            )
        )
    )


def calcular_crafts(
    quantidade_pocoes: int,
    producao_por_craft: int
) -> int:

    return math.ceil(
        quantidade_pocoes
        / producao_por_craft
    )


def obter_ingredientes(
    receita: Receita,
    encantamento: int
) -> list[Ingrediente]:

    ingredientes = list(
        receita.ingredientes
    )

    if encantamento == 0:
        return ingredientes

    conhecido = ARCANE_EXTRACT.get(
        (
            receita.nome,
            encantamento
        )
    )

    nome = extract_name(
        encantamento
    )

    if conhecido is None:

        print()
        print(
            f"A quantidade de {nome} para "
            f"{receita.nome} .{encantamento} "
            "ainda não está cadastrada."
        )

        quantidade = pedir_inteiro(
            f"Quantos {nome} por craft? "
        )

    else:

        quantidade = conhecido

    ingredientes.append(
        I(nome, quantidade)
    )

    return ingredientes


def calcular_ingredientes_totais(
    receita: Receita,
    encantamento: int,
    crafts: int
) -> dict[str, int]:

    ingredientes = obter_ingredientes(
        receita,
        encantamento
    )

    totais: dict[str, int] = {}

    for ingrediente in ingredientes:

        total = (
            ingrediente.quantidade
            * crafts
        )

        totais[ingrediente.nome] = (
            totais.get(
                ingrediente.nome,
                0
            )
            + total
        )

    return totais


def formatar_silver(valor: float) -> str:
    return f"{valor:,.2f}"


# ============================================================
# CÁLCULO COMPLETO
# ============================================================

def calcular_receita(
    receita: Receita,
    encantamento: int,
    quantidade_pocoes: int,
    precos: dict[str, float],
    preco_venda: float,
    production_bonus: float,
    taxa_estacao_por_craft: float,
    sales_tax_percent: float,
    setup_fee_percent: float,
    usar_focus: bool,
    focus_efficiency: float,
):
    crafts = calcular_crafts(
        quantidade_pocoes,
        receita.producao_por_craft
    )

    quantidade_real = (
        crafts
        * receita.producao_por_craft
    )

    ingredientes = (
        calcular_ingredientes_totais(
            receita,
            encantamento,
            crafts
        )
    )

    custo_materiais = 0.0

    for item, quantidade in ingredientes.items():

        if item not in precos:
            return None

        custo_materiais += (
            quantidade
            * precos[item]
        )

    rrr = calcular_rrr(
        production_bonus
    )

    valor_retorno = (
        custo_materiais
        * rrr
    )

    custo_materiais_efetivo = (
        custo_materiais
        - valor_retorno
    )

    receita_bruta = (
        quantidade_real
        * preco_venda
    )

    taxa_estacao = (
        taxa_estacao_por_craft
        * crafts
    )

    sales_tax = (
        receita_bruta
        * sales_tax_percent
        / 100.0
    )

    setup_fee = (
        receita_bruta
        * setup_fee_percent
        / 100.0
    )

    custo_total = (
        custo_materiais_efetivo
        + taxa_estacao
        + sales_tax
        + setup_fee
    )

    lucro = (
        receita_bruta
        - custo_total
    )

    if custo_total > 0:

        roi = (
            lucro
            / custo_total
            * 100.0
        )

    else:

        roi = 0.0

    if usar_focus:

        focus_por_craft = calcular_focus(
            receita.focus_base,
            focus_efficiency
        )

        if focus_por_craft is None:

            focus_total = None

        else:

            focus_total = (
                focus_por_craft
                * crafts
            )

    else:

        focus_total = 0.0

    if receita.tempo_craft is not None:

        tempo_total = (
            receita.tempo_craft
            * crafts
        )

    else:

        tempo_total = None

    if receita.peso_pocao is not None:

        peso_total = (
            receita.peso_pocao
            * quantidade_real
        )

    else:

        peso_total = None

    return {
        "receita": receita,
        "encantamento": encantamento,
        "quantidade": quantidade_pocoes,
        "quantidade_real": quantidade_real,
        "crafts": crafts,
        "ingredientes": ingredientes,
        "custo_materiais": custo_materiais,
        "rrr": rrr,
        "retorno": valor_retorno,
        "custo_materiais_efetivo": custo_materiais_efetivo,
        "taxa_estacao": taxa_estacao,
        "sales_tax": sales_tax,
        "setup_fee": setup_fee,
        "custo_total": custo_total,
        "receita_bruta": receita_bruta,
        "lucro": lucro,
        "roi": roi,
        "focus": focus_total,
        "tempo": tempo_total,
        "peso": peso_total,
    }


# ============================================================
# PREÇOS
# ============================================================

def materiais_unicos() -> list[str]:

    materiais = set()

    for receita in RECEITAS:

        for ingrediente in receita.ingredientes:

            materiais.add(
                ingrediente.nome
            )

    return sorted(materiais)


def pedir_precos_materiais() -> dict[str, float]:

    print()
    print("=" * 70)
    print("PREÇOS DOS MATERIAIS")
    print("=" * 70)

    print(
        "Digite o preço de UMA unidade."
    )

    precos = {}

    for material in materiais_unicos():

        precos[material] = pedir_numero(
            f"{material}: "
        )

    return precos


def pedir_precos_extracts(
    precos: dict[str, float]
) -> None:

    print()
    print("=" * 70)
    print("PREÇOS DOS ARCANE EXTRACTS")
    print("=" * 70)

    for item in [
        "Basic Arcane Extract",
        "Refined Arcane Extract",
        "Pure Arcane Extract",
    ]:

        precos[item] = pedir_numero(
            f"{item}: "
        )


def pedir_precos_pocoes() -> dict[str, float]:

    print()
    print("=" * 70)
    print("PREÇOS DE VENDA DAS POÇÕES")
    print("=" * 70)

    print(
        "Coloque 0 se não quiser considerar uma poção."
    )

    precos = {}

    for receita in RECEITAS:

        precos[receita.nome] = pedir_numero(
            f"{receita.nome} T{receita.tier}.0: "
        )

    return precos


# ============================================================
# MODO 1 — ANALISAR
# ============================================================

def analisar() -> None:

    print()
    print("=" * 70)
    print("         ANALISAR MELHOR PRODUÇÃO")
    print("=" * 70)

    # --------------------------------------------------------
    # JOGADOR
    # --------------------------------------------------------

    prata = pedir_numero(
        "\nQuanto de prata você tem? "
    )

    reserva = pedir_numero(
        "Quanto você quer deixar guardado? "
    )

    capital = max(
        0.0,
        prata - reserva
    )

    focus_disponivel = pedir_numero(
        "Quanto Focus você tem? "
    )

    premium = pedir_sim_nao(
        "Você possui Premium?",
        False
    )

    production_bonus = pedir_numero(
        "Production Bonus total (%): ",
        0.0
    )

    taxa_estacao_por_craft = pedir_numero(
        "Taxa da estação POR CRAFT (silver): ",
        0.0
    )

    sales_tax = pedir_numero(
        "Sales Tax (%): ",
        0.0
    )

    setup_fee = pedir_numero(
        "Setup Fee (%): ",
        0.0
    )

    usar_focus = pedir_sim_nao(
        "Considerar Focus?",
        True
    )

    focus_efficiency = 0.0

    if usar_focus:

        focus_efficiency = pedir_numero(
            "Focus Cost Efficiency: ",
            0.0
        )

    print()
    print(
        f"Capital disponível para investir: "
        f"{formatar_silver(capital)} silver"
    )

    # --------------------------------------------------------
    # PREÇOS
    # --------------------------------------------------------

    precos = pedir_precos_materiais()

    precos_venda = pedir_precos_pocoes()

    considerar_encantamentos = pedir_sim_nao(
        "\nConsiderar .1/.2/.3?",
        False
    )

    if considerar_encantamentos:

        pedir_precos_extracts(
            precos
        )

        encantamentos = [0, 1, 2, 3]

    else:

        encantamentos = [0]

    # --------------------------------------------------------
    # EXTRACTS DESCONHECIDOS
    # --------------------------------------------------------

    extract_quantities: dict[
        tuple[str, int],
        int
    ] = {}

    def obter_extract_para_analise(
        receita: Receita,
        encantamento: int
    ) -> Optional[Ingrediente]:

        if encantamento == 0:
            return None

        chave = (
            receita.nome,
            encantamento
        )

        if chave in extract_quantities:

            return I(
                extract_name(encantamento),
                extract_quantities[chave]
            )

        if chave in ARCANE_EXTRACT:

            quantidade = ARCANE_EXTRACT[chave]

        else:

            print()
            print(
                f"Falta a quantidade de "
                f"{extract_name(encantamento)} "
                f"para {receita.nome} .{encantamento}."
            )

            quantidade = pedir_inteiro(
                "Quantidade por craft: "
            )

        extract_quantities[chave] = quantidade

        return I(
            extract_name(encantamento),
            quantidade
        )

    # --------------------------------------------------------
    # SIMULAÇÕES
    # --------------------------------------------------------

    resultados = []

    # Quantidades testadas.
    #
    # Começamos de 5 e vamos de 5 em 5.
    #
    # Isso significa:
    # 5, 10, 15, 20...
    #
    # Máximo de 1500 poções por cenário.
    #
    # O importante aqui é:
    # quantidade representa POÇÕES,
    # não número de simulações.

    MAX_PoCOES_ANALISADAS = 1500

    for receita in RECEITAS:

        preco_venda = precos_venda[
            receita.nome
        ]

        if preco_venda <= 0:
            continue

        for encantamento in encantamentos:

            extra = obter_extract_para_analise(
                receita,
                encantamento
            )

            if extra is None:

                base_ingredientes = list(
                    receita.ingredientes
                )

            else:

                base_ingredientes = (
                    list(receita.ingredientes)
                    + [extra]
                )

            por_craft = {}

            for ingrediente in base_ingredientes:

                por_craft[
                    ingrediente.nome
                ] = (
                    por_craft.get(
                        ingrediente.nome,
                        0
                    )
                    + ingrediente.quantidade
                )

            for quantidade in range(
                receita.producao_por_craft,
                MAX_PoCOES_ANALISADAS + 1,
                receita.producao_por_craft
            ):

                crafts = (
                    quantidade
                    // receita.producao_por_craft
                )

                # --------------------------------------------
                # Focus
                # --------------------------------------------

                if usar_focus:

                    focus_unitario = calcular_focus(
                        receita.focus_base,
                        focus_efficiency
                    )

                    if focus_unitario is None:
                        continue

                    focus_total = (
                        focus_unitario
                        * crafts
                    )

                    if focus_total > focus_disponivel:

                        break

                else:

                    focus_total = 0.0

                # --------------------------------------------
                # Materiais
                # --------------------------------------------

                custo_materiais = 0.0

                impossivel = False

                for item, qtd_por_craft in por_craft.items():

                    if item not in precos:

                        impossivel = True
                        break

                    quantidade_total = (
                        qtd_por_craft
                        * crafts
                    )

                    custo_materiais += (
                        quantidade_total
                        * precos[item]
                    )

                if impossivel:

                    continue

                # --------------------------------------------
                # RRR
                # --------------------------------------------

                rrr = calcular_rrr(
                    production_bonus
                )

                retorno = (
                    custo_materiais
                    * rrr
                )

                custo_materiais_efetivo = (
                    custo_materiais
                    - retorno
                )

                # --------------------------------------------
                # Receita
                # --------------------------------------------

                receita_bruta = (
                    quantidade
                    * preco_venda
                )

                # --------------------------------------------
                # Taxas
                # --------------------------------------------

                taxa_estacao = (
                    taxa_estacao_por_craft
                    * crafts
                )

                sales_tax_value = (
                    receita_bruta
                    * sales_tax
                    / 100.0
                )

                setup_fee_value = (
                    receita_bruta
                    * setup_fee
                    / 100.0
                )

                custo_total = (
                    custo_materiais_efetivo
                    + taxa_estacao
                    + sales_tax_value
                    + setup_fee_value
                )

                # --------------------------------------------
                # Capital
                # --------------------------------------------

                if custo_total > capital:

                    break

                # --------------------------------------------
                # Lucro
                # --------------------------------------------

                lucro = (
                    receita_bruta
                    - custo_total
                )

                if custo_total <= 0:
                    continue

                roi = (
                    lucro
                    / custo_total
                    * 100.0
                )

                # --------------------------------------------
                # Tempo
                # --------------------------------------------

                if receita.tempo_craft is not None:

                    tempo = (
                        receita.tempo_craft
                        * crafts
                    )

                    lucro_por_segundo = (
                        lucro / tempo
                        if tempo > 0
                        else 0.0
                    )

                else:

                    tempo = None
                    lucro_por_segundo = None

                # --------------------------------------------
                # Guardar resultado
                # --------------------------------------------

                resultados.append(
                    {
                        "receita": receita,
                        "encantamento": encantamento,
                        "quantidade": quantidade,
                        "crafts": crafts,
                        "custo": custo_total,
                        "receita_bruta": receita_bruta,
                        "lucro": lucro,
                        "roi": roi,
                        "focus": focus_total,
                        "tempo": tempo,
                        "lucro_por_segundo": lucro_por_segundo,
                    }
                )

    # --------------------------------------------------------
    # RANKING
    # --------------------------------------------------------

    resultados.sort(
        key=lambda x: x["lucro"],
        reverse=True
    )

    print()
    print("=" * 100)
    print("TOP 3 — MAIOR LUCRO")
    print("=" * 100)

    if not resultados:

        print(
            "\nNenhuma estratégia válida foi encontrada."
        )

        return

    for posicao, resultado in enumerate(
        resultados[:3],
        start=1
    ):

        receita = resultado["receita"]

        print()
        print(
            f"{posicao}º LUGAR"
        )

        print(
            f"Poção:              "
            f"{receita.nome} "
            f"T{receita.tier}."
            f"{resultado['encantamento']}"
        )

        print(
            f"Quantidade:          "
            f"{resultado['quantidade']}"
        )

        print(
            f"Crafts:              "
            f"{resultado['crafts']}"
        )

        print(
            f"Custo total:         "
            f"{formatar_silver(resultado['custo'])} silver"
        )

        print(
            f"Receita:             "
            f"{formatar_silver(resultado['receita_bruta'])} silver"
        )

        print(
            f"LUCRO:               "
            f"{formatar_silver(resultado['lucro'])} silver"
        )

        print(
            f"ROI:                 "
            f"{resultado['roi']:.2f}%"
        )

        if resultado["focus"] is not None:

            print(
                f"Focus usado:         "
                f"{resultado['focus']:,.0f}"
            )

        if resultado["tempo"] is not None:

            print(
                f"Tempo:               "
                f"{resultado['tempo']:.2f} segundos"
            )

            if resultado["tempo"] > 0:

                print(
                    f"Lucro/hora:          "
                    f"{formatar_silver(
                        resultado['lucro_por_segundo']
                        * 3600
                    )} silver"
                )

    # --------------------------------------------------------
    # RECOMENDAÇÃO
    # --------------------------------------------------------

    melhor = resultados[0]

    receita = melhor["receita"]

    print()
    print("=" * 70)
    print("RECOMENDAÇÃO")
    print("=" * 70)

    print(
        f"Melhor estratégia:"
    )

    print(
        f"{receita.nome} "
        f"T{receita.tier}."
        f"{melhor['encantamento']}"
    )

    print(
        f"\nFaça aproximadamente "
        f"{melhor['quantidade']} poções."
    )

    print(
        f"Lucro esperado: "
        f"{formatar_silver(melhor['lucro'])} silver"
    )

    print(
        f"ROI: "
        f"{melhor['roi']:.2f}%"
    )

    print(
        "\nCritério usado: MAIOR LUCRO."
    )

    print(
        f"Premium informado: "
        f"{'SIM' if premium else 'NÃO'}"
    )


# ============================================================
# MODO 2 — CALCULAR UMA POÇÃO
# ============================================================

def calcular_uma() -> None:

    print()
    print("=" * 70)
    print("CALCULAR UMA POÇÃO")
    print("=" * 70)

    for numero, receita in enumerate(
        RECEITAS,
        start=1
    ):

        print(
            f"{numero:02d} - "
            f"{receita.nome} "
            f"T{receita.tier}.0"
        )

    while True:

        escolha = pedir_inteiro(
            "\nEscolha a poção: "
        )

        if 1 <= escolha <= len(RECEITAS):
            break

        print("Poção inválida.")

    receita = RECEITAS[
        escolha - 1
    ]

    print()
    print("=" * 70)
    print(
        f"{receita.nome} T{receita.tier}"
    )
    print("=" * 70)

    print("0 - .0")
    print("1 - .1")
    print("2 - .2")
    print("3 - .3")

    while True:

        encantamento = pedir_inteiro(
            "Escolha o encantamento: ",
            0
        )

        if encantamento in {0, 1, 2, 3}:
            break

        print(
            "Escolha 0, 1, 2 ou 3."
        )

    nome = (
        f"{receita.nome} "
        f"T{receita.tier}."
        f"{encantamento}"
    )

    print()
    print(
        f"Você escolheu: {nome}"
    )

    quantidade = pedir_inteiro(
        "\nQuantas poções você quer fabricar? "
    )

    crafts = calcular_crafts(
        quantidade,
        receita.producao_por_craft
    )

    quantidade_real = (
        crafts
        * receita.producao_por_craft
    )

    print()
    print("=" * 70)
    print("PLANEJAMENTO")
    print("=" * 70)

    print(
        f"Poção:              {nome}"
    )

    print(
        f"Você quer:          {quantidade}"
    )

    print(
        f"Crafts necessários: {crafts}"
    )

    print(
        f"Produção real:      {quantidade_real}"
    )

    if quantidade_real > quantidade:

        print(
            f"Sobra:              "
            f"{quantidade_real - quantidade}"
        )

    # --------------------------------------------------------
    # INGREDIENTES
    # --------------------------------------------------------

    ingredientes = (
        calcular_ingredientes_totais(
            receita,
            encantamento,
            crafts
        )
    )

    print()
    print("=" * 70)
    print("MATERIAIS NECESSÁRIOS")
    print("=" * 70)

    for item, quantidade_total in (
        ingredientes.items()
    ):

        print(
            f"{item:<38}"
            f"{quantidade_total:>10}"
        )

    # --------------------------------------------------------
    # PREÇOS
    # --------------------------------------------------------

    print()
    print("=" * 70)
    print("PREÇOS DOS MATERIAIS")
    print("=" * 70)

    precos = {}

    for item in ingredientes:

        precos[item] = pedir_numero(
            f"Preço de 1x {item}: "
        )

    preco_venda = pedir_numero(
        "\nPreço de venda de UMA poção: "
    )

    production_bonus = pedir_numero(
        "Production Bonus (%): ",
        33.0
    )

    taxa_estacao = pedir_numero(
        "Custo total da estação (silver): ",
        0.0
    )

    sales_tax = pedir_numero(
        "Sales Tax (%): ",
        0.0
    )

    setup_fee = pedir_numero(
        "Setup Fee (%): ",
        0.0
    )

    usar_focus = pedir_sim_nao(
        "Considerar Focus?",
        False
    )

    focus_efficiency = 0.0

    if usar_focus:

        focus_efficiency = pedir_numero(
            "Focus Cost Efficiency: ",
            0.0
        )

    resultado = calcular_receita(
        receita=receita,
        encantamento=encantamento,
        quantidade_pocoes=quantidade,
        precos=precos,
        preco_venda=preco_venda,
        production_bonus=production_bonus,
        taxa_estacao_por_craft=taxa_estacao / crafts,
        sales_tax_percent=sales_tax,
        setup_fee_percent=setup_fee,
        usar_focus=usar_focus,
        focus_efficiency=focus_efficiency,
    )

    if resultado is None:

        print(
            "\nNão foi possível calcular."
        )

        return

    # --------------------------------------------------------
    # RESULTADO
    # --------------------------------------------------------

    print()
    print("=" * 70)
    print("RESULTADO FINAL")
    print("=" * 70)

    print(
        f"Poção:                 {nome}"
    )

    print(
        f"Quantidade desejada:   "
        f"{quantidade}"
    )

    print(
        f"Quantidade produzida:  "
        f"{resultado['quantidade_real']}"
    )

    print(
        f"Crafts:                "
        f"{resultado['crafts']}"
    )

    print()
    print("CUSTOS")

    print(
        f"Materiais nominais:    "
        f"{formatar_silver(resultado['custo_materiais'])}"
    )

    print(
        f"RRR:                   "
        f"{resultado['rrr'] * 100:.2f}%"
    )

    print(
        f"Retorno RRR:           "
        f"-{formatar_silver(resultado['retorno'])}"
    )

    print(
        f"Materiais efetivos:    "
        f"{formatar_silver(resultado['custo_materiais_efetivo'])}"
    )

    print(
        f"Taxa da estação:       "
        f"{formatar_silver(resultado['taxa_estacao'])}"
    )

    print(
        f"Sales Tax:             "
        f"{formatar_silver(resultado['sales_tax'])}"
    )

    print(
        f"Setup Fee:             "
        f"{formatar_silver(resultado['setup_fee'])}"
    )

    print(
        f"CUSTO TOTAL:           "
        f"{formatar_silver(resultado['custo_total'])}"
    )

    print()
    print("VENDA")

    print(
        f"Receita bruta:         "
        f"{formatar_silver(resultado['receita_bruta'])}"
    )

    print()
    print("RESULTADO")

    if resultado["lucro"] >= 0:

        print(
            f"LUCRO:                 "
            f"{formatar_silver(resultado['lucro'])}"
        )

    else:

        print(
            f"PREJUÍZO:              "
            f"{formatar_silver(abs(resultado['lucro']))}"
        )

    print(
        f"ROI:                   "
        f"{resultado['roi']:.2f}%"
    )

    if resultado["focus"] is not None:

        print(
            f"Focus total:           "
            f"{resultado['focus']:,.0f}"
        )

    else:

        print(
            "Focus:                 "
            "não cadastrado"
        )

    if resultado["tempo"] is not None:

        print(
            f"Tempo total:           "
            f"{resultado['tempo']:.2f} segundos"
        )

        if resultado["tempo"] > 0:

            lucro_hora = (
                resultado["lucro"]
                / resultado["tempo"]
                * 3600
            )

            print(
                f"Lucro por hora:        "
                f"{formatar_silver(lucro_hora)}"
            )

    else:

        print(
            "Tempo:                 "
            "não cadastrado"
        )

    if resultado["peso"] is not None:

        print(
            f"Peso total:            "
            f"{resultado['peso']:.2f} kg"
        )

    else:

        print(
            "Peso:                  "
            "não cadastrado"
        )

    print("=" * 70)


# ============================================================
# MODO 3 — RECEITAS
# ============================================================

def mostrar_receitas() -> None:

    print()
    print("=" * 70)
    print("RECEITAS")
    print("=" * 70)

    for receita in RECEITAS:

        print()
        print(
            f"{receita.nome} "
            f"T{receita.tier}.0"
        )

        for ingrediente in receita.ingredientes:

            print(
                f"  {ingrediente.quantidade}x "
                f"{ingrediente.nome}"
            )

        print(
            f"  Produção: "
            f"{receita.producao_por_craft}"
        )

        if receita.focus_base is not None:

            print(
                f"  Focus base: "
                f"{receita.focus_base:g}"
            )

        else:

            print(
                "  Focus base: "
                "não cadastrado"
            )

        if receita.tempo_craft is not None:

            print(
                f"  Tempo: "
                f"{receita.tempo_craft}s"
            )

        else:

            print(
                "  Tempo: "
                "não cadastrado"
            )

        if receita.peso_pocao is not None:

            print(
                f"  Peso: "
                f"{receita.peso_pocao} kg"
            )

        else:

            print(
                "  Peso: "
                "não cadastrado"
            )


# ============================================================
# MENU
# ============================================================

def main():

    while True:

        print()
        print("=" * 70)
        print(
            "       ALBION ONLINE - CRAFTING OPTIMIZER"
        )
        print("=" * 70)

        print(
            "1 - ANALISAR melhor produção"
        )

        print(
            "2 - CALCULAR uma poção específica"
        )

        print(
            "3 - VER receitas"
        )

        print(
            "0 - SAIR"
        )

        escolha = input(
            "\nEscolha: "
        ).strip()

        if escolha == "1":

            analisar()

        elif escolha == "2":

            calcular_uma()

        elif escolha == "3":

            mostrar_receitas()

        elif escolha == "0":

            print(
                "\nFechando Albion Optimizer."
            )

            break

        else:

            print(
                "\nOpção inválida."
            )


if __name__ == "__main__":
    main()

