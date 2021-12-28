import pandas as pd

df = pd.read_csv('C:/Users/viss/OneDrive/Desktop/python/Files/FL_insurance_sample.csv')
print(df.head(15))
print(df.tail(15))
print('To print the columns df.columns')
print(df.columns)
print('Series meaning one only one row or column means it is series in pandas')
print(df['county'])
print("Type of df['county'] is series")
print(type(df['county']))
print('Series act like a list in pandas')
print("To select 20th index df['county'][20] ")
print(df['county'][20])
print("To select starting from index 10  to 20 index df['county'][10:20] ")
print(df['county'][10:20])
print('Selecting multiple columns or rows means it is dataframe in pandas like table sttucture')
print(df[['county','construction']])