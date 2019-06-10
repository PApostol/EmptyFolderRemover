# Empty Folder Remover

Helps keeping yous system tidy by removing empty folders. Written in Python 3.7.
Note: it is generally safe to remove empty folders, even from system directories. However, removing zero byte files is not recommended.

## GUI version - uses `tkinter`

-How to use `remove_empty_folders_gui.py`:

Use command line or terminal:

-Windows: `python remove_empty_folders_gui.py`

-Linux: `sudo python3 remove_empty_folders_gui.py`

Note: `tkinter` is not part of Python in Linux by default. If not present, install via `sudo apt-get install python3-tk`.

## CMD version

-How to use `remove_empty_folders.py`:

Use command line or terminal:

-Windows: `python remove_empty_folders.py`

-Linux: `sudo python3 remove_empty_folders.py`

Optional argument: `path`

e.g. `python remove_empty_folders.py 'C:/'`

If no path is provided, script will assume current working directory as path.



## Disclaimer:

Use with your own risk. No contributor is responsible for any damage caused to your system.
