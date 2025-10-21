##Q-1:

import pandas as pd
import numpy as np
import warnings

warnings.filterwarnings('ignore')


def answer_one():
    # --- Load Energy Indicators ---
    Energy = pd.read_excel(r"C:\Users\THINKPAD\Downloads\Energy Indicators.xls", skiprows=17, skipfooter=38, usecols="C:F")
    Energy.columns = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']

    # Replace '...' with np.nan
    Energy.replace('...', np.nan, inplace=True)

    # Convert Energy Supply to gigajoules (from petajoules)
    Energy['Energy Supply'] = Energy['Energy Supply'] * 1_000_000

    # Clean country names
    Energy['Country'] = Energy['Country'].str.replace(r"\(.*\)", "", regex=True)  # Remove parentheses
    Energy['Country'] = Energy['Country'].str.replace(r"\d+", "", regex=True)  # Remove digits
    Energy['Country'] = Energy['Country'].str.strip()  # Remove leading/trailing spaces

    # Rename specific countries
    Energy.replace({"Republic of Korea": "South Korea",
                    "United States of America": "United States",
                    "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
                    "China, Hong Kong Special Administrative Region": "Hong Kong"}, inplace=True)

    # --- Load GDP ---
    GDP = pd.read_csv(r"C:\Users\THINKPAD\Downloads\world_bank.csv", skiprows=4)

    # Rename countries
    GDP.replace({"Korea, Rep.": "South Korea",
                 "Iran, Islamic Rep.": "Iran",
                 "Hong Kong SAR, China": "Hong Kong"}, inplace=True)

    # Keep last 10 years only (2006-2015)
    years = list(map(str, range(2006, 2016)))
    GDP = GDP[['Country Name'] + years].rename(columns={'Country Name': 'Country'})

    # --- Load ScimEn ---
    ScimEn = pd.read_excel(r"C:\Users\THINKPAD\Downloads\scimagojr-3.xlsx")

    # Keep top 15 only
    ScimEn_top15 = ScimEn[ScimEn['Rank'] <= 15]

    # --- Merge all datasets ---
    df = pd.merge(ScimEn_top15, Energy, how='inner', on='Country')
    df = pd.merge(df, GDP, how='inner', on='Country')

    # Set Country as index and sort by Rank
    df.set_index('Country', inplace=True)
    df = df.sort_values('Rank')

    return df

#df = answer_one()
#print(df.head())
#print(df.shape)

##Q-2:
def answer_two():
    # Load datasets as in Q1
    Energy = pd.read_excel(r"C:\Users\THINKPAD\Downloads\Energy Indicators.xls", skiprows=17, skipfooter=38, usecols="C:F")
    Energy.columns = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']
    Energy.replace('...', np.nan, inplace=True)
    Energy['Energy Supply'] = Energy['Energy Supply'] * 1_000_000
    Energy['Country'] = Energy['Country'].str.replace(r"\(.*\)", "", regex=True)
    Energy['Country'] = Energy['Country'].str.replace(r"\d+", "", regex=True)
    Energy['Country'] = Energy['Country'].str.strip()
    Energy.replace({"Republic of Korea": "South Korea",
                    "United States of America": "United States",
                    "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
                    "China, Hong Kong Special Administrative Region": "Hong Kong"}, inplace=True)

    GDP = pd.read_csv(r"C:\Users\THINKPAD\Downloads\world_bank.csv", skiprows=4)
    GDP.replace({"Korea, Rep.": "South Korea",
                 "Iran, Islamic Rep.": "Iran",
                 "Hong Kong SAR, China": "Hong Kong"}, inplace=True)
    GDP = GDP.rename(columns={'Country Name': 'Country'})

    ScimEn = pd.read_excel(r"C:\Users\THINKPAD\Downloads\scimagojr-3.xlsx")

    # Entries before merging
    total_entries_before = len(set(Energy['Country']).union(set(GDP['Country'])).union(set(ScimEn['Country'])))

    # Merge
    merged = pd.merge(ScimEn, Energy, how='inner', on='Country')
    merged = pd.merge(merged, GDP, how='inner', on='Country')

    # Entries after merging
    total_entries_after = len(merged)

    # Entries lost
    lost_entries = total_entries_before - total_entries_after

    return lost_entries

#print(answer_two())

##Q-3:
def answer_three():
    Top15 = answer_one()
    years = list(map(str, range(2006, 2016)))
    avgGDP = Top15[years].mean(axis=1).sort_values(ascending=False)
    return avgGDP

#print(answer_three())

##Q-4:
def answer_four():
    Top15 = answer_one()
    years = list(map(str, range(2006, 2016)))
    avgGDP = Top15[years].mean(axis=1).sort_values(ascending=False)
    country6 = avgGDP.index[5]  # 6th largest average GDP
    gdp_change = Top15.loc[country6, '2015'] - Top15.loc[country6, '2006']
    return gdp_change

#print(answer_four())

##Q-5:
def answer_five():
    Top15 = answer_one()
    return Top15['Energy Supply per Capita'].mean()
#print(answer_five())

##Q-6:
def answer_six():
    Top15 = answer_one()
    country = Top15['% Renewable'].idxmax()
    value = Top15['% Renewable'].max()
    return (country, value)

#print(answer_six())

##Q-7:
def answer_seven():
    Top15 = answer_one()
    Top15['Ratio'] = Top15['Self-citations'] / Top15['Citations']
    country = Top15['Ratio'].idxmax()
    value = Top15['Ratio'].max()
    return (country, value)

#print(answer_seven())

##Q-8:
def answer_eight():
    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    third_country = Top15['PopEst'].sort_values(ascending=False).index[2]
    return third_country

#print(answer_eight())

##Q-9:
def answer_nine():
    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15['Citable docs per Capita'] = Top15['Citable documents'] / Top15['PopEst']
    correlation = Top15['Citable docs per Capita'].corr(Top15['Energy Supply per Capita'])
    return correlation

# Test Q9
#print(answer_nine())

##Q-10:
def answer_ten():
    Top15 = answer_one()
    median_renew = Top15['% Renewable'].median()
    HighRenew = (Top15['% Renewable'] >= median_renew).astype(int)
    HighRenew = HighRenew.sort_index()
    return HighRenew

#print(answer_ten())

##Q-11:
def answer_eleven():
    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']

    ContinentDict = {'China':'Asia',
                     'United States':'North America',
                     'Japan':'Asia',
                     'United Kingdom':'Europe',
                     'Russian Federation':'Europe',
                     'Canada':'North America',
                     'Germany':'Europe',
                     'India':'Asia',
                     'France':'Europe',
                     'South Korea':'Asia',
                     'Italy':'Europe',
                     'Spain':'Europe',
                     'Iran':'Asia',
                     'Australia':'Australia',
                     'Brazil':'South America'}

    df = Top15.copy()
    df['Continent'] = df.index.map(ContinentDict)
    result = df.groupby('Continent')['PopEst'].agg(['size','sum','mean','std'])
    return result

#print(answer_eleven())

##Q-12:
def answer_twelve():
    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']

    ContinentDict = {'China':'Asia',
                     'United States':'North America',
                     'Japan':'Asia',
                     'United Kingdom':'Europe',
                     'Russian Federation':'Europe',
                     'Canada':'North America',
                     'Germany':'Europe',
                     'India':'Asia',
                     'France':'Europe',
                     'South Korea':'Asia',
                     'Italy':'Europe',
                     'Spain':'Europe',
                     'Iran':'Asia',
                     'Australia':'Australia',
                     'Brazil':'South America'}

    df = Top15.copy()
    df['Continent'] = df.index.map(ContinentDict)
    df['% Renewable Bin'] = pd.cut(df['% Renewable'], 5)
    grouped = df.groupby(['Continent','% Renewable Bin']).size()
    return grouped

#print(answer_twelve())

##Q-13:
def answer_thirteen():
    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    PopEst_str = Top15['PopEst'].apply(lambda x: f"{x:,.2f}")
    return PopEst_str

#print(answer_thirteen())
