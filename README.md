[![CI](https://github.com/amandamarinoni/help-desk-analytics/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/amandamarinoni/help-desk-analytics/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/amandamarinoni/help-desk-analytics?display_name=tag)](https://github.com/amandamarinoni/help-desk-analytics/releases)

# Help Desk Analytics — KPIs de Suporte (SLA, MTTR, Backlog)
## Rodar rápido
```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python src/main.py --input data/raw/sample_tickets.csv --out data/processed/kpis.json
```
