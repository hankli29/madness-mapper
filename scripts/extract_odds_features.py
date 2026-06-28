import pandas as pd
from pathlib import Path

def main():
    base_dir = Path(__file__).resolve().parent.parent

    df = pd.read_csv(base_dir / "data" / "raw_historical_odds.csv")

    df = df[["Date", "Team", "Close", "ML", "YEAR"]]

    # convert strings from csv to numeric values
    # for games without odds, convert value to NaN
    df["Close"] = pd.to_numeric(df["Close"], errors="coerce")
    df["ML"] = pd.to_numeric(df["ML"], errors="coerce")
    df["Date"] = pd.to_numeric(df["Date"], errors="coerce")

    data_rows = []
    for i in range(0, len(df) - 1, 2):
        team1 = df.iloc[i]
        team2 = df.iloc[i + 1]
        
        date = team1["Date"]

        # narrow down odds data to focus on tournament games specifically
        # will incude reg season games as start date changes every year
        if date < 310 or date > 410:
            continue

        # tournament games always have odds
        # just clearing out random small reg season games
        if (pd.isna(team1["Close"]) or pd.isna(team1["ML"])) or (pd.isna(team2["Close"]) or pd.isna(team2["ML"])):
            continue

        if team1["ML"] < 0:
            # favored team's close == spread for favored team
            # underdog team's close == total point o/u
            spread_t1 = -1 * team1["Close"]
            spread_t2 = -1 * spread_t1
            total_ou = team2["Close"]
        else:
            spread_t2 = -1 * team2["Close"]
            spread_t1 = -1 * spread_t2
            total_ou = team1["Close"]
        
        row = {
            "DATE": date,
            "YEAR": team1["YEAR"],
            "TEAM T1": team1["Team"],
            "ML T1": team1["ML"],
            "SPREAD T1": spread_t1,
            "TEAM T2": team2["Team"],
            "ML T2": team2["ML"],
            "SPREAD T2": spread_t2,
            "TOTAL OU": total_ou
        }
        row_mirrored = {
            "DATE": date,
            "YEAR": team1["YEAR"],
            "TEAM T1": team2["Team"],
            "ML T1": team2["ML"],
            "SPREAD T1": spread_t2,
            "TEAM T2": team1["Team"],
            "ML T2": team1["ML"],
            "SPREAD T2": spread_t1,
            "TOTAL OU": total_ou
        }

        data_rows.append(row)
        data_rows.append(row_mirrored)

    cleaned_odds_df = pd.DataFrame(data_rows)

    cleaned_odds_df.to_csv(base_dir / "data" / "cleaned_historical_odds.csv", index=False)

if __name__ == "__main__":
    main()