import argparse, json
from datetime import datetime
from statistics import mean
import pandas as pd

def parse_args():
    p = argparse.ArgumentParser(description="Compute help desk KPIs from CSV.")
    p.add_argument("--input", required=True)
    p.add_argument("--out", required=True)
    return p.parse_args()

def to_dt(x):
    if not x or pd.isna(x):
        return None
    return datetime.fromisoformat(x)

def kpis(df: pd.DataFrame) -> dict:
    df["opened_at"] = df["opened_at"].apply(to_dt)
    df["closed_at"] = df["closed_at"].apply(to_dt)
    backlog = int(df["closed_at"].isna().sum())
    resolved = df.dropna(subset=["closed_at"]).copy()
    def minutes_delta(a, b): return int((b - a).total_seconds() // 60)
    resolved["resolution_minutes"] = resolved.apply(lambda r: minutes_delta(r["opened_at"], r["closed_at"]), axis=1)
    mttr = int(mean(resolved["resolution_minutes"])) if not resolved.empty else 0
    if "breached_sla" in df.columns:
        total = len(df); cumpriu = int((df["breached_sla"] == False).sum())  # noqa
        sla_pct = round((cumpriu / total) * 100, 2) if total else 0.0
    else:
        sla_pct = 0.0
    by_priority = df["priority"].value_counts().to_dict() if "priority" in df.columns else {}
    by_channel = df["channel"].value_counts().to_dict() if "channel" in df.columns else {}
    return {"tickets_total": int(len(df)),
            "mttr_minutes": mttr,
            "sla_met_percent": sla_pct,
            "backlog_open_tickets": backlog,
            "by_priority": by_priority,
            "by_channel": by_channel}

def main():
    args = parse_args()
    df = pd.read_csv(args.input)
    out = kpis(df)
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(json.dumps(out, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
