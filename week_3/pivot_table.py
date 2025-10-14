df=pd.read_csv(r"C:\Users\THINKPAD\Downloads\cwurData.csv")
print(df.head())

def create_category(ranking):
    if (ranking >= 1) & (ranking <= 100):
        return "First Tier Top University"
    elif (ranking >= 101) & (ranking <= 200):
        return "Second Tier Top University"
    elif (ranking >= 201) & (ranking <= 300):
        return "Third Tier Top University"
    return "Other Top University"

df['Rank_Level']=df["world_rank"].apply(lambda x:create_category(x))
print(df.head())
p1=df.pivot_table(index="country",columns='Rank_Level',values="score",aggfunc=[np.mean])
print(p1)
p2=df.pivot_table(index="country",columns="Rank_Level",values="score",aggfunc=[np.mean,np.max])
print(p2)
new_df=df.pivot_table(index="country",columns="Rank_Level",values="score",aggfunc=[np.mean,np.max],margins=True)
print(new_df)
print(new_df.index)
print(new_df.columns)
p3=new_df["mean"]["First Tier Top University"]
print(p3)
print(type(p3))
p4=new_df["mean"]["First Tier Top University"].idxmax()
print(p4)
stack=new_df.stack()
print(stack)
unstack=new_df.unstack().unstack()
print(unstack)
