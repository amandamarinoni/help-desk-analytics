[![CI](https://github.com/amandamarinoni/help-desk-analytics/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/amandamarinoni/help-desk-analytics/actions/workflows/ci.yml)
# Help Desk Analytics — KPIs de Suporte (SLA, MTTR, Backlog)
## Rodar rápido
```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python src/main.py --input data/raw/sample_tickets.csv --out data/processed/kpis.json
```
