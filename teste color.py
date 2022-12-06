import tkinter as tk
from tkinter import ttk
from tkinter.colorchooser import askcolor


root = tk.Tk()
root.title('Tkinter Color Chooser')
root.geometry('300x150')


def change_color():
    colors = askcolor(title="Tkinter Color Chooser")
    print('colors[1]: ', colors)
    hex_color1 = colors[1].upper()
    print('colors[1]: ', hex_color1)
    
    root.configure(bg=colors[1])


ttk.Button(
    root,
    text='Select a Color',
    command=change_color).pack(expand=True)
change_color()

root.mainloop()
