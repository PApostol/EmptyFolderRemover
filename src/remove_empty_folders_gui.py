from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import Menu 
from functools import partial
import os

mypath = ''
lista = []

def func_about():
    messagebox.showinfo('Empty Folder Remover 0.2.0', 'Browse to a path to remove any empty directories it contains.\nRepo: https://github.com/PApostol/EmptyFolderRemover.git.\nWritten in Python 3.7. Feel free to modify and use as desired.')


def find_empty(dir_path, lista):
    try:
        if not os.path.isdir(dir_path):
            return False

        if all([find_empty(os.path.join(dir_path, filename), lista) for filename in os.listdir(dir_path)]):        
            lista.append(dir_path)
            return True
        else:
            return False
    except:
        pass


def func_dir(root, path_text, button_find, button_del):
    button_find.config(state=DISABLED)
    button_del.config(state=DISABLED)

    global mypath
    mypath = filedialog.askdirectory()

    path_text.set(mypath)

    if mypath:
        button_find.config(state=NORMAL)


def func_find(root, listbox, found_text, button_del):
    global mypath, lista
    lista = [] # reset list

    listbox.delete(0, 'end') # reset listbox
    find_empty(mypath, lista)

    if not lista:
        found_text.set('Found: 0')
        messagebox.showinfo('Finished', 'No empty directories found.')

    else:
        for dir in lista:
            listbox.insert(END, dir)
        
        found = str(len(lista))
        found_text.set('Found: ' + found)

        messagebox.showinfo('Finished', 'Empty directories found: ' + found)
        button_del.config(state=NORMAL)


def func_del(listbox, del_text):
    global lista
    counter_del = 0
    counter_err = 0

    for i, dir in enumerate(lista):
        try:
            os.rmdir(dir)
            listbox.itemconfig(i, fg='green')
        except:
            counter_err+=1
        else:
            counter_del+=1

    deleted = str(counter_del)
    del_text.set('Deleted: ' + deleted)

    str_out =  'Empty directories deleted: ' + deleted
    if counter_err>0:
        str_out+='\nPermission to access or delete some directories was denied.'
    
    messagebox.showinfo('Finished', str_out)


def make_gui():
    # frame
    root = Tk()
    root.title('Empty Folder Remover 0.2.0')
    root.configure(background='LightSkyBlue1')
    root.geometry('400x600')
    root.resizable(False, False)
    
    # menu
    menu = Menu(root)
    menu.add_cascade(label='About', command=func_about)
    menu.add_cascade(label='Exit', command=root.destroy)
    root.config(menu=menu)

    # scrollbars & listbox
    scrolly = Scrollbar(root, orient="vertical")
    scrolly.place(relx=0.95, rely=0.3, relheight=0.645, anchor=N)

    scrollx = Scrollbar(root, orient="horizontal")
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
    del_label = Label(root,  textvariable=del_text, bg='LightSkyBlue1', fg='black')
    del_label.place(relx=0.7, rely=0.25, anchor=N)

    # remove button
    button_del = Button(root, text='Remove empty', bg='SpringGreen2', fg='black', command=partial(func_del, listbox, del_text))
    button_del.place(relx=0.7, rely=0.18, anchor=N)
    button_del.config(state=DISABLED)
    
    # find button
    button_find = Button(root, text='Find empty', bg='SpringGreen2', fg='black', command=partial(func_find, root, listbox, found_text, button_del))
    button_find.place(relx=0.3, rely=0.18, anchor=N)
    button_find.config(state=DISABLED)

    # path button
    button_dir = Button(root, text='Choose path', bg='SpringGreen2', fg='black', command=partial(func_dir, root, path_text, button_find, button_del))
    button_dir.place(relx=0.5, rely=0.05, anchor=N)

    root.mainloop()


def main():
    try:
        make_gui()
    except Exception as err:
        raise err


if __name__=='__main__':
    main()