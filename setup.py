from cx_Freeze import setup, Executable

# define your executable and its options
executables = [Executable('gui.py', base='Win32GUI')]

# setup the executable build
setup(
    name='Data Query Tool',
    version='1.0',
    description='A GUI tool to query data and export to CSV',
    executables=executables
)
