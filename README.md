## Empty Folder Remover

Helps keeping yous system tidy by removing empty folders. Available both as a graphical user interface (GUI, better suited for Windows) and a command-line interface (CLI, better suited for Linux). Requires Python 3.7+.

Note: It is generally safe to remove empty folders, even from system directories. However, removing zero byte files is not recommended.

Depending on your user rights, some folders might not be removable, e.g. you might need to be an admin to remove system folders.

### GUI version

Just run `remove_empty_folders_gui.exe` (Windows only)

Or use command line/terminal: `python remove_empty_folders_gui.py`

Note: The GUI version uses `tkinter`, which is not part of Python in Linux by default. If not present, install via `sudo apt-get install python3-tk`.

### CLI version

Use command line or terminal: `python remove_empty_folders_cli.py [path]`

If no path is provided, script will assume current working directory as path.

### Compile Binaries
To compile to a single binary (e.g. executable), install [pyinstaller](https://pypi.org/project/PyInstaller/) and run:

`pyinstaller --onefile remove_empty_folders_gui.py`

Note that this will make the binary tied to the OS you create it on (e.g. running on Windows will create an .exe that can't run on Linux, and vice-versa).


### Disclaimer
Use with your own risk. No contributor is responsible for any damage caused to your system.
