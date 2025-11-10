#Question 1:
import pandas as pd
import numpy as np
import re
import scipy.stats as stats

# --- Helpers ---
def nhl_correlation():
    NHL_df=pd.read_csv("assets/nhl.csv")
    cities = pd.read_html("assets/wikipedia_data.html")[1]
    cities = cities.iloc[:-1, [0, 3, 5, 6, 7, 8]]
    NHL_df=NHL_df[NHL_df.year==2018]
    NHL_df=NHL_df[["team","W","L"]]
    def remove_star(team):
        if "*" in team:
            return re.findall("([\w\s]*)\*",team)[0]
        else:
            return team
    NHL_df["team"]=NHL_df.team.apply(remove_star)
    
    
    #NHL_df.to_excel("NHL.xlsx")
    #return
    def remove_bracket(team):
        if "[" in team:
            return re.findall("([\w\s]*)\[",team)[0]
        else:
            return team
    cities["NHL"]=cities.NHL.apply(remove_bracket)
    
    cities=cities[['Metropolitan area', 'Population (2016 est.)[8]','NHL']]
    NHL_df["team_only"]=NHL_df.team.apply(lambda x:x.rsplit(None,1)[-1])
    
    
    NHL_df.loc[3,"team_only"]="Maple Leafs"
    NHL_df.loc[5,"team_only"]="Red Wings"
    NHL_df.loc[13,"team_only"]="Blue Jackets"
    NHL_df.loc[27,"team_only"]="Golden Knights"
    
    NHL_df.loc[14,"team_only"]="Rangers Islanders Devils"
    NHL_df.loc[16,"team_only"]="Rangers Islanders Devils"
    NHL_df.loc[17,"team_only"]="Rangers Islanders Devils"
    
    NHL_df.loc[28,"team_only"]="Kings Ducks"
    NHL_df.loc[30,"team_only"]="Kings Ducks"
    
    
    cities.rename(columns={'Metropolitan area':"city", 'Population (2016 est.)[8]':"population",'NHL':"team_only"},inplace=True)
    
    # Drop division rows
    divisions = [
    "Atlantic Division", "Metropolitan Division", "Central Division", "Pacific Division"]
    NHL_df = NHL_df[~NHL_df["team"].isin(divisions)]
    
    NHL_df.W=NHL_df.W.astype(float)
    NHL_df.L=NHL_df.L.astype(float)
    
    NHL_df = NHL_df.groupby("team_only")[["W", "L"]].mean().reset_index()
    
    merged_df=pd.merge(NHL_df, cities, how= "inner", on="team_only")
    #return merged_df
    #return merged_df.dtypes
    
    merged_df["win_loss_ratio"]=merged_df.W / (merged_df.W + merged_df.L)
    #return merged_df
    #return len(merged_df)
    
    population_by_region=pd.to_numeric(merged_df["population"],errors="coerce")
    win_loss_by_region=pd.to_numeric(merged_df["win_loss_ratio"],errors="coerce")
    assert len(population_by_region)== len(win_loss_by_region)
    assert len(population_by_region)== 28
    
    #NHL_df.to_excel("NHL.xlsx")
    #cities.to_excel("Cities.xlsx")
    return stats.pearsonr(population_by_region,win_loss_by_region)[0]
    
nhl_correlation()

#Question 2:
import pandas as pd
import numpy as np
import re
import scipy.stats as stats

# --- Helpers ---


def nba_correlation():
    nba_df=pd.read_csv("assets/nba.csv")
    cities = pd.read_html("assets/wikipedia_data.html")[1]
    cities = cities.iloc[:-1, [0, 3, 5, 6, 7, 8]]
    nba_df=nba_df[nba_df.year==2018]
    nba_df["team"]=nba_df.team.apply(lambda team: re.findall("([\w\s]*)\*",team)[0] if "*" in team else team)
    
    #return cities.columns
    
    
    nba_df["team"]=nba_df.team.apply(lambda team: re.findall("([\w\s]*)\(",team)[0] if "(" in team else team)
    cities["NBA"]=cities.NBA.apply(lambda team: re.findall("([\w\s]*)\[",team)[0] if "[" in team else team)
    cities=cities[['Metropolitan area', 'Population (2016 est.)[8]','NBA']]
    #return cities
    
    nba_df=nba_df[["team","W","L"]]
    nba_df["team_only"]=nba_df.team.apply(lambda x:x.rsplit(None,1)[-1])
    
    nba_df.loc[17,"team_only"]="Trail Blazers"
    
    nba_df.loc[10,"team_only"]="Knicks Nets"
    nba_df.loc[11,"team_only"]="Knicks Nets"
    nba_df.loc[24,"team_only"]="Lakers Clippers"
    nba_df.loc[25,"team_only"]="Lakers Clippers"
    
    cities.rename(columns={'Metropolitan area':"city", 'Population (2016 est.)[8]':"population",'NBA':"team_only"},inplace=True)
    
    #nba_df=nba_df[~nba_df.W.str.contains("Division")]
    
    nba_df.W=nba_df.W.astype(float)
    nba_df.L=nba_df.L.astype(float)
    
    nba_df = nba_df.groupby("team_only")[["W", "L"]].mean().reset_index()
    merged_df=pd.merge(nba_df, cities, how= "inner", on="team_only")
    
    merged_df.W=merged_df.W.astype(float)
    merged_df.L=merged_df.L.astype(float)
    merged_df["win_loss_ratio"]=merged_df.W / (merged_df.W + merged_df.L)
    #return len(merged_df)
    #nba_df.to_excel("NBA.xlsx")
    #return merged_df
    population_by_region=pd.to_numeric(merged_df["population"],errors="coerce")
    win_loss_by_region=pd.to_numeric(merged_df["win_loss_ratio"],errors="coerce")
    assert len(population_by_region)== len(win_loss_by_region)
    assert len(population_by_region)== 28
    
    #NHL_df.to_excel("NHL.xlsx")
    #cities.to_excel("Cities.xlsx")
    return stats.pearsonr(population_by_region,win_loss_by_region)[0]
    
nba_correlation()

#Question 3:
import pandas as pd
import numpy as np
import re
import scipy.stats as stats

# --- Helpers ---


def mlb_correlation():
    mlb_df=pd.read_csv("assets/mlb.csv")
    cities = pd.read_html("assets/wikipedia_data.html")[1]
    cities = cities.iloc[:-1, [0, 3, 5, 6, 7, 8]]
    
    cities["MLB"]=cities.MLB.apply(lambda team: re.findall("([\w\s]*)\[",team)[0] if "[" in team else team)
    cities=cities[['Metropolitan area', 'Population (2016 est.)[8]','MLB']]
    cities.rename(columns={'Metropolitan area':"city", 'Population (2016 est.)[8]':"population",'MLB':"team_only"},inplace=True)
    
    mlb_df=mlb_df[mlb_df.year==2018]
    mlb_df=mlb_df[["team","W","L"]]
    mlb_df["team_only"]=mlb_df.team.apply(lambda x:x.rsplit(None,1)[-1])
    
    #return cities,mlb_df
    mlb_df.loc[0,"team_only"]="Red Sox"
    mlb_df.loc[3,"team_only"]="Blue Jays"
    #mlb_df.loc[8,"team_only"]="White Sox"
    
    
    mlb_df.loc[1,"team_only"]="Yankees Mets"
    mlb_df.loc[18,"team_only"]="Yankees Mets"
    mlb_df.loc[13,"team_only"]="Dodgers Angels"
    mlb_df.loc[25,"team_only"]="Dodgers Angels"
    mlb_df.loc[8,"team_only"]="Cubs White Sox"
    mlb_df.loc[21,"team_only"]="Cubs White Sox"
    mlb_df.loc[11,"team_only"]="Giants Athletics"
    mlb_df.loc[28,"team_only"]="Giants Athletics"
    
    
    mlb_df.W=mlb_df.W.astype(float)
    mlb_df.L=mlb_df.L.astype(float)
    mlb_df = mlb_df.groupby("team_only")[["W", "L"]].mean().reset_index()
    merged_df=pd.merge(mlb_df, cities, how= "inner", on="team_only")
    
    merged_df.W=merged_df.W.astype(float)
    merged_df.L=merged_df.L.astype(float)
    merged_df["win_loss_ratio"]=merged_df.W / (merged_df.W + merged_df.L)
    
    
    #return len(merged_df)
    #mlb_df.to_excel("MLB.xlsx")
    #return cities,mlb_df
    population_by_region=pd.to_numeric(merged_df["population"],errors="coerce")
    win_loss_by_region=pd.to_numeric(merged_df["win_loss_ratio"],errors="coerce")
    assert len(population_by_region)== len(win_loss_by_region)
    assert len(population_by_region)== 26
    
    #mlb_df.to_excel("MLB.xlsx")
    #cities.to_excel("Cities3.xlsx")
    return stats.pearsonr(population_by_region,win_loss_by_region)[0]

mlb_correlation()

#Question 4:
import pandas as pd
import numpy as np
import re
import scipy.stats as stats

# --- Helpers ---


def nfl_correlation():
    nfl_df=pd.read_csv("assets/nfl.csv")
    cities = pd.read_html("assets/wikipedia_data.html")[1]
    cities = cities.iloc[:-1, [0, 3, 5, 6, 7, 8]]
    
    cities["NFL"]=cities.NFL.apply(lambda team: re.findall("([\w\s]*)\[",team)[0] if "[" in team else team)
    cities=cities[['Metropolitan area', 'Population (2016 est.)[8]','NFL']]
    cities.rename(columns={'Metropolitan area':"city", 'Population (2016 est.)[8]':"population",'NFL':"team_only"},inplace=True)
    
    nfl_df=nfl_df[nfl_df.year==2018]
    nfl_df=nfl_df[~nfl_df.W.str.contains("|".join(["AFC","NFC"]))]
    nfl_df["team"]=nfl_df.team.apply(lambda team: re.findall("([\w\s]*)\*",team)[0] if "*" in team else team)
    nfl_df["team"]=nfl_df.team.apply(lambda team: re.findall("([\w\s]*)\+",team)[0] if "+" in team else team)
    nfl_df=nfl_df[["team","W","L"]]
    nfl_df["team_only"]=nfl_df.team.apply(lambda x:x.rsplit(None,1)[-1])
    
    #return cities, nfl_df
    nfl_df.loc[4,"team_only"]="Giants Jets"
    nfl_df.loc[24,"team_only"]="Giants Jets"    
    
    nfl_df.loc[17,"team_only"]="Rams Chargers"
    nfl_df.loc[36,"team_only"]="Rams Chargers"
    nfl_df.loc[19,"team_only"]="49ers Raiders"
    nfl_df.loc[38,"team_only"]="49ers Raiders"
    
    
    nfl_df.W=nfl_df.W.astype(float)
    nfl_df.L=nfl_df.L.astype(float)
    nfl_df = nfl_df.groupby("team_only")[["W", "L"]].mean().reset_index()
    merged_df=pd.merge(nfl_df, cities, how= "inner", on="team_only")
    
    merged_df.W=merged_df.W.astype(float)
    merged_df.L=merged_df.L.astype(float)
    merged_df["win_loss_ratio"]=merged_df.W / (merged_df.W + merged_df.L)
    
    
    #return len(merged_df)
    #mlb_df.to_excel("MLB.xlsx")
    #return cities,mlb_df
    population_by_region=pd.to_numeric(merged_df["population"],errors="coerce")
    win_loss_by_region=pd.to_numeric(merged_df["win_loss_ratio"],errors="coerce")
    assert len(population_by_region)== len(win_loss_by_region)
    assert len(population_by_region)== 29
    
    #mlb_df.to_excel("MLB.xlsx")
    #cities.to_excel("Cities3.xlsx")
    return stats.pearsonr(population_by_region,win_loss_by_region)[0]

nfl_correlation()
