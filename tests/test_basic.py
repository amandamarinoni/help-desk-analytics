from pathlib import Path
import pandas as pd
from src.main import kpis

def test_kpis_runs():
    csv_path = Path("data/raw/sample_tickets.csv")
    df = pd.read_csv(csv_path)
    out = kpis(df)
    assert out["tickets_total"] > 0
    assert "mttr_minutes" in out
