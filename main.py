import eel
import wx
import tkinter.filedialog as filedialog
import glob, os
import dataset
import psycopg2
import json
import pymssql
import pyodbc

from dbfread import DBF
from tkinter import *
from tkinter.filedialog import askopenfilename

eel.init('web', allowed_extensions=['.js', '.html'])


_CHOSED_SQL = ' '
_POSTSQL = 'Postgresql'
_MSSQL = 'Mssql'

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
    # print(_CHOSED_SQL)
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
    # convert_psql_file(path)
    if _CHOSED_SQL == _MSSQL:
        print('был выбран MSSQL')
        convert_msql_file(path)
    elif _CHOSED_SQL == 'Postgresql':
        print('был выбран POSTGRESQL', path)
        convert_psql_file(path)
    print("Был выбран", _CHOSED_SQL)
    print(path)
    return path


@eel.expose
def get_filepath():
    Tk().withdraw()
    return askopenfilename()


"""Отсюда берется данные для PSQL"""
def read_psql_conf():
    global config_dir
    a = os.getcwd()
    print(a)
    # print("После создания txt файла ", os.getcwd())
    print(os.listdir())  # Проверка файла txt

    for path in sys.path:
        if os.path.exists(os.path.join(path, 'config/config.txt')):
            print('config.txt файл существует')
            full = path
        else:
            print('Такого файла не существует')

    # if os.path.exists(path+'\\config\\config.txt'):
    #     print('config.txt файл существует')
    # else:
    #     print('Такого файла не существует')
    print('До перехода', os.getcwd())
    # if os.getcwd() == a:
    os.chdir(full + '\\config')
    print("Теперь", os.getcwd())

    with open("config.txt", "r", encoding='utf-8') as f:
        for l in f:
            print(l)
            data = l
            a = json.loads(data)
            # print(type(a))
            # print(a, '\n', a['username'])
            return a


def read_msql_conf():
    a = os.getcwd()
    print(a)
    # print("После создания txt файла ", os.getcwd())
    print(os.listdir())  # Проверка файла txt

    for path in sys.path:
        if os.path.exists(os.path.join(path, 'config/config_msql.txt')):
            print('config_msql.txt файл существует')
            full = path
        else:
            print('Такого файла не существует')

    # if os.path.exists(path+'\\config\\config.txt'):
    #     print('config.txt файл существует')
    # else:
    #     print('Такого файла не существует')
    print('До перехода', os.getcwd())
    # if os.getcwd() == a:
    os.chdir(full + '\\config')
    print("Теперь", os.getcwd())

    with open("config_msql.txt", "r", encoding='utf-8') as f:
        for l in f:
            print(l)
            data = l
            a = json.loads(data)
            # print(type(a))
            # print(a, '\n', a['username'])
            return a


"""Для чтения папки"""
@eel.expose
def selectFolder():
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
        print('был выбран POSTGRESQL', directory_path)
        convert_folder_psql(directory_path)
    print("Был выбран",_CHOSED_SQL)
    # convert_folder_psql(directory_path)
    print(directory_path)
    return directory_path


"""Проверяет только папку, если есть в папке dbf файл то да"""
def convert_folder_psql(files):
    print("Это файл", files)
    print("С перва я здесь ", os.getcwd())
    for path in sys.path:
        if os.path.exists(os.path.join(path, 'config/config.txt')):
            print('some_module is heresdf safd asdfsfd : {}'.format(path))
            a = path  # Путь на один каталог назад

    print('desktop бул', a)
    os.chdir(a)
    print("я здесь ", os.getcwd())
    sql = read_psql_conf()
    print(sql['username'])
    db = dataset.connect(
        url=f'postgresql+psycopg2://{sql["username"]}:{sql["password"]}@{sql["host"]}/{sql["database"]}')
    if db:
        print('connected')
    else:
        print('not connected')
    os.chdir(files)
    print(os.getcwd())
    for file in glob.glob('*.dbf'):
        print(file)
        # if glob.glob('*.dbf') not in os.chdir(files):
        #     print('Вашем файле нету данных')
        table = db.create_table(file)
        table = db[file]
        for record in DBF(file):
            table.insert(record)


"""Проверяет только папку, если есть в папке dbf файл то да"""
def convert_folder_msql(files):
    print("Это файл", files)
    print("С перва я здесь ", os.getcwd())
    for path in sys.path:
        if os.path.exists(os.path.join(path, 'config/config_msql.txt')):
            print('some_module is heresdf safd asdfsfd : {}'.format(path))
            a = path  # Путь на один каталог назад

    print('desktop бул', a)
    os.chdir(a)
    print("я здесь ", os.getcwd())
    msql = read_msql_conf()
    print(msql['username'])
    db = dataset.connect(
        url=f"mssql+pymssql://{msql['username']}:{msql['password']}@{msql['host']}:{msql['port']}/{msql['database']}")
    if db:
        print('connected')
    else:
        print('not connected')
    os.chdir(files)
    print(os.getcwd())
    for file in glob.glob('*.dbf'):
        print(file)
        # if glob.glob('*.dbf') not in os.chdir(files):
        #     print('Вашем файле нету данных')
        table = db.create_table(file)
        table = db[file]
        for record in DBF(file):
            table.insert(record)



"""Только для файла"""
def convert_psql_file(dbf_path):
    print( "Получил",dbf_path)
    sql = read_psql_conf()
    print(sql['username'])
    # db = dataset.connect(url=f"postgresql+psycopg2://{}.:{}.@{}./{}.".format('postgres', 'beka', 'localhost', 'data'))
    db = dataset.connect(
        url=f'postgresql+psycopg2://{sql["username"]}:{sql["password"]}@{sql["host"]}/{sql["database"]}')
    if db:
        print('connected')
    else:
        print('not connected')
    print(dbf_path)
    dbf_path1 = os.path.basename(dbf_path)
    print(dbf_path1)

    table = db.create_table(dbf_path1)
    table = db[dbf_path1]
    for record in DBF(dbf_path):
        table.insert(record)


def convert_msql_file(dbf_path):
    print(dbf_path)
    msql = read_msql_conf()
    print(msql['username'])
    user = msql['username']
    pas = msql['password']
    data = msql['database']
    # db = dataset.connect(url=f"postgresql+psycopg2://{}.:{}.@{}./{}.".format('postgres', 'beka', 'localhost', 'data'))


    db = dataset.connect(url=f"mssql+pymssql://{msql['username']}:{msql['password']}@{msql['host']}:{msql['port']}/{msql['database']}")
    if db:
        print('connected')
    else:
        print('not connected')
    print(dbf_path)
    dbf_path1 = os.path.basename(dbf_path)
    print(dbf_path1)

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


@eel.expose
def psql_conn():
    global _CHOSED_SQL
    global _POSTSQL
    try:
        conf_sql = read_psql_conf()
        conn = psycopg2.connect(
            f"dbname={conf_sql['database']} user={conf_sql['username']} password={conf_sql['password']} host={conf_sql['host']}")
        print('Подключено к PSQL')
        _CHOSED_SQL = _POSTSQL
        print(_CHOSED_SQL)
        eel.reverse_info('True')
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
    global _CHOSED_SQL
    global _MSSQL
    try:
        msql = read_msql_conf()
        user = msql['username']
        pas = msql['password']
        data = msql['database']
        _CHOSED_SQL = _MSSQL
        print(_CHOSED_SQL)
        print(pas)
        # conn = pymssql.connect(f"dbname={msql['database']} user={msql['username']} password={msql['password']} host={msql['host']} port={msql['port']}")
        # conn = pymssql.connect(f"user={msql['username']}, password={msql['password']} , database={msql['database']}")
        # conn = pymssql.connect(user="beksultan", password= "beksultan", database ="data")
        conn = pymssql.connect(user='beksultan', password='beksultan', database='data')
        if conn:
            print('connected')
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM people')
            row = cursor.fetchone()
            while row:
                print("ID=%s" % (row[0]))
                row = cursor.fetchone()

        # else:
        #     print('not connected')
        #     eel.reverse_info('False')
        #     return False
        # # conn = pymssql.connect(f"user={msql['username']} password={msql['password']} database={msql['database']}")




        print('Подключено к MSQL')
        eel.reverse_info('True')
        # conn.close()
        # if conn.close():
        #     print('база closed')
        return True
    except:
        print('Не подключено к MSQL')
        eel.reverse_info('False')
        return False




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


# @eel.expose
# def msql_con(data):
#     print('msql принял', data)


@eel.expose
def psql_con(data):
    print('psql принял', data)


@eel.expose
def test_sql_con(data):
    print(data)


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
