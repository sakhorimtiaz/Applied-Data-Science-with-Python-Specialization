df=pd.read_csv(r"C:\Users\THINKPAD\Downloads\cwurData.csv")
print(df.head())

def create_category(ranking):
    if (ranking >= 1) & (ranking <= 100):
        return "First Tier Top Unversity"
    elif (ranking >= 101) & (ranking <= 200):
        return "Second Tier Top Unversity"
    elif (ranking >= 201) & (ranking <= 300):
        return "Third Tier Top Unversity"
    return "Other Top Unversity"

df['Rank_Level']=df["world_rank"].apply(lambda x:create_category(x))
print(df.head())
print(df.pivot_table(index="country",columns='Rank_Level',values="score",aggfunc=[np.mean]))
