from os import closerange
from tkinter import *
import pyodbc
from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showinfo


from classAdd import *
from classShow import *
from classModify import *
from classDelete import *

class GUI:

    def __init__(self, master):

        '''
        GUI
        '''
        self.master = master
        self.frame = Frame(self.master)
        self.frame.pack()

        '''
        pyodbc
        '''
        # try:
        self.connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                                'SERVER=localhost;'
                                'DATABASE=dbBiblioteca;'
                                'Trusted_Connection=yes;')

        self.cursor = self.connection.cursor()

        self.master.title("Interface of DB")
        self.master.geometry("300x200")

        self.search_button = Button(self.master, text="Search", command=self.show_window)
        self.search_button.place(relx=0.5, rely=0.1, anchor=CENTER)

        self.add_button = Button(self.master, text="Add", command=self.add_window)
        self.add_button.place(relx=0.5, rely=0.3, anchor=CENTER)

        self.modify_button = Button(self.master, text="Modify", command=self.modify_window) 
        self.modify_button.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.delete_button = Button(self.master, text="Delete", command=self.delete_window)
        self.delete_button.place(relx=0.5, rely=0.7, anchor=CENTER)

    def show_window(self) -> None:
        self.show_Window = tk.Toplevel(self.master)
        self.app = Show(self.show_Window, self.cursor)

    def add_window(self) -> None:
        self.add_Window = tk.Toplevel(self.master)
        self.app2 = Add(self.add_Window, self.cursor)

    def modify_window(self) -> None:
        self.modify_Window = tk.Toplevel(self.master)
        self.app3 = Modify(self.modify_Window, self.cursor)

    def delete_window(self) -> None:
        self.delete_Window = tk.Toplevel(self.master)
        self.app4 = Delete(self.delete_Window, self.cursor)



def main():
    root = tk.Tk()
    GUI.show_window
    app = GUI(root)
    root.mainloop()

main()
