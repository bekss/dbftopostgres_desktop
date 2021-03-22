import os
import dataset
from dbfread import DBF
import pyodbc
import pymssql


""""Для проверки юзера использутеся этот код"""
# conn = pymssql.connect(user="beksultan", password="beksultan", database="data")
#
# if conn:
#     print('connected')
# else:
#     print('not connected')
# cursor = conn.cursor()
# cursor.execute('SELECT * FROM people')
# row = cursor.fetchone()
# while row:
#     print("ID=%s" % (row[0]))
#     row = cursor.fetchone()


# conn = pyodbc.connect('Driver={SQL Server};'
#                       'Server=DESKTOP-OG81R5M\SQLEXPRESS;'
#                       'Database=data;'
#                       'Trusted_Connection=yes;')
# cursor = conn.cursor()
# cursor.execute('SELECT * FROM data.dbo.people')
#
# for row in cursor:
#     print(row)



db = dataset.connect(url='mssql+pymssql://beksultan:beksultan@localhost:1433/data')

if db:
    print('connected')
else:
    print('not connected')

path = 'oked4.dbf'
table = db.create_table('df')
table = db[path]
for record in DBF(path):
    table.insert(record)

# dataset.connect(url=f"postgresql+psycopg2://{}.:{}.@{}./{}.".format('postgres', 'beka', 'localhost', 'data'))



# db = dataset.connect('sqlite:///data.db')
# if db:
#     print('connected')
# else:
#     print('not connected')
#
#
# path = 'oked4.dbf'
# table = db.create_table('dbf')
# table = db[path]
# for record in DBF(path):
#     table.insert(record)

# a = os.getcwd()
#
#
# print(a)
# if os.path.exists(a+'\\config\\'):
#     print('Существует')
# else:
#     print('Не существует')
#
# os.chdir(os.getcwd()+'\\config\\')
# print(os.getcwd())
#
