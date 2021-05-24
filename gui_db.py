from os import closerange
from tkinter import *
import pyodbc
from tkinter import ttk
from tkinter.messagebox import showinfo
import re

class GUI():

    def __init__(self, master) -> None:

        '''
        GUI
        '''
        self.master = master
        # self.masterttk = master_ttk

        self.master.title("Interface of DB")
        self.master.geometry("300x200")

        self.search_button = Button(self.master, text="Search", command=self.open_window)
        self.search_button.place(relx=0.5, rely=0.1, anchor=CENTER)

        self.delete_button = Button(self.master, text="Delete")
        self.delete_button.place(relx=0.5, rely=0.3, anchor=CENTER)

        self.add_button = Button(self.master, text= "Add")
        self.add_button.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.modify_button = Button(self.master, text="Modify") 
        self.modify_button.place(relx=0.5, rely=0.7, anchor=CENTER)

        
        '''
        pyodbc
        '''
        try:
            self.connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                                    'SERVER=localhost;'
                                    'DATABASE=dbBiblioteca;'
                                    'Trusted_Connection=yes;')

            self.cursor = self.connection.cursor()
            # self.cursor.execute(f'SELECT * FROM dbBiblioteca.dbo.catCATEGORIA_USUARIO')

        except Exception as e:
            print(str(e))


    global t_option
    def selected_table_option(self, event) -> None:

        # Tabla que escogio el usuario
        self.t_option = event.widget.get()

    global c_option
    def selected_column_option(self, event) -> None:

        # Columna que escogio el usuario
        self.c_option = event.widget.get()

    
    def query_with_selected_options(self) -> None:

        # Obtener nombres de columnas de la tabla elegida
        # print(f"SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE N'{self.t_option}'")
        self.cursor.execute(f"SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'{self.t_option}'")
        self.rowcolumns = [row for row in self.cursor]
        # print("Esto es\n:" + str(self.rowcolumns))


        # Primero borramos el contenido
        self.text_box.delete("1.0", "end")
        
        # SELECT column FROM table
        self.cursor.execute(f"SELECT {self.c_option} FROM {self.t_option}")
        for row in self.cursor:
            self.text_box.insert(END, str(row)+"\n")



    def open_window(self) -> None:

        self.new = Toplevel(self.master)
        self.new.title("Show Window")
        self.new.geometry("400x400") 

        # Obtener nombres de tablas que empiecen por tbl
        self.cursor.execute("SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME LIKE 'tbl%'")

        self.row_to_list = [row for row in self.cursor]

        # Lista con el nombre de las puras tablas
        self.clean_row_list = []

        for x in self.row_to_list:
            for y in x:
                if re.search('tbl\w+', y):
                    self.clean_row_list.append(y)


        self.labelTOP = Label(self.new, text="Lista de tablas.")
        self.labelTOP.pack()


        self.db_tables = ttk.Combobox(self.new)
        self.db_tables['values'] = self.clean_row_list
        self.db_tables.pack()

        self.db_tables.bind("<<ComboboxSelected>>", self.selected_table_option)


        

        self.labelCENTER = Label(self.new, text="Choose one")
        self.labelCENTER.pack()
        

        self.search_options = ttk.Combobox(self.new,
                                           values=[
                                               "ID_LIBRO",
                                               "AUTOR", # Autor no es parte de la tabla tblLibro
                                               "ID_AUTOR",
                                               "EDITORIAL",
                                               "ID_EDITORIAL",
                                               "IDIOMA",
                                               "ID_IDIOMA"
                                           ]
        )

        self.search_options.pack()
        self.search_options.bind("<<ComboboxSelected>>", self.selected_column_option)
        self.accept_botton = Button(self.new, text="Accept", command=self.query_with_selected_options)
        self.accept_botton.pack()

        self.text_box = Text(self.new, width=24, height=10)
        self.text_box.pack()

    # def show_input_box(self) -> None:
    #     print(f"Entrada: {self.input.get()}")


root = Tk()
my_gui = GUI(root)
# my_gui.connection
root.mainloop()