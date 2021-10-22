import tkinter as tk
from tkinter import ttk

win=tk.Tk()
win.title("MENUBAR")


#MENU


"""menubar=tk.Menu(win)  # menubar is a object of class Menu

def func():
    print('func called')

menubar.add_command(label='Home',command=func)
menubar.add_command(label='Reviews',command=func)
menubar.add_command(label='Search',command=func)
menubar.add_command(label='About',command=func)
menubar.add_command(label='Save',command=func) """

def func():
    print('func called')

main_menu=tk.Menu(win)
main_menu.add_command(label='Home',command=func)
main_menu.add_command(label='Reviews',command=func)
main_menu.add_command(label='Help',command=func)
main_menu.add_command(label='About',command=func)
file_menu=tk.Menu(main_menu,tearoff=0)
file_menu.add_command(label='New File',command=func)
file_menu.add_command(label='New Window',command=func)
file_menu.add_separator()  # this will create a separator 
file_menu.add_command(label='Save file',command=func)
file_menu.add_command(label='Editor',command=func)

# edit menu
edit_menu=tk.Menu(main_menu,tearoff=0)
edit_menu.add_command(label='Undo',command=func)
edit_menu.add_command(label='Redo',command=func)

main_menu.add_cascade(label='File',menu=file_menu)
main_menu.add_cascade(label='EDIT',menu=edit_menu)
win.config(menu=main_menu)
#win.config(menu=menubar)


win.mainloop()