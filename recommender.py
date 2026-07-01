import pandas as pd

performance = pd.read_csv("data/processed/07_scheme_performance_clean.csv")

print("\nAvailable Risk Levels:")
for level in sorted(performance["risk_grade"].unique()):
    print("-", level)

risk = input("\nEnter Risk Appetite: ")

recommendation = (
    performance[
        performance["risk_grade"].str.lower() == risk.lower()
    ]
    .sort_values("sharpe_ratio", ascending=False)
    .head(3)
)

if recommendation.empty:
    print("\nNo funds found for the selected risk level.")
else:
    print("\nTop 3 Recommended Funds:\n")
    print(
        recommendation[
            [
                "amfi_code",
                "scheme_name",
                "fund_house",
                "category",
                "risk_grade",
                "sharpe_ratio"
            ]
        ].to_string(index=False)
    )