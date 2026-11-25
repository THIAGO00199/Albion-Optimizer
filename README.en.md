# Albion Optimizer — Crafting and Potion Profit Calculator

A command-line crafting optimizer for Albion Online potion recipes. It compares crafting options using prices and operating assumptions supplied by the player.

## Features

- Potion recipes across tiers T2–T8.
- Material and craft quantity calculations.
- Resource return rate (RRR) modeling from a supplied production bonus.
- Station fees, sales tax, setup fees, material costs, revenue, profit, and ROI estimates.
- Focus-efficiency calculations where recipe data is available.
- Strategy ranking based on the player's supplied market prices and constraints.

## Run

Requirements: Python 3.10+; the current implementation uses the Python standard library.

```bash
python3 main.py
```

The program asks for silver balance, reserve targets, focus/premium assumptions, production bonuses, taxes, material prices, and sale prices. It can compare multiple recipes or calculate a selected potion directly.

## Modeling assumptions

- Market prices and fees are entered by the user; they are not fetched live.
- Recipes and craft quantities are local reference data and may need updating after game patches.
- This version assumes five potions per craft.
- Resource return is modeled as expected value; exact in-game rounding and some recipe/focus values still require verification.
- Profit and ROI are estimates, not guarantees of market outcomes.

---

[Português](./README.md) · [English](./README.en.md) · [Español](./README.es.md)
