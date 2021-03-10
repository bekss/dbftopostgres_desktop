from dbfread import DBF
import os
import psycopg2
from collections import namedtuple

import dataset
import sys
from dbfread import DBF

# def show(*words):
#     print('  ' + ' '.join(str(word) for word in words))
#
# def show_field(field):
#     print('    {} ({} {})'.format(field.name, field.type, field.length))

# def main():
#     for filename in sys.argv[1:]:
#         print(filename + ':')
#         table = DBF(filename, ignore_missing_memofile=True)
#         show('Name:', table.name)
#         show('Memo File:', table.memofilename or '')
#         show('DB Version:', table.dbversion)
#         show('Records:', len(table))
#         show('Deleted Records:', len(table.deleted))
#         show('Last Updated:', table.date)
#         show('Character Encoding:', table.encoding)
#         show('Fields:')
#         for field in table.fields:
#             show_field(field)
# main()

# def dbf_file(path):
#     type_file, extension = os.path.splitext(path)
#     # try:
#         # decod_file = path
#         # print(decod_file)
#
#
#     table = DBF(path,load=True)
#     name_column = list(table.records[0])             #Здесь мы получаем в List python
#     name = list(name_column)
#     print(len(name))
#     for new_name in range(len(name)):
#         print(name[new_name])                         #Имена столбцов


    # for record in DBF(path,  load=True):
    #     print(list(record)[2])
        # print(list(record)[2])                    #Получаем имена столбцов
        # done_file = dict(record)                    #Получаем в словаре наши данные
        # print(done_file.get('KOD'))

    #     if not path:
    #         raise Exception(f'Файл пустой ')
    #     if extension != '.dbf':
    #         raise Exception(f'Файл не правльного формата {path}')
    # except IOError as e:
    #     raise Exception("Файл не правильного формата файл")
# dbf_file('oked.dbf')





# def connect_to_pg():
#     global con
#     con = psycopg2.connect(
#         database='dbf',
#         user='postgres',
#         password='admin',
#         host='127.0.0.1',
#         port='5432'
#     )
#     if con:
#         print('Succesfully connected')
#
#
# def create_name_tables():
#     global con
#     cur = con.cursor()
#     cur.execute('''CREATE TABLE STUDENT''')


