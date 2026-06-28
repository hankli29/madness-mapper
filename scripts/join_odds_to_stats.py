import pandas as pd
from pathlib import Path

base_dir = Path(__file__).resolve().parent.parent

TEAM_NAME_MAPPING = {
    "AbileneChristian": "Abilene Christian",
    "Akron": "Akron",
    "Alabama": "Alabama",
    "AlabamaState": "Alabama St.",
    "AlbanyNY": "Albany",
    "American": "American",
    "Arizona": "Arizona",
    "ArizonaState": "Arizona St.",
    "Arkansas": "Arkansas",
    "ArkPineBluff": "Arkansas Pine Bluff",
    "Auburn": "Auburn",
    "AustinPeay": "Austin Peay",
    "BYU": "BYU",
    "Baylor": "Baylor",
    "Belmont": "Belmont",
    "Binghamton": "Binghamton",
    "BoiseState": "Boise St.",
    "BostonCollege": "Boston College",
    "BostonU": "Boston University",
    "Bradley": "Bradley",
    "CalPolySLO": "Cal Poly",
    "CSBakersfield": "Cal St. Bakersfield",
    "CSFullerton": "Cal St. Fullerton",
    "CSNorthridge": "Cal St. Northridge",
    "TennesseeChat": "Chattanooga",
    "ClevelandState": "Cleveland St.",
    "CoastalCarolina": "Coastal Carolina",
    "CollCharleston": "College of Charleston",
    "CollOfCharleston": "College of Charleston",
    "ColoradoSt.": "Colorado St.",
    "ColoradoState": "Colorado St.",
    "DetroitU": "Detroit",
    "ETennesseeSt": "East Tennessee St.",
    "EastTennSt.": "East Tennessee St.",
    "EastTennState": "East Tennessee St.",
    "EasternKentucky": "Eastern Kentucky",
    "E.Washington": "Eastern Washington",
    "EasternWashington": "Eastern Washington",
    "FairDickinson": "Fairleigh Dickinson",
    "FarleighDickinson": "Fairleigh Dickinson",
    "FlaAtlantic": "Florida Atlantic",
    "FloridaAtlantic": "Florida Atlantic",
    "FlaGulfCoast": "Florida Gulf Coast",
    "FloridaGulfCoast": "Florida Gulf Coast",
    "FloridaState": "Florida St.",
    "FresnoState": "Fresno St.",
    "GardnerWebb": "Gardner Webb",
    "GeorgeMason": "George Mason",
    "GeoWashington": "George Washington",
    "GeorgeWashington": "George Washington",
    "GeorgiaState": "Georgia St.",
    "GeorgiaTech": "Georgia Tech",
    "Grambling": "Grambling St.",
    "GrandCanyon": "Grand Canyon",
    "WiscGreenBay": "Green Bay",
    "HighPoint": "High Point",
    "HolyCross": "Holy Cross",
    "HoustonU": "Houston",
    "IndianaU": "Indiana",
    "IndianaState": "Indiana St.",
    "IowaState": "Iowa St.",
    "JacksonSt.": "Jacksonville St.",
    "JacksonState": "Jacksonville St.",
    "JacksonvilleSt": "Jacksonville St.",
    "JamesMadison": "James Madison",
    "KansasState": "Kansas St.",
    "KentState": "Kent St.",
    "LongIsland": "LIU Brooklyn",
    "LaSalle": "La Salle",
    "ArkansasLR": "Little Rock",
    "LongBeachState": "Long Beach St.",
    "ULLafayette": "Louisiana Lafayette",
    "LoyolaChicago": "Loyola Chicago",
    "LoyolaMaryland": "Loyola MD",
    "McNeeseState": "McNeese St.",
    "MemphisU": "Memphis",
    "MiamiFlorida": "Miami FL",
    "MichiganState": "Michigan St.",
    "MiddleTennSt": "Middle Tennessee",
    "WiscMilwaukee": "Milwaukee",
    "MinnesotaU": "Minnesota",
    "MississippiSt": "Mississippi St.",
    "MissValleySt": "Mississippi Valley St.",
    "MontanaState": "Montana St.",
    "MoreheadState": "Morehead St.",
    "MorganState": "Morgan St.",
    "MountStMarys": "Mount St. Mary's",
    "MurrayState": "Murray St.",
    "NebraskaOmaha": "Nebraska Omaha",
    "NewMexico": "New Mexico",
    "NewMexicoState": "New Mexico St.",
    "NorfolkSt": "Norfolk St.",
    "NorthCarolina": "North Carolina",
    "N.CarolinaA&T": "North Carolina A&T",
    "NCCentral": "North Carolina Central",
    "NCState": "North Carolina St.",
    "NorthDakota": "North Dakota",
    "NorthDakotaState": "North Dakota St.",
    "NDakotaSt": "North Dakota St.",
    "NorthTexas": "North Texas",
    "No.Colorado": "Northern Colorado",
    "NorthernIowa": "Northern Iowa",
    "NorthernKentucky": "Northern Kentucky",
    "NorthwesternSt": "Northwestern St.",
    "NotreDame": "Notre Dame",
    "OhioState": "Ohio St.",
    "OklahomaState": "Oklahoma St.",
    "OldDominion": "Old Dominion",
    "OralRoberts": "Oral Roberts",
    "OregonState": "Oregon St.",
    "Pennsylvania": "Penn",
    "PennState": "Penn St.",
    "PortlandState": "Portland St.",
    "RhodeIsland": "Rhode Island",
    "RobertMorris": "Robert Morris",
    # SIU Edwardsville
    "St.Josephs": "Saint Joseph's",
    "SaintLouis": "Saint Louis",
    "SaintMarysCA": "Saint Mary's",
    "St.Peter's": "Saint Peter's",
    "SamHouston": "Sam Houston St.",
    "SamHoustonSt": "Sam Houston St.",
    "SanDiego": "San Diego",
    "SanDiegoState": "San Diego St.",
    "SanFrancisco": "San Francisco",
    "SetonHall": "Seton Hall",
    "SouthAlabama": "South Alabama",
    "SouthCarolina": "South Carolina",
    "SouthDakotaSt": "South Dakota St.",
    "SouthDakotaState": "South Dakota St.",
    "SouthFlorida": "South Florida",
    "SouthernMiss": "Southern Miss",
    "St.Bonaventure": "St. Bonaventure",
    "St.Johns": "St. John's",
    "StephenAustin": "Stephen F. Austin",
    "StephenF.Austin": "Stephen F. Austin",
    "StonyBrook": "Stony Brook",
    "TexasA&M": "Texas A&M",
    "TexasA&MCorpus": "Texas A&M Corpus Chris",
    "TexasSouthern": "Texas Southern",
    "TexasTech": "Texas Tech",
    "UCDavis": "UC Davis",
    "CalIrvine": "UC Irvine",
    # UC San Diego
    "CalSantaBarb": "UC Santa Barbara",
    "CentralFlorida": "UCF",
    "MDBaltimoreCo": "UMBC",
    "NCAsheville": "UNC Asheville",
    "NCGreensboro": "UNC Greensboro",
    "NCWilmington": "UNC Wilmington",
    "TexasArlington": "UT Arlington",
    "TexSanAntonio": "UTSA",
    "UtahU": "Utah",
    "UtahState": "Utah St.",
    "VaCommonwealth": "VCU",
    "VirginiaTech": "Virginia Tech",
    "WakeForest": "Wake Forest",
    "WashingtonU": "Washington",
    "WashingtonState": "Washington St.",
    "WeberState": "Weber St.",
    "WestVirginia": "West Virginia",
    "WesternKentucky": "Western Kentucky",
    "WesternMichigan": "Western Michigan",
    "WichitaState": "Wichita St.",
    "WrightState": "Wright St.",
}

cleaned_odds_df = pd.read_csv(base_dir / "data" / "cleaned_historical_odds.csv")
historical_data_df = pd.read_csv(base_dir / "data" / "historical_data.csv")

# with open(base_dir / "data" / "tournament_teams.txt", "r") as fp:
    # all_tournament_teams = set(fp.read().splitlines())
cleaned_odds_df["TEAM T1"] = cleaned_odds_df["TEAM T1"].replace(TEAM_NAME_MAPPING)
cleaned_odds_df["TEAM T2"] = cleaned_odds_df["TEAM T2"].replace(TEAM_NAME_MAPPING)

# cleaned_odds_df.to_csv(base_dir / "data" / "mapped_historical_odds.csv", index=False)

# print(cleaned_odds_df.head())
# print(historical_data_df.head())

combined_data_df = pd.merge(historical_data_df, cleaned_odds_df, on=["YEAR", "TEAM T1", "TEAM T2"], how="left")
# remove duplicate UNC vs Notre Dame matchup
# played against each other twice in March 2016, for ACC tournament and actual tournament
combined_data_df = combined_data_df.drop_duplicates(subset=["YEAR", "TEAM T1", "TEAM T2"], keep="last")
print(historical_data_df.shape)
print(combined_data_df.shape)
print(combined_data_df.isna().sum())

missing = combined_data_df[combined_data_df["ML T1"].isna()]
print(missing["YEAR"].value_counts().sort_index())

combined_data_df.to_csv(base_dir / "data" / "final_training_data.csv", index=False)

# Kansas vs Michigan St 2009 PICKEM

# UNLV vs Northern Iowa 2010 3/18 PICKEM

# Gonzaga vs St John's 2011 PICKEM
# A&M vs Florida St 2011 PICKEM
# Michigan vs Tennessee 2011 PICKEM

# Vanderbilt vs Wisconsin 2012 PICKEM

# Wisconsin vs Kentucky 2014 PICKEM
# Connecticut vs Iowa St 2014 PICKEM

# Wichita St vs Kansas 2015 PICKEM
# Oregon vs Oklahoma St 2015 PICKEM

# Wichita St vs Arizona 2016 PICKEM

# Michigan vs Oregon 2017 PICKEM

# Nevada vs Texas 2018 PICKEM

# Florida St vs Colorado 2021 PICKEM

# Duke vs Texas Tech 2022 PICKEM