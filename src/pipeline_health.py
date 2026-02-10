import pandas as pd

df = pd.read_csv("outputs/deal_win_probabilities.csv")

expected_revenue = (df["deal_amount"] * df["win_probability"]).sum()
total_pipeline = df["deal_amount"].sum()

health_score = expected_revenue / total_pipeline

print("\n=== PIPELINE HEALTH METRIC ===")
print("Expected Revenue:", round(expected_revenue,2))
print("Pipeline Health Score:", round(health_score,3))
print("Interpretation: Portion of pipeline likely to convert.")