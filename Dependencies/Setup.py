import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"],
                     "include_files": ['Dependencies', 'Add', 'Status', 'Images', 'Logs']}

# GUI applications require a different base on Windows (the default is for
# a console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="QualiCheck",
    version="1.0",
    description="QualiCheck",
    options={"build_exe": build_exe_options},
    executables=[Executable("QualiCheck.py", base=base, icon="Images/QualiCheck.ico")]
)
