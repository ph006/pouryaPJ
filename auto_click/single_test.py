from cx_Freeze import setup, Executable

executables = [Executable("your_script.py")]

setup(
    name="YourScript",
    version="1.0",
    description="Description of your script",
    executables=executables
)