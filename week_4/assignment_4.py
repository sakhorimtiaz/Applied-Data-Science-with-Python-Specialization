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
nhl_df = nhl_df[nhl_df['year'] == 2018]
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
    nhl_df = nhl_df[nhl_df['year'] == 2018]
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


##Question-2
###Practice:
import pandas as pd
import re
cities = pd.read_html(r"C:\Users\THINKPAD\Downloads\wikipedia_data.html")[1]
cities=cities.iloc[:-1,[0,3,5,6,7,8]]
#rename for clarity
cities.columns = ['Metropolitan area', 'Population', 'NFL', 'MLB', 'NBA', 'NHL']
#print(cities)

nba_df = pd.read_csv(r"C:\Users\THINKPAD\Downloads\nba.csv")
#print(nhl_df.columns)
nba_df = nba_df[nba_df['year'] == 2018]
nba_df=nba_df[["team","W","L","W/L%"]]
nba_df=nba_df.rename(columns={"W/L%":"win_loss_ratio"})
nba_df['W'] = pd.to_numeric(nba_df['W'], errors='coerce')
nba_df['L'] = pd.to_numeric(nba_df['L'], errors='coerce')
nba_df['win_loss_ratio'] = pd.to_numeric(nba_df['win_loss_ratio'], errors='coerce')



print(nba_df.head())

metro_to_teams = {}
for index,row in cities.iterrows():
    metro_area=row['Metropolitan area']
    teams=row['NHL']
    teams = re.split(r',|\s(?=[A-Z])', str(row['NBA']))
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
        mask = nba_df['team'].str.contains(team, case=False, na=False)
        city_teams = nba_df[mask]
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
        if nba_df['team'].str.contains(team, case=False, na=False).any():
            found = True
    if not found and teams:
        print("No match found for:", city, "→", teams)

from scipy.stats import pearsonr
print(pearsonr(population_by_region, win_loss_by_region))
print(len(population_by_region), len(win_loss_by_region))

###Final Answer
#Q-2
import pandas as pd
import re
from scipy.stats import pearsonr

def nba_correlation():
    # --- Read data ---
    nba_df = pd.read_csv(r"C:\Users\THINKPAD\Downloads\nba.csv")
    cities = pd.read_html(r"C:\Users\THINKPAD\Downloads\wikipedia_data.html")[1]
    cities = cities.iloc[:-1,[0,3,5,6,7,8]]
    cities.columns = ['Metropolitan area', 'Population', 'NFL', 'MLB', 'NBA', 'NHL']

    # --- Filter NBA data for 2018 and select necessary columns ---
    nba_df = nba_df[nba_df['year'] == 2018]
    nba_df = nba_df[['team', 'W', 'L', 'W/L%']]
    nba_df = nba_df.rename(columns={'W/L%': 'win_loss_ratio'})
    nba_df['W'] = pd.to_numeric(nba_df['W'], errors='coerce')
    nba_df['L'] = pd.to_numeric(nba_df['L'], errors='coerce')
    nba_df['win_loss_ratio'] = pd.to_numeric(nba_df['win_loss_ratio'], errors='coerce')

    # --- Map metro areas to NBA teams ---
    metro_to_teams = {}
    for index, row in cities.iterrows():
        metro_area = row['Metropolitan area']
        teams = re.split(r',|\s(?=[A-Z])', str(row['NBA']))
        metro_to_teams[metro_area] = teams

    # --- Clean team names ---
    cleaned_dict = {}
    for city, teams in metro_to_teams.items():
        cleaned_teams = []
        for team in teams:
            team = re.sub(r'\[.*?\]', '', team)
            team = team.replace('—', '').strip()
            if team:
                cleaned_teams.append(team)
        cleaned_dict[city] = cleaned_teams

    # --- Compute population and average win/loss per metro ---
    population_by_region = []
    win_loss_by_region = []

    for city, teams in cleaned_dict.items():
        if not teams:
            continue
        ratios = []
        for team in teams:
            mask = nba_df['team'].str.contains(team, case=False, na=False)
            city_teams = nba_df[mask]
            if not city_teams.empty:
                ratios.extend(city_teams['win_loss_ratio'].tolist())
        if ratios:
            avg_ratio = sum(ratios) / len(ratios)
            win_loss_by_region.append(avg_ratio)
            pop = float(str(cities.loc[cities['Metropolitan area'] == city, 'Population'].values[0]).replace(',', ''))
            population_by_region.append(pop)

    # --- Optional: check unmatched cities ---
    for city, teams in cleaned_dict.items():
        found = False
        for team in teams:
            if nba_df['team'].str.contains(team, case=False, na=False).any():
                found = True
        if not found and teams:
            print("No match found for:", city, "→", teams)

    # --- Assertions ---
    assert len(population_by_region) == len(win_loss_by_region), "Q2: Your lists must be the same length"
    assert len(population_by_region) == 28, "Q2: There should be 28 teams being analysed for NBA"

    # --- Compute correlation ---
    return pearsonr(population_by_region, win_loss_by_region)

# --- Call function ---
corr_result = nba_correlation()
print(corr_result)

####Q-3
##Practice
import pandas as pd
import re
cities = pd.read_html(r"C:\Users\THINKPAD\Downloads\wikipedia_data.html")[1]
cities=cities.iloc[:-1,[0,3,5,6,7,8]]
#rename for clarity
cities.columns = ['Metropolitan area', 'Population', 'NFL', 'MLB', 'NBA', 'NHL']
#print(cities)

mlb_df = pd.read_csv(r"C:\Users\THINKPAD\Downloads\mlb.csv")
#print(nhl_df.columns)
mlb_df = mlb_df[mlb_df['year'] == 2018]
mlb_df=mlb_df[["team","W","L","W-L%"]]
mlb_df=mlb_df.rename(columns={"W-L%":"win_loss_ratio"})
mlb_df['W'] = pd.to_numeric(mlb_df['W'], errors='coerce')
mlb_df['L'] = pd.to_numeric(mlb_df['L'], errors='coerce')
mlb_df['win_loss_ratio'] = pd.to_numeric(mlb_df['win_loss_ratio'], errors='coerce')



print(mlb_df.head())

metro_to_teams = {}
for index,row in cities.iterrows():
    metro_area=row['Metropolitan area']
    teams=row['MLB']
    teams = re.split(r',|\s(?=[A-Z])', str(row['MLB']))
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
        mask = mlb_df['team'].str.contains(team, case=False, na=False)
        city_teams = mlb_df[mask]
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
        if mlb_df['team'].str.contains(team, case=False, na=False).any():
            found = True
    if not found and teams:
        print("No match found for:", city, "→", teams)

from scipy.stats import pearsonr
print(pearsonr(population_by_region, win_loss_by_region))
print(len(population_by_region), len(win_loss_by_region))

####Final answer
#Q-3
import pandas as pd
import re
from scipy.stats import pearsonr

def mlb_correlation():
    # --- Read data ---
    mlb_df = pd.read_csv(r"C:\Users\THINKPAD\Downloads\mlb.csv")
    cities = pd.read_html(r"C:\Users\THINKPAD\Downloads\wikipedia_data.html")[1]
    cities = cities.iloc[:-1,[0,3,5,6,7,8]]
    cities.columns = ['Metropolitan area', 'Population', 'NFL', 'MLB', 'NBA', 'NHL']

    # --- Filter MLB data for 2018 and select necessary columns ---
    mlb_df = mlb_df[mlb_df['year'] == 2018]
    mlb_df = mlb_df[['team', 'W', 'L', 'W-L%']]
    mlb_df = mlb_df.rename(columns={'W-L%': 'win_loss_ratio'})
    mlb_df['W'] = pd.to_numeric(mlb_df['W'], errors='coerce')
    mlb_df['L'] = pd.to_numeric(mlb_df['L'], errors='coerce')
    mlb_df['win_loss_ratio'] = pd.to_numeric(mlb_df['win_loss_ratio'], errors='coerce')

    # --- Map metro areas to MLB teams ---
    metro_to_teams = {}
    for index, row in cities.iterrows():
        metro_area = row['Metropolitan area']
        teams = re.split(r',|\s(?=[A-Z])', str(row['MLB']))
        metro_to_teams[metro_area] = teams

    # --- Clean team names ---
    cleaned_dict = {}
    for city, teams in metro_to_teams.items():
        cleaned_teams = []
        for team in teams:
            team = re.sub(r'\[.*?\]', '', team)
            team = team.replace('—', '').strip()
            if team:
                cleaned_teams.append(team)
        cleaned_dict[city] = cleaned_teams

    # --- Compute population and average win/loss per metro ---
    population_by_region = []
    win_loss_by_region = []

    for city, teams in cleaned_dict.items():
        if not teams:
            continue
        ratios = []
        for team in teams:
            mask = mlb_df['team'].str.contains(team, case=False, na=False)
            city_teams = mlb_df[mask]
            if not city_teams.empty:
                ratios.extend(city_teams['win_loss_ratio'].tolist())
        if ratios:
            avg_ratio = sum(ratios) / len(ratios)
            win_loss_by_region.append(avg_ratio)
            pop = float(str(cities.loc[cities['Metropolitan area'] == city, 'Population'].values[0]).replace(',', ''))
            population_by_region.append(pop)

    # --- Optional: check unmatched cities ---
    for city, teams in cleaned_dict.items():
        found = False
        for team in teams:
            if mlb_df['team'].str.contains(team, case=False, na=False).any():
                found = True
        if not found and teams:
            print("No match found for:", city, "→", teams)

    # --- Assertions ---
    assert len(population_by_region) == len(win_loss_by_region), "Q3: Your lists must be the same length"
    assert len(population_by_region) == 26, "Q3: There should be 26 teams being analysed for MLB"

    # --- Compute correlation ---
    return pearsonr(population_by_region, win_loss_by_region)

# --- Call function ---
corr_result = mlb_correlation()
print(corr_result)

####Q-4
##practice:
import pandas as pd
import re
cities = pd.read_html(r"C:\Users\THINKPAD\Downloads\wikipedia_data.html")[1]
cities=cities.iloc[:-1,[0,3,5,6,7,8]]
#rename for clarity
cities.columns = ['Metropolitan area', 'Population', 'NFL', 'MLB', 'NBA', 'NHL']
#print(cities)

nfl_df = pd.read_csv(r"C:\Users\THINKPAD\Downloads\nfl.csv")
#print(nfl_df.columns)
nfl_df = nfl_df[nfl_df['year'] == 2018]
nfl_df=nfl_df[["team","W","L","W-L%"]]
nfl_df=nfl_df.rename(columns={"W-L%":"win_loss_ratio"})
nfl_df['W'] = pd.to_numeric(nfl_df['W'], errors='coerce')
nfl_df['L'] = pd.to_numeric(nfl_df['L'], errors='coerce')
nfl_df['win_loss_ratio'] = pd.to_numeric(nfl_df['win_loss_ratio'], errors='coerce')

print(nfl_df.head())

metro_to_teams = {}
for index,row in cities.iterrows():
    metro_area=row['Metropolitan area']
    teams=row['NFL']
    teams = re.split(r',|\s(?=[A-Z])', str(row['NFL']))
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
        mask = nfl_df['team'].str.contains(team, case=False, na=False)
        city_teams = nfl_df[mask]
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
        if nfl_df['team'].str.contains(team, case=False, na=False).any():
            found = True
    if not found and teams:
        print("No match found for:", city, "→", teams)

from scipy.stats import pearsonr
print(pearsonr(population_by_region, win_loss_by_region))
print(len(population_by_region), len(win_loss_by_region))

####Final answer:
##Q-4:
import pandas as pd
import numpy as np
import scipy.stats as stats
import re

def nfl_correlation():
    # --- Read city population data ---
    cities = pd.read_html(r"C:\Users\THINKPAD\Downloads\wikipedia_data.html")[1]
    cities = cities.iloc[:-1,[0,3,5,6,7,8]]
    cities.columns = ['Metropolitan area', 'Population', 'NFL', 'MLB', 'NBA', 'NHL']

    # --- Read NFL data for 2018 ---
    nfl_df = pd.read_csv(r"C:\Users\THINKPAD\Downloads\nfl.csv")
    nfl_df = nfl_df[nfl_df['year'] == 2018]
    nfl_df = nfl_df[["team","W","L","W-L%"]]
    nfl_df = nfl_df.rename(columns={"W-L%":"win_loss_ratio"})
    nfl_df['W'] = pd.to_numeric(nfl_df['W'], errors='coerce')
    nfl_df['L'] = pd.to_numeric(nfl_df['L'], errors='coerce')
    nfl_df['win_loss_ratio'] = pd.to_numeric(nfl_df['win_loss_ratio'], errors='coerce')

    # --- Map metro areas to teams ---
    metro_to_teams = {}
    for index,row in cities.iterrows():
        metro_area = row['Metropolitan area']
        teams = re.split(r',|\s(?=[A-Z])', str(row['NFL']))
        metro_to_teams[metro_area] = teams

    # --- Clean team names ---
    cleaned_dict = {}
    for city, teams in metro_to_teams.items():
        cleaned_teams = []
        for team in teams:
            team = re.sub(r'\[.*?\]', '', team)
            team = team.replace('—', '').strip()
            if team:
                cleaned_teams.append(team)
        cleaned_dict[city] = cleaned_teams

    # --- Compute population and win/loss ratio lists ---
    population_by_region = []
    win_loss_by_region = []

    for city, teams in cleaned_dict.items():
        if not teams:
            continue

        ratios = []
        for team in teams:
            mask = nfl_df['team'].str.contains(team, case=False, na=False)
            city_teams = nfl_df[mask]
            if not city_teams.empty:
                ratios.extend(city_teams['win_loss_ratio'].tolist())

        if ratios:
            avg_ratio = sum(ratios) / len(ratios)
            win_loss_by_region.append(avg_ratio)

            pop = float(str(cities.loc[cities['Metropolitan area'] == city, 'Population'].values[0]).replace(',', ''))
            population_by_region.append(pop)

    # Optional: print unmatched cities
    for city, teams in cleaned_dict.items():
        found = False
        for team in teams:
            if nfl_df['team'].str.contains(team, case=False, na=False).any():
                found = True
        if not found and teams:
            print("No match found for:", city, "→", teams)

    # --- Return Pearson correlation ---
    assert len(population_by_region) == len(win_loss_by_region), "Q4: Your lists must be the same length"
    assert len(population_by_region) == 29, "Q4: There should be 29 teams being analysed for NFL"
    return stats.pearsonr(population_by_region, win_loss_by_region)

print(nfl_correlation())
