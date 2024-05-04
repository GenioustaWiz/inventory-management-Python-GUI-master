import sys
from cx_Freeze import setup, Executable
#replaces command lin arg 'build'
#sys.argv.append("build")

filename = "index3.py"

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name = "IRS Pos",
      version = "1.0",
      description  = "Welcome to IRS",
      options = {"build_exe":{
            'packages':["tkinter","sqlite3","time","sales1","products","users","receipt"],
            #'ínclude_files':['boneca.jpg'],
            'include_msvcr': True,
      }},
      executables = [Executable(filename, base=base)])

#run in command line:  python setup.py bdist_msi