import pandas as pd

performance = pd.read_csv("1.data/raw/07_scheme_performance.csv")

def recommend_funds(risk_level):
    funds = performance[
        performance["risk_grade"] == risk_level
    ].sort_values(
        "sharpe_ratio",
        ascending=False
    )

    return funds[
        ["scheme_name", "risk_grade", "sharpe_ratio"]
    ].head(3)

if __name__ == "__main__":
    print("Top Moderate Risk Funds:")
    print(recommend_funds("Moderate"))