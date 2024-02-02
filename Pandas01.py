import pandas as pd
import numpy as np
import re
#Pandas Tutorial i followed is from Keith Galli
def placeholder():
    print()
    print("-----------------------------")
    print()
df = pd.read_csv("pokemon_data.csv")

#df_txt = pd.read_csv("pokemon_data.txt", delimiter="\t") 
#you can load in from excel aswell
print(df.head(3))

placeholder()
print(df.columns)
placeholder()
print(df["Name"][0:5])
placeholder()
print(df[['Name','Type 1','HP']][0:5])

placeholder()

print(df.iloc[1]) # gives back the first row 
print(df.iloc[0:5])
placeholder()
print(df.iloc[2,1]) # the third row and the second column value  (Venusaur)

placeholder()
#print("Iterating through the df")
#for index, row in df.iterrows(): not very good because its generally slow
#    print(index,row)
print(df.loc[df["Type 1"] == "Fire"])

placeholder()
print(df.describe())
placeholder()
print("Sorting")
print(df.sort_values(["Type 1","HP"], ascending=[True,False])) #Type 1 is ascending and the HP is descending

placeholder()
print("New Column")
df["Total"] = df.iloc[:, 4:10].sum(axis=1) #horizontally
print(df.head(5))
placeholder()
print("Drop Columns")
df = df.drop(columns=["Total"])
print(df.head(5))


df["Total"] = df.iloc[:, 4:10].sum(axis=1)


placeholder()
cols = list(df.columns.values)
print("Rearranging columns")
df = df[cols[0:4] + [cols[-1]] + cols[4:12]]
print(df.head(5))

placeholder()

print("Saving our data")
##df.to_csv("modified.csv",index=False)

placeholder()

print("Filtering out data (advanced)")
#print(df.loc[df["Type 1"] == "Fire"])
new_df = df.loc[(df["Type 1"] == "Grass") & (df["Type 2"] == "Poison") & (df["HP"]>70)]
print(new_df) 


placeholder()
print("Reset index")
new_df = new_df.reset_index(drop=True)
new_df.to_csv("modified.csv")

placeholder()
print(new_df.to_numpy())
placeholder()

print(df.loc[df["Type 1"].str.contains("Fire|Grass", regex=True)]) #regex lookup
print(df.loc[df["Name"].str.contains("^pi[a-z]*",flags=re.I,regex=True)]) # where the pi is in the beginning 

placeholder()
print("Conditional Changes")
df.loc[df["Type 1"] == "Fire","Type 1"] = "Flamer" #We change "Fire" type 1 into "Flamer"
#df.loc[df["Type 1"] == "Fire","Legendary"] = True #So where the type1 equals Fire, lets change the legendary column's value to True
print(df)

placeholder()
print("Groupby")
print(df.groupby(["Type 1"]).mean().sort_values("Total",ascending=False))

placeholder()

df["count"] = 1
print(df.groupby(["Type 1"]).count()["count"])



