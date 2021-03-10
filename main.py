# import eel
# from jinja2 import DictLoader, Template
#
# # template = Template('main.html')
# # a = template.render()
#
# # @eel.expose
# # def get_files(a):
# #     print(a)
#
# @eel.expose
# def say_hello_py(x):
#     print('work in  %s' % x)
#
#
# def start():
#     eel.init('web', allowed_extensions=['.js','.html'])
#     eel.start('main.html')
#
# start()
#
# # @eel.expose
# # def hello():
# #     print('hello')
# #     print(3+1)

import eel
import wx
import tkinter.filedialog as filedialog
import glob, os
import dataset
import sqlalchemy
import psycopg2

from dbfread import DBF
from tkinter import *
from tkinter.filedialog import askopenfilename


eel.init('web', allowed_extensions=['.js', '.html'])



"""Проверяет только файл"""
def chek_dbf_os(files):
    script_dir = os.path.dirname(__file__)
    for file in os.path.join(script_dir, files):
        if file:
            print('I haved this file')
        print(os.path.join(files, file))


"""Выбор толкько файла"""
@eel.expose
def pythonFunction(wildcard="*.dbf"):
    app = wx.App(None)
    style = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
    dialog = wx.FileDialog(None, 'Open', wildcard=wildcard, style=style)
    if dialog.ShowModal() == wx.ID_OK:
        path = dialog.GetPath()
    else:
        path = None
    dialog.Destroy()
    # get_one_file(path)
    # chek_dbf_os(path)
    convert_to_psql_file(path)
    # print(path)
    return path


@eel.expose
def get_filepath():
    Tk().withdraw()
    return askopenfilename()

"""Для чтения папки"""
@eel.expose
def selectFolder():
    print("Here")
    root = Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    directory_path = filedialog.askdirectory()
    chek_dbf_folder(directory_path)
    print(directory_path)
    return directory_path


"""Проверяет только папку, если есть в папке dbf файл то да"""
def chek_dbf_folder(files):
    db = dataset.connect(url='postgresql+psycopg2://postgres:admin@localhost/data')
    if db:
        print('connected')
    else:
        print('not connected')
    os.chdir(files)
    for file in glob.glob('*.dbf'):
        print(file)
        # if glob.glob('*.dbf') not in os.chdir(files):
        #     print('Вашем файле нету данных')

        # db = dataset.connect(url=f"postgresql+psycopg2://{}.:{}.@{}./{}.".format('postgres', 'beka', 'localhost', 'data'))

        # file_dbf = open("D:\\myfiles\welcome.txt", "r")
        # print(file_dbf.read())
        table = db.create_table(file)
        table = db[file]
        for record in DBF(file):
            table.insert(record)
        # return file



"""Только для файла"""
def convert_to_psql_file(dbf_path):
    # db = dataset.connect(url=f"postgresql+psycopg2://{}.:{}.@{}./{}.".format('postgres', 'beka', 'localhost', 'data'))
    db = dataset.connect(url='postgresql+psycopg2://postgres:admin@localhost/data')
    if db:
        print('connected')
    else:
        print('not connected')
    print(dbf_path)
    dbf_path1 = os.path.basename(dbf_path)
    print(dbf_path1)

    # file_dbf = open("D:\\myfiles\welcome.txt", "r")
    # print(file_dbf.read())
    table = db.create_table(dbf_path1)
    table = db[dbf_path1]
    for record in DBF(dbf_path):
        table.insert(record)




"""Подключение к базе данных Postgresql"""
@eel.expose
def data_psql(username, password, host, database):
    # if username is None:
    #     print('пожалуйста заполните поля')
    try:
        conn = psycopg2.connect(f"dbname={database} user={username} password={password} host={host}")
        print('Подключено к PSQL')
        print(f' имя: {username} \n пароль: {password} \n хост: {host} \n база данных: {database}')
        eel.reverse_info('True')
        return True
    except:
        print('Не подключено к PSQL')
        eel.reverse_info('False')
        return False


def config_psql():
    pass



"""Это функция передает данные из python в javascript"""
@eel.expose
def load_program():
    return eel.setLoading('done with')


"""Выбирает папку"""
@eel.expose
def chosed_files():
    return eel.name_file(selectFolder())


"""Выбирает файл"""
@eel.expose
def chosed_file():
    return eel.set_file(pythonFunction())


@eel.expose
def folder_return():
    name = 'Folder for dbf'
    print(name)
    return name


# def sql_connect(user=None, password=None, port=None, database=None):
#     db = dataset.connect(url="postgresql+psycopg2://{}.:{}.@{}./{}.".format('postgres', 'admin', 'localhost', 'data'))
#     if db:
#         print('connected')
#     else:
#         print('not connected')

# sql_connect()
eel.start('main.html')




# def get_one_file(files):
#     script_dir = os.path.dirname(__file__)
#     file_path = os.path.join(script_dir, files)
#     for file in os.path.join(script_dir, files):
#         print(os.path.join(file_path, file))
    # with open(file_path, 'r') as fi:
    #     print(file_path)

