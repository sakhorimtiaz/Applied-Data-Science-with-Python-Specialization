##Q-1
####practice
import pandas as pd
import re
cities = pd.read_html(r"C:\Users\THINKPAD\Downloads\wikipedia_data.html")[1]
cities=cities.iloc[:-1,[0,3,5,6,7,8]]
#rename for clarity
cities.columns = ['Metropolitan area', 'Population', 'NFL', 'MLB', 'NBA', 'NHL']
#print(cities)

nhl_df = pd.read_csv(r"C:\Users\THINKPAD\Downloads\nhl.csv")
#print(nhl_df.columns)
nhl_df=nhl_df[["team","W","L"]]
#print(nhl_df.head())
#cleaning non-numeric values
nhl_df['W'] = pd.to_numeric(nhl_df['W'], errors='coerce')
nhl_df['L'] = pd.to_numeric(nhl_df['L'], errors='coerce')
nhl_df = nhl_df.dropna(subset=['W', 'L'])

nhl_df["win_loss_ratio"]=nhl_df["W"]/(nhl_df["W"]+nhl_df["L"])
#print(nhl_df.head())

metro_to_teams = {}
for index,row in cities.iterrows():
    metro_area=row['Metropolitan area']
    teams=row['NHL']
    teams = re.split(r',|\s(?=[A-Z])', str(row['NHL']))
    # some cells have multiple teams
    metro_to_teams[metro_area] = teams

#print(metro_to_teams)

###clean
import re

cleaned_dict = {}

for city, teams in metro_to_teams.items():
    cleaned_teams = []
    for team in teams:
        # remove bracketed notes like [note 13]
        team = re.sub(r'\[.*?\]', '', team)
        team = team.replace('—', '').strip()
        if team:  # only add if non-empty after cleaning
            cleaned_teams.append(team)
    cleaned_dict[city] = cleaned_teams

#print(cleaned_dict)

population_by_region = []
win_loss_by_region = []

for city, teams in cleaned_dict.items():
    # Skip cities without any teams
    if not teams:
        continue

    # Find win/loss ratios for each team in that metro
    ratios = []
    for team in teams:
        # check if any NHL team name is in nhl_df["team"]
        mask = nhl_df['team'].str.contains(team, case=False, na=False)
        city_teams = nhl_df[mask]
        if not city_teams.empty:
            ratios.extend(city_teams['win_loss_ratio'].tolist())

    # Only proceed if we found valid ratios
    if ratios:
        avg_ratio = sum(ratios) / len(ratios)
        win_loss_by_region.append(avg_ratio)

        # Clean population (remove commas and convert to float)
        pop = float(str(cities.loc[cities['Metropolitan area'] == city, 'Population'].values[0]).replace(',', ''))
        population_by_region.append(pop)

for city, teams in cleaned_dict.items():
    found = False
    for team in teams:
        if nhl_df['team'].str.contains(team, case=False, na=False).any():
            found = True
    if not found and teams:
        print("No match found for:", city, "→", teams)

from scipy.stats import pearsonr
print(pearsonr(population_by_region, win_loss_by_region))
print(len(population_by_region), len(win_loss_by_region))

###Final answer
#Q-1
import pandas as pd
import numpy as np
import scipy.stats as stats
import re

def nhl_correlation():
    # --- Load data ---
    nhl_df = pd.read_csv(r"C:\Users\THINKPAD\Downloads\nhl.csv")
    cities = pd.read_html(r"C:\Users\THINKPAD\Downloads\wikipedia_data.html")[1]
    cities = cities.iloc[:-1, [0, 3, 5, 6, 7, 8]]
    cities.columns = ['Metropolitan area', 'Population', 'NFL', 'MLB', 'NBA', 'NHL']

    # --- Clean and compute win/loss ratio ---
    nhl_df = nhl_df[['team', 'W', 'L']]
    nhl_df['W'] = pd.to_numeric(nhl_df['W'], errors='coerce')
    nhl_df['L'] = pd.to_numeric(nhl_df['L'], errors='coerce')
    nhl_df = nhl_df.dropna(subset=['W', 'L'])
    nhl_df['win_loss_ratio'] = nhl_df['W'] / (nhl_df['W'] + nhl_df['L'])

    # --- Build metro → team dictionary ---
    metro_to_teams = {}
    for _, row in cities.iterrows():
        teams = re.split(r',|\s(?=[A-Z])', str(row['NHL']))
        metro_to_teams[row['Metropolitan area']] = teams

    # --- Clean team names ---
    cleaned_dict = {}
    for city, teams in metro_to_teams.items():
        cleaned = []
        for team in teams:
            team = re.sub(r'\[.*?\]', '', team)
            team = team.replace('—', '').strip()
            if team:
                cleaned.append(team)
        cleaned_dict[city] = cleaned

    # --- Compute population & average win/loss ratio by region ---
    population_by_region = []
    win_loss_by_region = []

    for city, teams in cleaned_dict.items():
        if not teams:
            continue
        ratios = []
        for team in teams:
            mask = nhl_df['team'].str.contains(team, case=False, na=False)
            matches = nhl_df[mask]
            if not matches.empty:
                ratios.extend(matches['win_loss_ratio'].tolist())

        if ratios:
            avg_ratio = sum(ratios) / len(ratios)
            win_loss_by_region.append(avg_ratio)

            pop = float(str(cities.loc[cities['Metropolitan area'] == city, 'Population'].values[0]).replace(',', ''))
            population_by_region.append(pop)

    # --- Assertions for correctness ---
    assert len(population_by_region) == len(win_loss_by_region), "Lists must match in length"
    assert len(population_by_region) == 28, "There should be 28 metropolitan areas"

    # --- Return correlation result ---
    return stats.pearsonr(population_by_region, win_loss_by_region)

print(nhl_correlation())
