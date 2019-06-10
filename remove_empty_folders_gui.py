from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import Menu 
from functools import partial
import os

mypath = ''

def remove_empty(dir_path, counter):
    try:
        if not os.path.isdir(dir_path):
            return False

        if all([remove_empty(os.path.join(dir_path, filename), counter) for filename in os.listdir(dir_path)]):        
            counter[0]+=1
            os.rmdir(dir_path)
            counter[1]+=1
            return True
        else:
            return False
    except:
        counter[2]+=1


def func_about():
    messagebox.showinfo('Empty Folder Remover 0.1', 'Browse to a path to remove any empty directories it contains.\nRepo: https://github.com/PApostol/EmptyFolderRemover.git.\nWritten in Python 3.7. Feel free to modify and use as desired.')


def func_dir(window, button_del):
    global mypath
    mypath = filedialog.askdirectory()
    lbl = Label(window, text=mypath, bg='white', fg='black')
    lbl.place(relx=0.5, rely=0.3, anchor=N)

    if mypath:
        button_del.config(state=NORMAL)


def func_del():
    global mypath
    counter = [0,0,0]
    remove_empty(mypath, counter)

    output = []
    output.append('Found ' + str(counter[0]) + ' empty directories.')
    output.append('Deleted ' + str(counter[0]) + ' empty directories.')

    if counter[2]>0:
        output.append('Permission to access or delete some directories was denied.')

    str_out = '\n'.join(output)
    messagebox.showinfo('Finished', str_out)


def make_gui():
    window = Tk()
    window.title('Empty Folder Remover 0.1')
    window.geometry('300x200')
    
    menu = Menu(window)
    menu.add_cascade(label='About', command=func_about)
    menu.add_cascade(label='Exit', command=window.destroy)
    window.config(menu=menu)
    
    button_del = Button(window, text='Remove empty', bg='grey', fg='black', command=func_del)
    button_del.place(relx=0.5, rely=0.5, anchor=N)
    button_del.config(state=DISABLED)

    button_dir = Button(window, text='Choose path', bg='grey', fg='black', command=partial(func_dir, window, button_del))
    button_dir.place(relx=0.5, rely=0.1, anchor=N)

    window.mainloop()


def main():
    try:
        make_gui()    
    except Exception as e:
        raise e


if __name__=='__main__':
    main()