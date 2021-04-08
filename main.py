import glob
import json
import os
import tkinter.filedialog as filedialog
from tkinter import *
from tkinter.filedialog import askopenfilename

import dataset
import eel
import psycopg2
import pyodbc
import wx
from dbfread import DBF

_CHOSED_SQL = ' '
_POSTSQL = 'Postgresql'
_MSSQL = 'Mssql'

eel.init('web', allowed_extensions=['.js', '.html'])


def chek_dbf_os(files):
    """This function cheking only files."""
    script_dir = os.path.dirname(__file__)
    for file in os.path.join(script_dir, files):
        if file:
            print('I haved this file')
        print(os.path.join(files, file))


@eel.expose
def pythonFunction(wildcard="*.dbf"):
    """Выбор толкько файла This function choosed only dbf files and giving root path"""
    app = wx.App(None)
    style = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
    dialog = wx.FileDialog(None, 'Open', wildcard=wildcard, style=style)
    if dialog.ShowModal() == wx.ID_OK:
        path = dialog.GetPath()
    else:
        path = None
    dialog.Destroy()
    print(_CHOSED_SQL)
    if _CHOSED_SQL == _MSSQL:
        print('был выбран MSSQL')
        convert_msql_file(path)
    elif _CHOSED_SQL == 'Postgresql':
        print('был выбран POSTGRESQL', path)
        convert_psql_file(path)
    print("Был выбран", _CHOSED_SQL)

    return path


@eel.expose
def get_filepath():
    Tk().withdraw()
    return askopenfilename()


def read_psql_conf():
    """
    Отсюда берется данные для PSQL From hier taking a data for connection SQLs.For example username, password,
    database, host e.t.c
    """
    print(os.listdir())  # Проверка файла txt

    for path in sys.path:
        if os.path.exists(os.path.join(path, 'config/config.txt')):
            print('config.txt файл существует')
            full = path
        else:
            print('Такого файла не существует')
    os.chdir(full + '\\config')

    with open("config.txt", "r", encoding='utf-8') as f:
        for l in f:
            print(l)
            data = l
            a = json.loads(data)
            return a


def read_msql_conf():
    a = os.getcwd()
    print(a)
    print(os.listdir())  # Проверка файла txt

    for path in sys.path:
        if os.path.exists(os.path.join(path, 'config/config_msql.txt')):
            print('config_msql.txt файл существует')
            full = path
        else:
            print('Такого файла не существует')
    print('До перехода', os.getcwd())
    os.chdir(full + '\\config')
    print("Теперь", os.getcwd())

    with open("config_msql.txt", "r", encoding='utf-8') as f:
        for l in f:
            print(l)
            data = l
            a = json.loads(data)
            return a


@eel.expose
def selectFolder():
    """This function read a folders. Giving a permission"""
    print(_CHOSED_SQL)
    print("Here")
    root = Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    directory_path = filedialog.askdirectory()
    if _CHOSED_SQL == _MSSQL:
        print('был выбран MSSQL')
        convert_folder_msql(directory_path)
    elif _CHOSED_SQL == 'Postgresql':
        convert_folder_psql(directory_path)
    return directory_path


def convert_folder_psql(files):
    """First cheking a folder, if in a folder have dbf files then begining to convert"""

    for path in sys.path:
        if os.path.exists(os.path.join(path, 'config/config.txt')):
            print('some_module is heresdf safd asdfsfd : {}'.format(path))
            a = path  # Путь на один каталог назад

    os.chdir(a)
    sql = read_psql_conf()
    db = dataset.connect(
        url=f'postgresql+psycopg2://{sql["username"]}:{sql["password"]}@{sql["host"]}/{sql["database"]}')
    if db:
        print('connected')
    else:
        print('not connected')
    os.chdir(files)
    for file in glob.glob('*.dbf'):
        print(file)
        # if glob.glob('*.dbf') not in os.chdir(files):
        #     print('Вашем файле нету данных')
        name_table = os.path.splitext(file)[0]
        table = db[name_table]
        for record in DBF(file):
            table.insert(record)


def convert_folder_msql(files):
    """First cheking a folder, if in a folder have dbf files then begining to convert"""
    for path in sys.path:
        if os.path.exists(os.path.join(path, 'config/config_msql.txt')):
            print('some_module is heresdf safd asdfsfd : {}'.format(path))
            a = path  # Путь на один каталог назад

    os.chdir(a)
    msql = read_msql_conf()
    db = dataset.connect(
        url=f"mssql+pymssql://{msql['username']}:{msql['password']}@{msql['host']}:{msql['port']}/{msql['database']}")
    if db:
        print('connected')
    else:
        print('not connected')
    os.chdir(files)
    print(os.getcwd())
    for file in glob.glob('*.dbf'):
        name_table = os.path.splitext(file)[0]
        table = db[name_table]
        for record in DBF(file):
            table.insert(record)


def convert_psql_file(dbf_path):
    """Function for converting only file."""
    sql = read_psql_conf()
    db = dataset.connect(
        url=f'postgresql+psycopg2://{sql["username"]}:{sql["password"]}@{sql["host"]}/{sql["database"]}')
    if db:
        print('connected')
    else:
        print('not connected')
    print(dbf_path)
    dbf_path1 = os.path.basename(dbf_path)
    print(dbf_path1)
    dbf_path_second = os.path.basename(dbf_path)
    name_table = os.path.splitext(dbf_path_second)[0]
    table = db[name_table]
    for record in DBF(dbf_path):
        table.insert(record)


def convert_msql_file(dbf_path):
    """This funcfion converting a file to MSSQL"""
    msql = read_msql_conf()
    db = dataset.connect(
        url=f"mssql+pymssql://{msql['username']}:{msql['password']}@{msql['host']}:{msql['port']}/{msql['database']}")
    if db:
        print('connected')
    else:
        print('not connected')
    dbf_path_second = os.path.basename(dbf_path)
    name_table = os.path.splitext(dbf_path_second)[0]
    print('name table', name_table)
    table = db[name_table]
    for record in DBF(dbf_path):
        table.insert(record)


@eel.expose
def data_psql(username, password, host, database):
    """Connection to Postgresql database from inputs in first version"""
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


# def chek_mssql_table_name(name):
#     msql = read_msql_conf()
#     try:
#         print(msql)
#         user = msql['username']
#         pas = msql['password']
#         data = msql['database']
#         host = msql['host']
#         conn = pyodbc.connect("DRIVER={SQL Server};SERVER=%s;DATABASE=%s;UID=%s;PWD=%s" % (host, data, user, pas))
#         if conn:
#             print('connected')
#             cursor = conn.cursor()
#             cursor.execute(f"SELECT * FROM information_schema.tables WHERE table_name = '{name}'")
#             row = cursor.fetchone()
#             while row:
#                 print("ID=%s" % (row[0]))
#                 row = cursor.fetchone()
#                 print(row)
#

@eel.expose
def psql_conn():
    """PSQL connection check"""
    global _CHOSED_SQL
    global _POSTSQL
    try:
        conf_sql = read_psql_conf()
        conn = psycopg2.connect(
            f"dbname={conf_sql['database']} user={conf_sql['username']} password={conf_sql['password']} host={conf_sql['host']}")
        print('Подключено к PSQL')
        _CHOSED_SQL = _POSTSQL
        print(_CHOSED_SQL)
        eel.reverse_info('True', 'PSQL')
        conn.close()
        if conn.close():
            print('база closed')
        return True
    except:
        print('Не подключено к PSQL')
        eel.reverse_info('False')
        return False


@eel.expose
def msql_conn():
    """Connecting to MSSQL and checking a user"""
    global _CHOSED_SQL
    global _MSSQL
    msql = read_msql_conf()
    try:
        print(msql)
        user = msql['username']
        pas = msql['password']
        data = msql['database']
        host = msql['host']
        # sqldriver = msql['sqldriver']
        _CHOSED_SQL = _MSSQL
        print(_CHOSED_SQL)
        # print(pas)
        # conn = pymssql.connect(f"dbname={msql['database']} user={msql['username']} password={msql['password']} host={msql['host']} port={msql['port']}")
        # conn = pymssql.connect(f"user={msql['username']}, password={msql['password']} , database={msql['database']}")
        # conn = pymssql.connect(user="beksultan", password= "beksultan", database ="data")
        # conn = pymssql.connect(user='beksultan', password='beksultan', database='data')
        conn = pyodbc.connect("DRIVER={SQL Server};SERVER=%s;DATABASE=%s;UID=%s;PWD=%s" % (host, data, user, pas))
        if conn:
            print('connected')

        print('Подключено к MSQL')
        eel.reverse_info('True', 'MSQL')
        conn.close()
        return True
    except:
        print('Не подключено к MSQL')
        eel.reverse_info('False')
        return False


@eel.expose
def load_program():
    """This a testing function transmit a data from python to javascript/ for first test"""
    return eel.setLoading('done with')


@eel.expose
def chosed_files():
    """Selects a folder"""
    return eel.name_file(selectFolder())


@eel.expose
def chosed_file():
    """Selects a file"""
    return eel.set_file(pythonFunction())


@eel.expose
def folder_return():
    name = 'Folder for dbf'
    print(name)
    return name


@eel.expose
def psql_con(data):
    print('psql принял', data)


eel.start('main.html', port=4000 )

# def sql_connect(user=None, password=None, port=None, database=None):
#     db = dataset.connect(url="postgresql+psycopg2://{}.:{}.@{}./{}.".format('postgres', 'admin', 'localhost', 'data'))
#     if db:
#         print('connected')
#     else:
#         print('not connected')

# sql_connect()

# def get_one_file(files):
#     script_dir = os.path.dirname(__file__)
#     file_path = os.path.join(script_dir, files)
#     for file in os.path.join(script_dir, files):
#         print(os.path.join(file_path, file))
# with open(file_path, 'r') as fi:
#     print(file_path)

# IF EXISTS (SELECT 1
#            FROM INFORMATION_SCHEMA.TABLES
#            WHERE TABLE_TYPE='BASE TABLE'
#            AND TABLE_NAME='stest1.dbf')
#    SELECT 1 AS res ELSE SELECT 0 AS res;
