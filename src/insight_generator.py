import pandas as pd

df = pd.read_csv("data/skygeni_sales_data.csv")

def generate_cro_insights(df):

    win_rate = (df["outcome"]=="Won").mean()

    stage_win = df.groupby("deal_stage")["outcome"].apply(lambda x: (x=="Won").mean())
    worst_stage = stage_win.idxmin()

    region_win = df.groupby("region")["outcome"].apply(lambda x: (x=="Won").mean())
    worst_region = region_win.idxmin()

    top_deals = df.sort_values("deal_amount", ascending=False).head(int(0.2*len(df)))
    concentration = top_deals["deal_amount"].sum() / df["deal_amount"].sum()

    print("\n=== SALES INTELLIGENCE INSIGHTS FOR CRO ===\n")
    print(f"Overall Win Rate: {round(win_rate*100,2)}%")
    print(f"Lowest Converting Stage: {worst_stage}")
    print(f"Lowest Performing Region: {worst_region}")
    print(f"Pipeline Concentration Risk: {round(concentration*100,2)}% revenue in top 20% deals")

generate_cro_insights(df)

# High risk deals

risk_deals = df_results = pd.read_csv("outputs/deal_win_probabilities.csv")

high_risk = risk_deals[risk_deals["win_probability"] < 0.4]
high_risk = high_risk.sort_values("win_probability")

print("\n=== HIGH RISK DEALS (Sample) ===")
print(high_risk[["deal_id","deal_stage","region","deal_amount","win_probability"]].head(10))