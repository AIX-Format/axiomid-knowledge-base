---
title: "AlphaAxiom — Trading Engine (L4)"
last_updated: "2026-05-16"
status: "stable"
tags: [trading, python, risk, trading-signals]
layer: "L4"
related:
  - "[[stack-overview]]"
  - "[[L5-piworker-os]]"
  - "[[clean-room-skills]]"
---

# AlphaAxiom — Trading Engine (L4)

> ~21,419 lines Python + 742 TS | Tauri + Next.js

## Core Components

### Signal Pipeline
```
signal_generator.py → Gemini AI → JSON signal
→ position_sizing.py: fixed_fractional(2% risk)
→ risk_shield.py: 4 rules
  ├── max_position ≤ 20% equity
  ├── max_concurrent ≤ 3 positions
  ├── daily_loss ≤ 2%
  └── max_drawdown ≤ 5%
→ trading_core.py: CCXT create_order()
→ profit → PiWorker-OS Treasury (10% tax)
```

### Adapters (3,200 lines)
- **CCXT Adapter**: 100+ exchanges
- **MT5**: MetaTrader 5 integration
- **EVM**: On-chain Ethereum
- **Coinbase Adapter**: Coinbase Pro
- **Paper Trading**: Dry-run mode

### Reinforcement Learning (1,149 lines)
- Gymnasium RL environment
- Custom reward functions
- MCTS for trading decisions

### Key Unique Features
- **RiskShield**: Aladdin-inspired 4-rule risk management (فريد)
- **Signal Generator**: Gemini-powered trading signals (فريد)
- **Shadow Mode**: Dry-run comparison
- **Ghost Mode**: Desktop Tauri overlay

## Unique Code (لا يوجد في أي repo آخر)
- `signal_generator.py` — Gemini trading signals
- `risk_shield.py` — 4-rule Aladdin Risk Shield
- `position_sizing.py` — Kelly + ATR + Fixed Fractional
- MCTS for trading
- Desktop Tauri app

## Integration
- Trading profits → PiWorker-OS Treasury via 10% sovereign tax
- Some .aix skills being migrated to L3 marketplace
- See [[L3-aix-agent-skills]] for marketplace integration
- See [[L5-piworker-os]] for treasury flow
