import pandas as pd
import re
df = pd.read_csv('C:/Users/viss/OneDrive/Desktop/python/Files/Pokemon.csv')
print(df.head(20))
# Read each row
#print(df.iloc[0:4])here from row 0 to row 4 not including row 4
print(df.iloc[0:4]) # This is for index location based on numbers
for index,row in df.iterrows():
    print(index,row)
print('Only display the names ')
for index,row in df.iterrows():
    print(index,row['Name'])
# To filter only the Type 1 = Fire loc is search based on text
print(df.loc[df["Type 1"]=='Fire'])

print(df['Attack']>80)
# Read a specific location (R,C)
print(df.iloc[2,10])
print('Sorting and describing')
print(df.describe())
print('Sort the data based on Name by default asceding ')
print(df.sort_values('Name'))
print('Sort the data based on Name by  dsceding ')
print(df.sort_values('Name',ascending=False))
print(df.sort_values(['Name','HP'],ascending=True))
print(df.sort_values(['Name','HP'],ascending=False))
print("Based on Multiple column values 1 is for aceding and 0 is for decending")
print(df.sort_values(['Name','HP','Speed'],ascending=[1,0,1]))
print('Making changes to the Data')
df['Total'] = df['HP'] + df['Attack'] + df['Defense']
print(df['Total'])
print('Droping a colum or multiple column form the dataframe')
#df = df.drop(columns=['HP','Type 2'])
#print(df[['Name','HP']])
df['TotalValues'] = df.iloc[:,4:10].sum(axis=1) #Creating a new column axis = 1 rowwise 0 columwise total
print('Total values:',df['TotalValues'])
cols = list(df.columns)
print(cols)
print('Rearrenching the columns in the dataframe')
df = df[cols[0:4] + [cols[-1]] + cols[4:12]]
print(df)
df.to_excel('C:/Users/viss/OneDrive/Desktop/python/Files/modified.xlsx')
print('To remove the index use index=False')
df.to_excel('C:/Users/viss/OneDrive/Desktop/python/Files/modifiedNoIndex.xlsx',index=False)
df.to_csv('C:/Users/viss/OneDrive/Desktop/python/Files/modifiedNoIndex.txt',index=False,sep='\t') # seperated by tab
print('Filtering data ')
df1 = df.loc[(df['Type 2'] == 'Poison') & (df['Name'] == 'Venusaur')]
print(df1)
df2 = df.loc[(df['Type 2'] == 'Poison') & (df['Attack'] > 80)]
print(df2[['Type 2','Attack']])
print(df.loc[df['Name'].str.contains('Mega')])
print('Use ~ symbol to not include the name contains Mega like not in in oracle')
print(df.loc[~df['Name'].str.contains('Mega')])
#print(df.loc[df['Type 1'].str.contains('Grass|Fire',regex=True)])

print(df.loc[df['Type 1'].str.contains('Grass|Fire')])
print('Case insentive meaning if it is lowercase or upper case no issue use flags=re.I')
print(df.loc[df['Type 1'].str.contains('Grass|fire',flags=re.I)])
print('Name start with only pi to display "^pi[a:z]*" here * means zero or more characters')
print(df.loc[df['Name'].str.contains('^pi[a:z]*',flags=re.I)])
#Condition changes
df.loc[df['Type 1'] == 'Fire','Type 1'] ='Flamer'
print('Type 1 value Fire is now change to Flamer',df['Type 1'])
df.loc[df['TotalValues'] > 200,'Legendary'] = True
print(df[['TotalValues','Legendary']])
df.loc[df['TotalValues'] > 200,['Legendary','Generation']] = ['Test1','Test2']
print(df[['TotalValues','Legendary','Generation']])
print('How to use Group by "df.groupby(["Type 1"]).mean()" ')
print(df.groupby(['Type 1']).mean().sort_values('TotalValues',ascending=False))
df['count'] = 1
print(df.groupby(['Type 1','Type 2']).count()['count'])