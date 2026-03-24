import kagglehub
import pandas as pd

# downloads latest version of march madness data
path = kagglehub.dataset_download("nishaanamin/march-madness-data")

print("Path to dataset files:", path)

kenpom_bart_df = pd.read_csv(f"{path}/KenPom Barttorvik.csv")
# print(kenpom_bart_df.head()) # prints the first 5 rows of data from the dataframe

# indexing into a dataframe returns a sub-table/sub-dataframe
# single key/column for a series, list of keys for a dataframe
# only want to focus on these select data columns
kenpom_bart_df = kenpom_bart_df[["YEAR", "TEAM", "SEED", "ROUND", "KADJ O", "KADJ D", "KADJ EM", "BADJ EM", "BADJ O", "BADJ D", "BARTHAG", "WIN%", "EXP", "TALENT", "ELITE SOS"]]
# data for current year (2026) has every team ROUND stat = 0, this will skew data

# kenpom_bart_df["ROUND"] > 0 creates a boolean mask (true for rows where condition is true, false otherwise)
# kenpom_bart_df[<boolean mask>] returns dataframe only containing "true" rows
kenpom_bart_df = kenpom_bart_df[kenpom_bart_df["ROUND"] > 0]
# after removing 2026 data, row index will no longer start from 0
# must reset index, use drop arg to get rid of old index col
kenpom_bart_df = kenpom_bart_df.reset_index(drop=True)


print(kenpom_bart_df.head())