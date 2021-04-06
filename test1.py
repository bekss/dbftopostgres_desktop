import os
import dataset
from dbfread import DBF
import pyodbc
import pymssql

# 'Driver = {ODBC Driver 13 for SQL Server}; Server = NameServer; uid = sa; pwd = '
#                             'myPassword; Database = BaseName
# DRIVER={SQL Server};SERVER=localhost;DATABASE=testdb;UID=user;PWD=password
conn = pyodbc.connect("DRIVER={SQL Server};SERVER=212.42.101.123;DATABASE=StructureService;UID=importeruser;PWD=vNe7NT")

# # row = cursor.fetchone()
# # print(row)
# if conn:
#     print('connected')
#     cursor = conn.cursor()
#     cursor.execute("select *from GKUD6151065_Dsd9_Year2020_Dynamic")
#     row = cursor.fetchone()
#     print(row)
#
# else:
#     print('NOt connect')

# pyodbc.connect('DSN=DataSourceName;UID=user;PWD=password')




""""Для проверки юзера использутеся этот код"""
# conn = pymssql.connect( user="beksultan", password="beksultan", database="data")
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


#
db = dataset.connect(url='mssql+pymssql://beksultan:beksultan@127.0.0.1:1433/data')
print('connected')
cursor = conn.cursor()
cursor.execute("SELECT * FROM information_schema.tables WHERE table_name = 'stest.dbf'")
row = cursor.fetchone()
print(row)
if row is None:
    print('Noneee')
else:
    print('haveed')
# while row:
#     print("ID=%s" % (row[0]))
#     row = cursor.fetchone()
#     print(row)

#
# if db:
#     print('connected')
# else:
#     print('not connected')
# path = 'tab1.dbf'
# # table = db.create_table('testingdata')
# table = db['testingdata']
# for record in DBF(path):
#     table.insert(record)
#     print(record)

# dataset.connect(url=f"postgresql+psycopg2://{}.:{}.@{}./{}.".format('postgres', 'beka', 'localhost', 'data')) PROGER-\SQLEXPRESS



# db = dataset.connect('sqlite:///data.db')
# if db:
#     print('connected')
# else:
#     print('not connected')
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
