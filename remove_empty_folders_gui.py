from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import Menu 
from functools import partial
import os

mypath = ''
lista = []

def func_about():
    messagebox.showinfo('Empty Folder Remover 0.1', 'Browse to a path to remove any empty directories it contains.\nRepo: https://github.com/PApostol/EmptyFolderRemover.git.\nWritten in Python 3.7. Feel free to modify and use as desired.')


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


def func_dir(root, button_find, button_del):
    button_find.config(state=DISABLED)
    button_del.config(state=DISABLED)

    global mypath
    mypath = filedialog.askdirectory()

    path_label = Label(root, text=mypath, bg='white', fg='black')
    path_label.place(relx=0.5, rely=0.2, anchor=N)

    if mypath:
        button_find.config(state=NORMAL)


def func_find(root, listbox, button_del):
    global mypath, lista
    find_empty(mypath, lista)

    if not lista:
        messagebox.showinfo('Finished', 'No empty directories found.')

    else:
        for dir in lista:
            listbox.insert(END, dir)
        
        button_del.config(state=NORMAL)
        messagebox.showinfo('Finished', 'Empty directories found: ' + str(len(lista)))


def func_del():
    global lista
    counter_del = 0
    counter_err = 0

    for dir in lista:
        try:
            os.rmdir(dir)
        except:
            counter_err+=1
        else:
            counter_del+=1

    str_out =  'Empty directories deleted: ' + str(counter_del)
    if counter_err>0:
        str_out+='\nPermission to access or delete some directories was denied.'
    
    messagebox.showinfo('Finished', str_out)


def make_gui():
    # frame
    root = Tk()
    root.title('Empty Folder Remover 0.1')
    root.geometry('300x400')
    #root.resizable(False, False)
    
    # menu
    menu = Menu(root)
    menu.add_cascade(label='About', command=func_about)
    menu.add_cascade(label='Exit', command=root.destroy)
    root.config(menu=menu)

    # listbox
    listbox = Listbox(root,width=40, height=12)
    listbox.place(relx=0.5, rely=0.4, anchor=N)

    # path label
    #path_label = Label(root, bg='white', fg='black')
    #path_label.place(relx=0.5, rely=0.2, anchor=N)

    # remove button
    button_del = Button(root, text='Remove empty', bg='grey', fg='black', command=func_del)
    button_del.place(relx=0.7, rely=0.3, anchor=N)
    button_del.config(state=DISABLED)
    
    # find button
    button_find = Button(root, text='Find empty', bg='grey', fg='black', command=partial(func_find, root, listbox, button_del))
    button_find.place(relx=0.3, rely=0.3, anchor=N)
    button_find.config(state=DISABLED)

    # path button
    button_dir = Button(root, text='Choose path', bg='grey', fg='black', command=partial(func_dir, root, button_find, button_del))
    button_dir.place(relx=0.5, rely=0.05, anchor=N)

    root.mainloop()


def main():
    try:
        make_gui()
    except Exception as e:
        raise e


if __name__=='__main__':
    main()