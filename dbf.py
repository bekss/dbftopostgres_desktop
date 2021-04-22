from cx_Freeze import setup,Executable
import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["glob", "json", "os", "tkinter", "psycopg2", "eel", "dataset", "tkinter", "pyodbc", "wx", "dbfread"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

# setup(
#     name="BeksS Ltd.Corporation",
#     version="0.1",
#     description = "BeksS Ltd.Corporation",
#     options = {"build_exe": build_exe_options},
#     executables = [Executable("mainwn.py", base = base)])

setup(name="TS Ltd.Corporation",
        version="0.1",
        description="TS Ltd.Corporation",
        options={"build_exe": build_exe_options},
        executables=[Executable("main.py", base=base)]
        )