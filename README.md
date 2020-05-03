<img src="https://github.com/jrib02/CardinalAIDSplus/blob/master/UI/CardinalAIDS-full.jpg" width="200" height="200">

# CardinalAIDS+
A student information system chatbot developed by Mapúa University Computer Engineering students for fellow Mapúans.

Link of the project documentation: https://bit.ly/3b47jz3

## Important Prerequisites for Execution
### Python 3.7+
The CardinalAIDS+ project is based on Python 3.7+ and therefore requires a Python environment with the specified version. Kindly install it before beginning. Here are guides for [Linux](https://docs.python-guide.org/starting/install3/linux/#install3-linux), [Windows](https://docs.python-guide.org/starting/install3/win/#install3-windows), and [macOS](https://docs.python-guide.org/starting/install3/osx/#install3-osx). It is recommended to be in the latest version unless specified.
### SQLite
After installing Python or having already installed it before, check for the installation of SQLite by typing the following into a Python terminal:

    sqlite3
The following output should be similar to this and means that it is installed:
    
    SQLite version 3.30.0 2019-10-04 15:03:17
    Enter ".help" for usage hints.
    Connected to a transient in-memory database.
    Use ".open FILENAME" to reopen on a persistent database.
    sqlite>
SQLite should come packaged with Python's standard library but kindly check just to be sure. Should SQLite not be installed on your device, here is a guide for installation on [Linux, Windows, and macOS](https://www.tutorialspoint.com/sqlite/sqlite_installation.htm)
### PyQt5
This project utilizes PyQT5 for its GUI and requires it to be installed. Check if the package is already installed by typing the following into a Python terminal and looking for PyQt5-sip:

    pip list
If the package is missing, follow this installation guide for [Linux, Windows, and macOS](https://pythonbasics.org/install-pyqt/).

## Running CardinalAIDS+
Clone or download the GitHub repository [here](https://github.com/jrib02/CardinalAIDSplus.git). The top level folder should be _**CardinalAIDSplus**_ (repository name) and subfolders _**BLL, DAL, UI and TEST**_ should be found within.
In a Python terminal, possibly within an IDE, navigate to the repository or _**CardinalAIDSplus**_ folder and enter the command:

    python BLL\main.py
If no errors are met, the CardinalAIDS+ Login Window should appear and the program will begin its process.
