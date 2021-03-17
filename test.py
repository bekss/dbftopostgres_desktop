import dataset
import psycopg2
import sqlalchemy
import sqlalchemy as sql
from dbfread import DBF
import os
import json


# db = sql.create_engine('postgresql+psycopg2://postgres:admin@localhost/data')
# connect = db.connect()
# if connect:
#     print('succes')
# else:
#     print('dont connected')


# Для подключение MSSQL
def create_psql_conf():
    global config_dir
    config_dir = 'config_sql'  #Имя config файла psql
    config_txt = 'config.txt'
    directory_path = os.getcwd()

    path = os.path.join(directory_path, config_dir)
    print("Текущая деректория:", directory_path)
    if not os.path.isdir(config_dir):
         os.mkdir(config_dir)

    os.chdir(directory_path+f'\\{config_dir}')
    print('Следующая директория' + os.getcwd())

    if not os.path.exists(config_txt):
        text_file = open(config_txt, "w", encoding='utf-8')
        text_file.write('{"username":"postgres", "password":"admin", "host":"host", "database":"data"}')


def read_sql_conf():
    print("После создания txt файла ", os.getcwd())
    print(os.listdir()) #Проверка файла txt

    # os.chdir(a+f'\\{config_dir}')
    with open("config.txt", "r", encoding='utf-8') as f: # Чтобы вытаскывать все данные
        for l in f:
            print(l)
            data = l
            a = json.loads(data)
            print(type(a))
            print(a, '\n', a['username'])

create_psql_conf()
read_sql_conf()

# Для подключение MSSQL
def create_msql_conf():
    global config_dir
    config_txt = 'config_msql.txt'
    directory_path = os.getcwd()

    path = os.path.join(directory_path, config_dir)
    print("Текущая деректория:", directory_path)
    if not os.path.isdir(config_dir):
         os.mkdir(config_dir)

    os.chdir(directory_path+f'\\{config_dir}')
    print('Следующая директория' + os.getcwd())

    if not os.path.exists(config_txt):
        text_file = open(config_txt, "w", encoding='utf-8')
        text_file.write('{"username":"postgres", "password":"admin", "host":"host", "database":"data"}')

# def psql():
#     try:
#         conn = psycopg2.connect("dbname=data user=postgres password=admin")
#         return True
#     except:
#         return False
# print(psql())


# db = dataset.connect(url= 'postgresql://postgres:admi@localhost/data')
# if db:
#     print('succesfully connected')
# else:
#     print('don"t connected')
#
# table = db.create_table('population')
# table = db['popuion']
# for record in DBF('oked.dbf'):
#     table.insert(record)
# {"username":"postgres", "password":"admin", "host":"host", "database":"data"}



#
# def file_path():
#     while True:
#         name_file = input('1) Показать файлы \n'
#                           '2) Выбрать файл \n'
#                           '3) Вернуться в меню \n'
#                           '4) чтобы выйти нажмите любую клавишу \n \n'
#                           ' Введите путь к файлу: \n ')
#
#         if os.path.exists(name_file):
#             print(f'{name_file} указанный файл существует  {name_file} обработан \n')
#         elif name_file == '1':
#             print(os.listdir(), '\n')
#         elif name_file == '3':
#             return file_path()
#         else:
#             print(f"{name_file} файл не существует \n")
#
#
# file_path()








# os.getcwd() показывает текущий путь

# engine = create_engine('postgresql+psycopg2://postgres:admin@localhost/dbf')
# conn = engine.connect()
# if conn:
#     print('sub')
# f = sqlalchemy
# a=f.create_engine("postgresql+psycopg2://postgres:admin@host:5432/dbf")
# if a:
#     print('succesfully connected')
# db = dataset.connect("postgresql+psycopg2://postgres:admin@host:5432/dbf")
# if db:
#     print('sfsf')
# table = db['person']
# table.insert(dict(name='S'))


# db = dataset.connect("postgresql+psycopg2://postgres:admin@/dbf")
# db = create_engine("postgresql+psycopg2://postgres:admin@host:5432/dbf")
# if db is True:
#     print('succesfull')
#
# db.create_table('population')