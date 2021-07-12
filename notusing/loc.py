import pandas as pd
df=pd.DataFrame(pd.read_csv("biglist.csv", header=None))
df=df.rename(columns={0: "Loc"})
df=df.sort_values('Loc').reset_index(drop=True)
df=df.drop_duplicates(subset=['Loc']).reset_index(drop=True)
for row in df.index:
    print(str(row) + ": " + str(df['Loc'].loc[row]))

print(df)
df.to_csv("sorted.csv")
