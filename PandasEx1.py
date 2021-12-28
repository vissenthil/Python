import pandas as pd

df = pd.read_csv('C:/Users/viss/OneDrive/Desktop/python/Files/grades.csv')
print(df)
print('To Know the data type use dataframename.dtypes as below')
print(df.dtypes)
print('To know the columns list use df.columns as below')
print(df.columns)
print('Example of iloc display based on index here startindex:endindex df.iloc[0:3]')
print(df.iloc[0:3])
print("Example of loc display based on labels here df.loc('First name']")
print(df['Last name'] == 'Alfalfa')
