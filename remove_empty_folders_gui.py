"""GUI to recursively remove empty directories in a given path"""
import os
from functools import partial
from tkinter import *
from tkinter import Menu, filedialog, messagebox
from typing import List

TITLE = 'Empty Folder Remover 0.3.0'
MYPATH = ''
MYLIST = []


def func_about():
    messagebox.showinfo(
        TITLE,
        'Browse to a path to remove any empty directories it contains.\nRepo: https://github.com/PApostol/EmptyFolderRemover.git',
    )


def find_empty(dir_path: str, lista: List[str]) -> bool:
    try:
        if not os.path.isdir(dir_path):
            return False

        if all([find_empty(os.path.join(dir_path, filename), lista) for filename in os.listdir(dir_path)]):
            lista.append(dir_path)
            return True
        return False
    except:
        pass


def func_dir(_, path_text: StringVar, button_find: Button, button_del: Button) -> None:
    button_find.config(state=DISABLED)
    button_del.config(state=DISABLED)

    global MYPATH
    MYPATH = filedialog.askdirectory()
    path_text.set(MYPATH)

    if MYPATH:
        button_find.config(state=NORMAL)


def func_find(_, listbox: Listbox, found_text: StringVar, button_del: Button) -> None:
    global MYPATH, MYLIST
    MYLIST = []   # reset list

    listbox.delete(0, 'end')   # reset listbox
    find_empty(MYPATH, MYLIST)

    if not MYLIST:
        found_text.set('Found: 0')
        messagebox.showinfo('Finished', 'No empty directories found.')
    else:
        for directory in MYLIST:
            listbox.insert(END, directory)

        found = len(MYLIST)
        found_text.set(f'Found: {found}')

        messagebox.showinfo('Finished', f'Empty directories found: {found}')
        button_del.config(state=NORMAL)


def func_del(listbox: Listbox, del_text: StringVar) -> None:
    global MYLIST
    counter_del = 0
    counter_err = 0

    for i, directory in enumerate(MYLIST):
        try:
            os.rmdir(directory)
            listbox.itemconfig(i, fg='green')
        except:
            counter_err += 1
        else:
            counter_del += 1

    del_text.set(f'Deleted: {counter_del}')
    str_out = f'Empty directories deleted: {counter_del}'

    if counter_err > 0:
        str_out += '\nPermission to access or delete some directories was denied.'

    messagebox.showinfo('Finished', str_out)


def make_gui() -> None:
    # frame
    root = Tk()
    root.title(TITLE)
    root.configure(background='LightSkyBlue1')
    root.geometry('400x600')
    root.resizable(False, False)

    # menu
    menu = Menu(root)
    menu.add_cascade(label='About', command=func_about)
    menu.add_cascade(label='Exit', command=root.destroy)
    root.config(menu=menu)

    # scrollbars & listbox
    scrolly = Scrollbar(root, orient='vertical')
    scrolly.place(relx=0.95, rely=0.3, relheight=0.645, anchor=N)

    scrollx = Scrollbar(root, orient='horizontal')
    scrollx.place(relx=0.5, rely=0.95, relwidth=0.83, anchor=N)

    listbox = Listbox(root, width=55, height=24, xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
    listbox.place(relx=0.5, rely=0.3, anchor=N)

    scrolly.config(command=listbox.yview)
    scrollx.config(command=listbox.xview)

    # labels
    path_text = StringVar()
    path_label = Label(root, textvariable=path_text, bg='LightSkyBlue1', fg='black')
    path_label.place(relx=0.5, rely=0.12, anchor=N)

    found_text = StringVar()
    found_label = Label(root, textvariable=found_text, bg='LightSkyBlue1', fg='black')
    found_label.place(relx=0.3, rely=0.25, anchor=N)

    del_text = StringVar()
    del_label = Label(root, textvariable=del_text, bg='LightSkyBlue1', fg='black')
    del_label.place(relx=0.7, rely=0.25, anchor=N)

    # remove button
    button_del = Button(
        root, text='Remove empty', bg='SpringGreen2', fg='black', command=partial(func_del, listbox, del_text)
    )
    button_del.place(relx=0.7, rely=0.18, anchor=N)
    button_del.config(state=DISABLED)

    # find button
    button_find = Button(
        root,
        text='Find empty',
        bg='SpringGreen2',
        fg='black',
        command=partial(func_find, root, listbox, found_text, button_del),
    )
    button_find.place(relx=0.3, rely=0.18, anchor=N)
    button_find.config(state=DISABLED)

    # path button
    button_dir = Button(
        root,
        text='Choose path',
        bg='SpringGreen2',
        fg='black',
        command=partial(func_dir, root, path_text, button_find, button_del),
    )
    button_dir.place(relx=0.5, rely=0.05, anchor=N)

    root.mainloop()


if __name__ == '__main__':
    make_gui()
