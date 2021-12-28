import csv

import mysql.connector as conn
import pandas as pd
mydb = conn.connect(host='localhost',user='root',password='vissmysql@#75')
myquery = 'show databases'
mycursor = mydb.cursor()
mycursor.execute(myquery)
'''myquery1 ='create database pymysql'
mycursor.execute(myquery1)
mycursor.execute(myquery)'''
#print(mycursor.fetchall())
print('Ok')
#createTableQuery = 'create table pymysql.studentInof(Studid int, stud_name varchar(100),age int, sex varchar2(1),course_name varchar(100))'
#mycursor.execute(createTableQuery)
#showTable = 'show tables'
#mycursor.execute(showTable)
print(mycursor.fetchall())
mycursor.execute('Drop table pymysql.studentInfo1')
mycursor.execute('Drop table pymysql.glass')
createTableQuery = 'create table pymysql.studentInfo1' \
                   '(Studid int, ' \
                   'stud_name varchar(100),' \
                   'age int, ' \
                   'sex varchar(1),' \
                   'course_name varchar(100))'
mycursor.execute(createTableQuery)
for i in range(10):
    insertQuery = 'insert into pymysql.studentInfo1 values(1,"Senthilkumar",46,"M","PYTHON");'
    mycursor.execute(insertQuery)
mydb.commit();
mycursor.execute('SELECT * FROM pymysql.studentInfo1;')
print(mycursor.fetchall())
#To close a connection
print('Read using Pandas connection ')
readedData = pd.read_sql('SELECT * FROM pymysql.studentInfo1;',mydb)
print(readedData)

CreateTableQuer = 'create table pymysql.glass(RI float(10,5),	' \
                  'Na float(10,5),	' \
                  'Mg float(10,5),	' \
                  'Al float(10,5),	' \
                  'Si float(10,5),	' \
                  'K float(10,5),	' \
                  'Ca float(10,5),	' \
                  'Ba float(10,5),	' \
                  'Fe float(10,5));'
mycursor.execute(CreateTableQuer)
with open('C:/Users/viss/OneDrive/Desktop/python/Files/glass_csv.csv','r') as f:
    glass_data = csv.reader(f,delimiter = '\n')
    for lines in enumerate(glass_data):
        for list_ in (lines[1]):
            #print(list_)
            mycursor.execute('insert into pymysql.glass values ({a})'.format(a = list_))
mydb.commit()
print('Extract data from mysql using pandas.read_sql')
print(pd.read_sql('SELECT * FROM pymysql.glass',mydb))
print('Using Select statement')
#print(mycursor.execute('select * from pymysql.glass where Mg = 3.49000'))
mycursor.execute('delete from pymysql.glass where Mg = 3.49000')
mydb.commit()
print('Select statement after delete')
#print(mycursor.execute('select * from pymysql.glass where Ca = 8.77000'))
print(pd.read_sql('SELECT * FROM pymysql.glass where Ca = 8.77',mydb))
mycursor.execute('update pymysql.glass '
                 'set Ca = 9.90 '
                 'where Ca = 8.77')
mydb.commit()
print('Select statement after update')
print(pd.read_sql('SELECT * FROM pymysql.glass where Ca = 9.90',mydb))
