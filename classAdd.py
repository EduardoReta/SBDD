import tkinter as tk
import re
from tkinter import *
from rich.console import Console
from rich import style
from datetime import datetime, timedelta, date

class Add:
    def __init__(self, master, cursor):
        self.master = master
        self.cursor = cursor
        self.frame = Frame(self.master)
        self.master.title("Add Window")
        self.master.geometry("400x400")

        self.autor_button = Button(self.master, text="Autor", command=self.add_autor_window)
        self.autor_button.place(relx=0.5, rely=0.1, anchor=CENTER)

        self.lending_button = Button(self.master, text="Prestamos", command=self.add_lending_window)
        self.lending_button.place(relx=0.5, rely=0.3, anchor=CENTER)

        self.devolution_button = Button(self.master, text="Devoluciones", command=self.add_devolution_window)
        self.devolution_button.place(relx=0.5, rely=0.5, anchor=CENTER)

    def add_autor_window(self):
        self.add_autor = tk.Toplevel(self.master)
        self.autor = Autor(self.add_autor, self.cursor)

    def add_lending_window(self):
        self.add_lending = tk.Toplevel(self.master)
        self.lending = Prestamos(self.add_lending, self.cursor)

    def add_devolution_window(self):
        self.add_devolution = tk.Toplevel(self.master)
        self.devolution = Devolucion(self.add_devolution, self.cursor)

class Autor:
    def __init__(self, master, cursor):
        self.cursor = cursor
        self.master = master
        self.frame = Frame(self.master)
        self.master.title("Agregar autores")
        self.master.geometry("800x800")
        self.console = Console()

        self.label1 = Label(self.master, text="Insertar valor:")
        self.label1.pack()

        self.value_to_table = StringVar()
        self.insert_value = Entry(self.master, textvariable=self.value_to_table)
        self.insert_value.pack()

        self.execute_insert = Button(self.master, text="Aceptar", command=self.insert_value_query)#, self. )
        self.execute_insert.pack()

        self.null_button = Button(self.master, text="Sin Valor", command=self.null_value)#, self. )
        self.null_button.pack()        

        self.text_box = Text(self.master, width=500, height=500)
        self.text_box.pack()

        global contador
        self.contador = 1

        self.number_of_column_to_insert = 1

        # Mostrar tabla automaticamente cuando se abra la ventana de insertar autor.
        self.show_table()


    def show_table(self) -> str:
        self.text_box.delete(1.0, END)

        # Obtenemos el numero de columnas de la tabla a la que se desea agregar el registro para
        # cambiar dinamicamente el numero de widgets "Entry" (entrada texto) de acuerdo
        # a la tabla seleccionada
        self.cursor.execute("SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME LIKE 'tbl%'")
        self.row_to_list = [row for row in self.cursor]

        # Lista con el nombre de las puras tablas
        self.clean_row_list = [] 

        for x in self.row_to_list:
            for y in x:
                if re.search('tbl\w+', y):
                    self.clean_row_list.append(y)

        self.cursor.execute(f"SELECT * FROM tblAUTOR")
        for column in self.cursor.description:
            self.text_box.insert(END, str(column[0]) + " | ")

        self.row_to_list = [row for row in self.cursor]

        for item in self.row_to_list:
            try:
                self.text_box.insert(END, "\n"+str(item)) 
            except Exception as e:
                print(str(e))


        # Obtener nombres de columnas
        self.cursor.execute(f"SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'tblAUTOR'")
        self.row_to_list = [row for row in self.cursor]
        self.clean_row_list = []
        for item in self.row_to_list:
            self.clean_row_list.append(item[3])

        # Numero de columnas
        global quantity_columns
        self.quantity_columns = len(self.clean_row_list) - 1

        # Almacenar la columna en la que se va a insertar el valor
        global list_of_column_to_insert_value
        self.list_of_column_to_insert_value = []
        self.list_of_column_to_insert_value.append("ID_AUTOR")

        # Almacenan los valores a insertar en la tabla
        global list_of_values_to_insert
        self.list_of_values_to_insert = []

        # Le asignamos el siguiente ID_AUTOR que este disponible
        # self.cursor.execute("SELECT TOP 1 ID_AUTOR FROM tblAUTOR ORDER BY ID_AUTOR DESC;")
        # self.value_returned = [row for row in self.cursor]
        # self.list_of_values_to_insert.append(self.value_returned[0][0] + 1)

        self.label1.configure(text=f"Inserte valor de: {self.clean_row_list[1]}")               


    def insert_value_query(self):

        self.cursor.execute("SELECT TOP 1 ID_AUTOR FROM tblAUTOR ORDER BY ID_AUTOR DESC;")
        self.value_returned = [row for row in self.cursor]
        x = self.value_returned[0][0] + 1

        if x not in self.list_of_values_to_insert:
            self.new_id_autor()


        if "ID_AUTOR" not in self.list_of_column_to_insert_value:
            self.list_of_column_to_insert_value.append("ID_AUTOR")

        if self.contador < self.quantity_columns:
            self.label1.configure(text=f"Inserte valor de: {self.clean_row_list[self.contador + 1]}")
            self.label1.update()

        elif self.contador == self.quantity_columns:
            self.label1.configure(text=f"Inserte valor de: {self.clean_row_list[self.contador]}")
            self.label1.update()

        if self.number_of_column_to_insert <= self.quantity_columns:
            if self.contador <= self.quantity_columns:
                self.list_of_column_to_insert_value.append(self.clean_row_list[self.contador])
                self.list_of_values_to_insert.append(self.value_to_table.get())

                self.console.print("Lista valores columna" + str(self.list_of_column_to_insert_value), style='red')
                self.console.print("Lista valores " + str(self.list_of_values_to_insert), style='blue')
                self.console.print("Numero de columna a insertar " + str(self.number_of_column_to_insert), style='green')
                self.console.print("Cantidad de columnas " + str(self.quantity_columns), style='yellow')
                self.console.print("Contador " + str(self.contador), style='bold red')
                print("-"*50)

        # Cuando se inserte el ultimo valor haga lo siguiente
        if self.number_of_column_to_insert == self.quantity_columns:

            # Reiniciar valores para que puedan volver a introducir registros
            self.contador = 0
            self.number_of_column_to_insert = 1
            self.label1.configure(text=f"Inserte valor de: {self.clean_row_list[1]}")

            # En teoria quedaria si:
            #   self.list_of_column_to_insert_value = ['ID_AUTOR', 'NOMBRE', 'APELLIDO_PAT', 'APELLIDO_MAT'] Esto no -> , 'DIA_PUBLICACION', 'MES_PUBLICACION', 'AÑO_PUBLICACION']
            #   self.list_of_values_to_insert) = [valor0, valor1, valor2, valor3]  Esto no -> , valor4, valor5, valor6]

            self.cursor.execute(f"INSERT INTO tblAUTOR ({str(self.list_of_column_to_insert_value[0])}, {str(self.list_of_column_to_insert_value[1])}, {str(self.list_of_column_to_insert_value[2])}, {str(self.list_of_column_to_insert_value[3])}) VALUES ({str(self.list_of_values_to_insert[0])}, '{str(self.list_of_values_to_insert[1])}', '{str(self.list_of_values_to_insert[2])}', '{str(self.list_of_values_to_insert[3])}')")
            self.cursor.commit()

            # Cuando se inserte el registro de autor, actualizamos el contenido en la misma ventana.
            self.text_box.delete(1.0, END)
            self.cursor.execute(f"SELECT * FROM tblAUTOR")
            for column in self.cursor.description:
                self.text_box.insert(END, str(column[0]) + " | ")

            self.row_to_list = [row for row in self.cursor]

            for item in self.row_to_list:
                try:
                    self.text_box.insert(END, "\n"+str(item)) 
                except Exception as e:
                    print(str(e))
            
            # Reiniciar valores para que puedan volver a introducir registros
            self.list_of_column_to_insert_value = []
            self.list_of_values_to_insert = []
            self.number_of_column_to_insert = 1
            self.quantity_columns = len(self.clean_row_list) - 1
            self.contador = 1
                        
        else:

            # FIXME: Mandar mensaje si se inserto el ultimo valor de la tabla
            # NOTE: No es necesario avisar ya que cuando se inserte el ultimo valor, se cambiara
            #       el nombre del Label por el de la primera columna.
            self.number_of_column_to_insert += 1
            self.contador = self.contador + 1
            self.insert_value.delete(0, 'end')


    # Insertar "DEFAULT" como valor para dar valor nulo a columna dada 
    def null_value(self):
        self.list_of_column_to_insert_value.append(self.clean_row_list[self.contador] )
        self.list_of_values_to_insert.append("DEFAULT")
        self.label1.configure(text=f"Inserte valor de: {self.clean_row_list[self.contador + 1]}")
        self.label1.update()

        self.number_of_column_to_insert += 1
        self.contador += 1


    def new_id_autor(self):
        # Le asignamos el siguiente ID_PRESTAMO que este disponible
        self.cursor.execute("SELECT TOP 1 ID_AUTOR FROM tblAUTOR ORDER BY ID_AUTOR DESC;")
        self.value_returned = [row for row in self.cursor]
        self.list_of_values_to_insert.append(self.value_returned[0][0] + 1)



class Prestamos:

    def __init__(self, master, cursor):
        self.cursor = cursor
        self.master = master
        self.frame = Frame(self.master)
        self.master.title("Prestamos")
        self.master.geometry("800x800")
        self.console = Console()


        self.label1 = Label(self.master, text="Insertar valor:")
        self.label1.pack()

        self.value_to_table = StringVar()
        self.insert_value = Entry(self.master, textvariable=self.value_to_table)
        self.insert_value.pack()

        self.execute_insert = Button(self.master, text="Aceptar", command=self.insert_value_query)#, self. )
        self.execute_insert.pack()

        self.text_box = Text(self.master, width=500, height=500)
        self.text_box.pack()
        
        global contador
        self.contador = 1

        self.number_of_column_to_insert = 1

        # Mostrar tabla automaticamente cuando se abra la ventana de insertar autor.
        self.show_table()



    def show_table(self) -> str:
        self.text_box.delete(1.0, END)

        # Obtenemos el numero de columnas de la tabla a la que se desea agregar el registro para
        # cambiar dinamicamente el numero de widgets "Entry" (entrada texto) de acuerdo
        # a la tabla seleccionada
        self.cursor.execute("SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME LIKE 'tbl%'")
        self.row_to_list = [row for row in self.cursor]

        # Lista con el nombre de las puras tablas
        self.clean_row_list = [] 

        for x in self.row_to_list:
            for y in x:
                if re.search('tbl\w+', y):
                    self.clean_row_list.append(y)

        self.cursor.execute(f"SELECT * FROM tblPRESTAMOS")
        for column in self.cursor.description:
            self.text_box.insert(END, str(column[0]) + " | ")

        self.row_to_list = [row for row in self.cursor]

        for item in self.row_to_list:
            try:
                self.text_box.insert(END, "\n"+str(item)) 
            except Exception as e:
                print(str(e))


        # Obtener nombres de columnas
        self.cursor.execute(f"SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'tblPRESTAMOS'")
        self.row_to_list = [row for row in self.cursor]
        self.clean_row_list = []
        for item in self.row_to_list:
            self.clean_row_list.append(item[3])
        
        # Numero de columnas
        global quantity_columns
        self.quantity_columns = len(self.clean_row_list) - 3 # ID_PRESTAMO, FECHA_PRESTAMO, FECHA REGRESO
        print(self.quantity_columns)
        # Almacenar la columna en la que se va a insertar el valor
        global list_of_column_to_insert_value
        self.list_of_column_to_insert_value = []
        self.list_of_column_to_insert_value.append("ID_PRESTAMO")

        # Almacenan los valores a insertar en la tabla
        global list_of_values_to_insert
        self.list_of_values_to_insert = []

        global values_devolution
        self.values_devolution = []

        self.label1.configure(text=f"Inserte valor de: {self.clean_row_list[1]}")  


    def insert_value_query(self):

        self.cursor.execute("SELECT TOP 1 ID_PRESTAMO FROM tblPRESTAMOS ORDER BY ID_PRESTAMO DESC;")
        self.value_returned = [row for row in self.cursor]
        x = self.value_returned[0][0] + 1

        if x not in self.list_of_values_to_insert:
            self.new_id_lending()

        if "ID_PRESTAMO" not in self.list_of_column_to_insert_value:
            self.list_of_column_to_insert_value.append("ID_PRESTAMO")

        if self.contador < self.quantity_columns:
            self.label1.configure(text=f"Inserte valor de: {self.clean_row_list[self.contador + 1]}")
            self.label1.update()

        elif self.contador == self.quantity_columns:
            self.label1.configure(text=f"Inserte valor de: {self.clean_row_list[self.contador]}")
            self.label1.update()


        if self.number_of_column_to_insert <= self.quantity_columns:
            if self.contador <= self.quantity_columns:
                self.list_of_column_to_insert_value.append(self.clean_row_list[self.contador])
                self.list_of_values_to_insert.append(self.value_to_table.get())

                self.console.print("Lista valores columna" + str(self.list_of_column_to_insert_value), style='red')
                self.console.print("Lista valores " + str(self.list_of_values_to_insert), style='blue')
                self.console.print("Numero de columna a insertar " + str(self.number_of_column_to_insert), style='green')
                self.console.print("Cantidad de columnas " + str(self.quantity_columns), style='yellow')
                self.console.print("Contador " + str(self.contador), style='bold red')
                print("-"*50)


        # Cuando se inserte el ultimo valor haga lo siguiente
        if self.number_of_column_to_insert == self.quantity_columns:

            # Reiniciar valores para que puedan volver a introducir registros
            self.label1.configure(text=f"Inserte valor de: {self.clean_row_list[1]}")
        

            # Agregamos los ultimos dos elementos de la lista (FECHA_PRESTAMO Y FECHA_REGRESO)
            self.list_of_column_to_insert_value.append(self.clean_row_list[-2])
            self.list_of_column_to_insert_value.append(self.clean_row_list[-1])

            # Obtener fecha al momento de prestarse
            self.date_at_lending = datetime.today().strftime('%Y-%m-%d')

            # Obtener fecha de regreso esperada (+3 dias)
            self.date = datetime.strptime(self.date_at_lending, "%Y-%m-%d")
            self.modified_date = self.date + timedelta(days=3)
            self.date_at_return = datetime.strftime(self.modified_date, "%Y-%m-%d")

            self.list_of_values_to_insert.append(self.date_at_lending)
            self.list_of_values_to_insert.append(self.date_at_return)

            print("*"*50)
            print(self.list_of_column_to_insert_value)
            print(self.list_of_values_to_insert)
            # print(self.list_of_column_to_insert_value)
            print(f"INSERT INTO tblPRESTAMOS ({str(self.list_of_column_to_insert_value[0])}, {str(self.list_of_column_to_insert_value[1])}, {str(self.list_of_column_to_insert_value[2])}, {str(self.list_of_column_to_insert_value[3])}, {str(self.list_of_column_to_insert_value[4])}, {str(self.list_of_column_to_insert_value[5])}) VALUES ({str(self.list_of_values_to_insert[0])}, '{str(self.list_of_values_to_insert[1])}', '{str(self.list_of_values_to_insert[2])}', '{str(self.list_of_values_to_insert[3])}', '{str(self.list_of_values_to_insert[4])}', '{str(self.list_of_values_to_insert[5])}')")
            # print(f"INSERT INTO tblPRESTAMOS ({str(self.list_of_column_to_insert_value[0])}, {str(self.list_of_column_to_insert_value[1])}, {str(self.list_of_column_to_insert_value[2])}, {str(self.list_of_column_to_insert_value[3])}, {str(self.list_of_column_to_insert_value[4])}, {str(self.list_of_column_to_insert_value[5])}) VALUES ({str(self.list_of_values_to_insert[0])}, '{str(self.list_of_values_to_insert[1])}', '{str(self.list_of_values_to_insert[2])}', '{str(self.list_of_values_to_insert[3])}', '{str(self.list_of_values_to_insert[4])}', '{str(self.list_of_values_to_insert[5])}')")

            

            self.cursor.execute("SELECT TOP 1 ID_DEVOLUCION FROM tblDEVOLUCION ORDER BY ID_DEVOLUCION DESC;")
            self.value_returned = [row for row in self.cursor]
            x = self.value_returned[0][0] + 1

            self.values_devolution.append(x)

            self.cursor.execute(f"INSERT INTO tblPRESTAMOS ({str(self.list_of_column_to_insert_value[0])}, {str(self.list_of_column_to_insert_value[1])}, {str(self.list_of_column_to_insert_value[2])}, {str(self.list_of_column_to_insert_value[3])}, {str(self.list_of_column_to_insert_value[4])}, {str(self.list_of_column_to_insert_value[5])}) VALUES ({str(self.list_of_values_to_insert[0])}, '{str(self.list_of_values_to_insert[1])}', '{str(self.list_of_values_to_insert[2])}', '{str(self.list_of_values_to_insert[3])}', '{str(self.list_of_values_to_insert[4])}', '{str(self.list_of_values_to_insert[5])}')")
            self.cursor.commit()

            # Creamos un registro de devolucion para este prestamo
            print(f"INSERT INTO tblDEVOLUCION (ID_DEVOLUCION, ID_PRESTAMO, ID_USUARIO, FECHA_DEVOLUCION, ESTADO) VALUES ({self.values_devolution[0]}, {int(self.list_of_values_to_insert[0])}, {int(self.list_of_values_to_insert[2])}, 'DEFAULT', 'Pendiente')")
            self.cursor.execute(f"INSERT INTO tblDEVOLUCION (ID_DEVOLUCION, ID_PRESTAMO, ID_USUARIO, FECHA_DEVOLUCION, ESTADO) VALUES ({self.values_devolution[0]}, {int(self.list_of_values_to_insert[0])}, {int(self.list_of_values_to_insert[2])}, 'None', 'PENDIENTE')")
            self.cursor.commit()
            # Cuando se inserte el registro de autor, actualizamos el contenido en la misma ventana.
            self.text_box.delete(1.0, END)
            self.cursor.execute(f"SELECT * FROM tblPRESTAMOS")
            for column in self.cursor.description:
                self.text_box.insert(END, str(column[0]) + " | ")

            self.row_to_list = [row for row in self.cursor]

            for item in self.row_to_list:
                try:
                    self.text_box.insert(END, "\n"+str(item)) 
                except Exception as e:
                    print(str(e))
            
            # Reiniciar valores para que puedan volver a introducir registros
            self.list_of_column_to_insert_value = []
            self.list_of_values_to_insert = []
            self.number_of_column_to_insert = 1
            self.quantity_columns = len(self.clean_row_list) - 3
            self.contador = 1
            self.insert_value.delete(0, 'end')
            self.values_devolution = []

        else:
            self.number_of_column_to_insert += 1
            self.contador = self.contador + 1
            self.insert_value.delete(0, 'end')


    def new_id_lending(self):
        # Le asignamos el siguiente ID_PRESTAMO que este disponible
        self.cursor.execute("SELECT TOP 1 ID_PRESTAMO FROM tblPRESTAMOS ORDER BY ID_PRESTAMO DESC;")
        self.value_returned = [row for row in self.cursor]
        self.list_of_values_to_insert.append(self.value_returned[0][0] + 1)


class Devolucion:

    def __init__(self, master, cursor):
        self.cursor = cursor
        self.master = master
        self.frame = Frame(self.master)
        self.master.title("Devolucion")
        self.master.geometry("800x800")
        self.console = Console()

        self.label1 = Label(self.master, text="Insertar valor:")
        self.label1.pack()

        self.value_to_table = StringVar()
        self.insert_value = Entry(self.master, textvariable=self.value_to_table)
        self.insert_value.pack()

        self.execute_insert = Button(self.master, text="Aceptar", command=self.insert_value_query)#, self. )
        self.execute_insert.pack()
        
        global contador
        self.contador = 1

        self.number_of_column_to_insert = 1


        self.text_box = Text(self.master, width=500, height=500)
        self.text_box.pack()


        self.show_table()

    def show_table(self) -> str:
        self.text_box.delete(1.0, END)

        # Obtenemos el numero de columnas de la tabla a la que se desea agregar el registro para
        # cambiar dinamicamente el numero de widgets "Entry" (entrada texto) de acuerdo
        # a la tabla seleccionada
        self.cursor.execute("SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME LIKE 'tbl%'")
        self.row_to_list = [row for row in self.cursor]

        # Lista con el nombre de las puras tablas
        self.clean_row_list = [] 

        for x in self.row_to_list:
            for y in x:
                if re.search('tbl\w+', y):
                    self.clean_row_list.append(y)

        self.cursor.execute(f"SELECT * FROM tblDEVOLUCION WHERE ESTADO='Pendiente';")

        for column in self.cursor.description:
            self.text_box.insert(END, str(column[0]) + " | ")

        self.row_to_list = [row for row in self.cursor]
        if self.row_to_list != []:
            # self.row_to_list = [row for row in self.cursor]

            for item in self.row_to_list:
                try:
                    self.text_box.insert(END, "\n"+str(item)) 
                except Exception as e:
                    print(str(e))

        else:
            self.text_box.delete(1.0, END)
            self.cursor.execute(f"SELECT * FROM tblDEVOLUCION")
            for column in self.cursor.description:
                self.text_box.insert(END, str(column[0]) + " | ")

            self.row_to_list = [row for row in self.cursor]

            for item in self.row_to_list:
                try:
                    self.text_box.insert(END, "\n"+str(item)) 
                except Exception as e:
                    print(str(e))


        # Obtener nombres de columnas
        self.cursor.execute(f"SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'tblDEVOLUCION'")
        self.row_to_list = [row for row in self.cursor]
        self.clean_row_list = []
        for item in self.row_to_list:
            self.clean_row_list.append(item[3])
        
        # Numero de columnas
        global quantity_columns
        self.quantity_columns = len(self.clean_row_list) - 3 # ID_PRESTAMO, FECHA_PRESTAMO, FECHA REGRESO
        print(self.quantity_columns)
        # Almacenar la columna en la que se va a insertar el valor
        global list_of_column_to_insert_value
        self.list_of_column_to_insert_value = []
        self.list_of_column_to_insert_value.append("ID_DEVOLUCION")

        # Almacenan los valores a insertar en la tabla
        global list_of_values_to_insert
        self.list_of_values_to_insert = []

        self.label1.configure(text=f"Inserte {self.clean_row_list[1]} ")
        
    def insert_value_query(self):
        
        # ID_PRESTAMO -> self.value_to_table.get()

        # self.date_at_devolution = datetime.today().strftime('%Y-%m-%d')
        self.date_at_devolution = "2021-05-29"
        self.cursor.execute(f"UPDATE tblDEVOLUCION SET ESTADO='ENTREGADO' WHERE ID_PRESTAMO={self.value_to_table.get()}")  
        self.cursor.commit()

        self.cursor.execute(f"UPDATE tblDEVOLUCION SET FECHA_DEVOLUCION='{self.date_at_devolution}' WHERE ID_PRESTAMO={self.value_to_table.get()}")
        self.cursor.commit()


        # Actualizamos tabla
        self.text_box.delete(1.0, END)
        self.cursor.execute(f"SELECT * FROM tblDEVOLUCION")
        for column in self.cursor.description:
            self.text_box.insert(END, str(column[0]) + " | ")

        self.row_to_list = [row for row in self.cursor]

        for item in self.row_to_list:
            try:
                self.text_box.insert(END, "\n"+str(item)) 
            except Exception as e:
                print(str(e))


        self.cursor.execute(f"SELECT FECHA_PRESTAMO FROM tblPRESTAMOS WHERE ID_PRESTAMO={self.value_to_table.get()};")
        self.lending_date = []
        for item in self.cursor:
            self.lending_date.append(item)

        print("Fecha prestamo", self.lending_date[0][0])

        self.l_date = str(self.lending_date[0][0])
        self.lending_day = self.l_date[-2:]
        self.lending_month = self.l_date[5:7]
        self.lending_year = self.l_date[:4]

        print("Day", self.lending_day)
        print("Month", self.lending_month)
        print("Year", self.lending_year)

        self.cursor.execute(f"SELECT FECHA_DEVOLUCION FROM tblDEVOLUCION WHERE ID_PRESTAMO={self.value_to_table.get()};")
        self.devolution_date = []
        for item in self.cursor:
            self.devolution_date.append(item)

        print("Fecha devolucion", self.devolution_date[0][0])

        self.d_date = str(self.devolution_date[0][0])
        self.devolution_day = self.d_date[-2:]
        self.devolution_month = self.d_date[5:7]
        self.devolution_year = self.d_date[:4]

        print("Day", self.devolution_day)
        print("Month", self.devolution_month)
        print("Year", self.devolution_year)


        # Obtener cantidad de dias entre FECHA_PRESTAMO Y FECHA_DEVOLUCION
        self.d0 = date(int(self.lending_year), int(self.lending_month), int(self.lending_day))
        self.d1 = date(int(self.devolution_year), int(self.devolution_month), int(self.devolution_day))
        self.delta = self.d1 - self.d0
        print("Dias diferencia", self.delta.days)

        if int(self.delta.days) > 3:

            # GET ID_MULTA
            self.values_fine = []
            self.cursor.execute("SELECT TOP 1 ID_MULTA FROM tblMULTA ORDER BY ID_MULTA DESC;")
            self.values_fine = [row for row in self.cursor]

            # If no ID create one
            if self.values_fine == []:
                self.next_id = 20001
                self.values_fine.append(self.next_id + 1) 

            elif self.values_fine != []:
                self.x = self.values_fine[0][0] + 1
                self.values_fine.append(self.x)

            # Get ID_DEVOLUCION
            self.id_dev_value = []
            self.cursor.execute("SELECT TOP 1 ID_DEVOLUCION FROM tblDEVOLUCION ORDER BY ID_DEVOLUCION DESC;")
            self.id_dev_value = [row for row in self.cursor]
            self.id_dev = self.id_dev_value[0][0]

            # Get COSTO_MULTA
            self.amount_fine = int(self.delta.days) * 10

            # self.cursor.execute(f"INSERT INTO tblMULTA (ID_MULTAS, ID_DEVOLUCION, DIAS_RETRASO, COSTO_MULTA) VALUES ({self.values_fine[0][0]}, {self.id_dev_value[0][0]}, {self.delta}, {self.amount_fine})")
            self.cursor.execute(f"INSERT INTO tblMULTA (ID_MULTA, ID_DEVOLUCION, DIAS_RETRASO, COSTO_MULTA) VALUES ({self.values_fine[0]}, {self.id_dev}, {int(self.delta.days)}, {self.amount_fine})")

            self.values_fine = []
            self.id_dev_value = []

