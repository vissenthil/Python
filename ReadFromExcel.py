import pandas as pd
import xlwt
from pandas_profiling import ProfileReport
df = pd.read_excel('C:/Users/viss/OneDrive/Desktop/python/Files/Data Refresh Sample Data.xlsx')
print(df.head())
print('To read different Sheet')
df1 = pd.read_excel('C:/Users/viss/OneDrive/Desktop/python/Files/Data Refresh Sample Data.xlsx',sheet_name='DeptData')
print(df1.head(10))
column = df1.columns
print('Print columns',column)
print('Read csv from github Link')
dfgithub = pd.read_csv('https://raw.githubusercontent.com/codeforamerica/ohana-api/master/data/sample-csv/addresses.csv')
print(dfgithub.head(13))
print('Read from HTLM page')
dfhtml = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2022_games-november.html')
print(dfhtml) #stores like a list
print(dfhtml[0].head(20))
#dfhtml[0].to_excel('C:/Users/viss/OneDrive/Desktop/python/Files/test1.xlsx')
print(dfhtml[0].columns)
print(dfhtml[0]['Home/Neutral'])
print(dfhtml[0][['Home/Neutral','Start (ET)']])
print('Data thpe of each column')
print(dfhtml[0].dtypes)
print('Object data type means string in python')
print(dfhtml[0].info())
Rep = ProfileReport(dfhtml[0])
print(Rep)