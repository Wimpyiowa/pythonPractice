import pandas as pd

#Loading Data into Pandas

df= pd.read_csv('pokemon_data.csv')

df_xlsx = pd.read_excel('pokemon_data.xlsx')

dftxt = pd.read_csv('pokemon_data.txt', delimiter = '\t')

print(df.head(5)) #Top data
print(df.tail(5)) #Bottom data

print(df_xlsx.head(3))

print(dftxt.head(20))

#Reading Data in Pandas
print(df.columns[0:5])

## Read each Column
print(df[['Name', 'Type 1', 'HP'][0:10]])
#for index, row in df.iterrows(): 
    #print(index, row['Name'])
df.loc[df["Type 1"] == "Fire"]

## Read each Row
print(df.iloc[1:4])

## Read a specific location (R,C)
print(df.iloc[2,1])

#Sorting/Describing Data
print(df.describe())
print(df.sort_values(['Type 1', 'HP'], ascending=[1,0])) #Will be sorting Type 1 from A-Z, while the HP goes from highest to lowest.


#Making changes to the data
print(df.head(5))
df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
print(df.head(5))

print(45+49+49+65+65+45)

df = df.drop(columns=['Total']) #Dropping the column
print(df.head(5))

df['Total'] = df.iloc[:, 4:10].sum(axis=1)

cols = list(df.columns.values)
df = df[cols[0:4] + [cols[-1]]+cols[4:12]]

print(df.head(5))

#Saving our Data (Exporting into Desired Format)
df.to_csv('modified.csv', index=False)

df.to_excel('modified.xlsx', index=False)

df.to_csv('modified.txt', index=False, sep='\t')

#Filtering Data
new_df = (df.loc[(df['Type 1'] == "Grass") & (df['Type 2'] == "Poison") & (df['HP'] > 70)]) #And (&)
print(new_df)
print(df.loc[(df['Type 1'] == "Grass") | (df['Type 2'] == "Poison")]) #Or (|)

new_df = new_df.reset_index(drop = True) #Do this to avoid index errors. (Incorrect values)
#Drop = True will remove old index before a change has been made. 
new_df.to_csv('filtered.csv')



print(df.loc[df['Name'].str.contains('Mega')])
print(df.loc[~df['Name'].str.contains('Mega')]) #Drops all names with "Mega"

import re #Regular Expressions
print(df.loc[df['Type 1'].str.contains('Fire|Grass', regex=True)]) #Fire or grass
#To ignore capitals, use flags=re.I after calling contained values.

print(df.loc[df['Name'].str.contains('^pi[a-z]*', flags=re.I, regex=True)]) #^ means start of line and * means zero or more.

#Conditional Changes
df.loc[df['Type 1'] == 'Fire', 'Type 1'] = "Flame" #Will change the data frame
print(df)

df.to_csv('dataFire.csv') #This is just for checking.

df = pd.read_csv('modified.csv') #Treating the modified version as a checkpoint
print(df)

df.loc[df['Total'] > 500, ['Generation', 'Lengendary']] = ['Test 1', 'Test 2']
print(df)
df = pd.read_csv('modified.csv')

#Aggregate Statistics (Groupby)
df = df.drop(columns=['Name'])
print(df.groupby(['Type 1']).mean().sort_values('Defense', ascending=False)) #Searchs for the mean values of type 1 pokemon
#Then, it is sorted by highest defense. We used ascending False to grab the highest average of defense.
#In this case, class type "Steel" has the highest defense on average.
