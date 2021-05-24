# from testgui import *

import re
from tkinter import *
from rich.console import Console
from rich import style

class Add:

    # Este es el ejemplo inicial.
    
    def __init__(self, master, cursor):
        self.master = master
        self.cursor = cursor
        self.frame = Frame(self.master)
        self.master.title("Add Window")
        self.master.geometry("800x800")

        self.console = Console()

        self.label0 = Label(self.master, text="Insertar en tabla:")
        self.label0.pack()
        
        self.table_of_insert_data_value = StringVar()
        self.insert_register_to_table = Entry(self.master, textvariable=self.table_of_insert_data_value)
        self.insert_register_to_table.pack()

        self.test_button = Button(self.master, text="Aceptar", command=self.show_table)
        self.test_button.pack()

        self.label1 = Label(self.master, text="Insertar valor:")
        self.label1.pack()

        self.value_to_table = StringVar()
        self.insert_value = Entry(self.master, textvariable=self.value_to_table)
        self.insert_value.pack()

        self.execute_insert = Button(self.master, text="Aceptar", command=self.insert_value_query)#, self. )
        self.execute_insert.pack()

        self.null_button = Button(self.master, text="Sin Va lor", command=self.null_value)#, self. )
        self.null_button.pack()        

        self.text_box = Text(self.master, width=500, height=500)
        self.text_box.pack()

        global contador
        self.contador = 1

        self.number_of_column_to_insert = 1


    def show_table(self) -> None:
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

        if self.table_of_insert_data_value.get() in self.clean_row_list:

            if self.table_of_insert_data_value.get() == "tblAUTOR":


                self.cursor.execute(f"SELECT * FROM {self.table_of_insert_data_value.get()}")
                for column in self.cursor.description:
                    self.text_box.insert(END, str(column[0]) + " | ")

                self.row_to_list = [row for row in self.cursor]

                for item in self.row_to_list:
                    try:
                        self.text_box.insert(END, "\n"+str(item)) 
                    except Exception as e:
                        print(str(e))


                # Obtener nombres de columnas
                self.cursor.execute(f"SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'{str(self.table_of_insert_data_value.get())}'")
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
                self.cursor.execute("SELECT TOP 1 ID_AUTOR FROM tblAUTOR ORDER BY ID_AUTOR DESC;")
                self.value_returned = [row for row in self.cursor]
                self.list_of_values_to_insert.append(self.value_returned[0][0] + 1)

                self.label1.configure(text=f"Inserte valor de: {self.clean_row_list[1]}")               



            elif self.table_of_insert_data_value.get() == "tblPRESTAMOS":

                self.cursor.execute(f"SELECT * FROM {self.table_of_insert_data_value.get()}")
                for column in self.cursor.description:
                    self.text_box.insert(END, str(column[0]) + " | ")

                self.row_to_list = [row for row in self.cursor]

                for item in self.row_to_list:
                    try:
                        self.text_box.insert(END, "\n"+str(item)) 
                    except Exception as e:
                        print(str(e))

                # Obtener nombres de columnas
                self.cursor.execute(f"SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'{str(self.table_of_insert_data_value.get())}'")
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
                self.list_of_column_to_insert_value.append("ID_PRESTAMO")

                # Almacenan los valores a insertar en la tabla
                global list_of_values_to_insert
                self.list_of_values_to_insert = []

                # Le asignamos el siguiente ID_AUTOR que este disponible
                self.cursor.execute("SELECT TOP 1 ID_PRESTAMO FROM tblPRESTAMOS ORDER BY ID_PRESTAMO DESC;")
                self.value_returned = [row for row in self.cursor]
                self.list_of_values_to_insert.append(self.value_returned[0][0] + 1)
                print(self.list_of_values_to_insert)
                self.label1.configure(text=f"Inserte valor de: {self.clean_row_list[1]}")
            

            elif self.table_of_insert_data_value.get() == "tblUSUARIO":

                self.cursor.execute(f"SELECT * FROM {self.table_of_insert_data_value.get()}")
                for column in self.cursor.description:
                    self.text_box.insert(END, str(column[0]) + " | ")

                self.row_to_list = [row for row in self.cursor]

                for item in self.row_to_list:
                    try:
                        self.text_box.insert(END, "\n"+str(item)) 
                    except Exception as e:
                        print(str(e))
                
                    # Obtener nombres de columnas
                self.cursor.execute(f"SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'{str(self.table_of_insert_data_value.get())}'")
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
                self.list_of_column_to_insert_value.append("ID_USUARIO")

                # Almacenan los valores a insertar en la tabla
                global list_of_values_to_insert
                self.list_of_values_to_insert = []

                # Le asignamos el siguiente ID_AUTOR que este disponible
                self.cursor.execute("SELECT TOP 1 ID_USUARIO FROM tblUSUARIO ORDER BY ID_AUTOR DESC;")
                self.value_returned = [row for row in self.cursor]
                self.list_of_values_to_insert.append(self.value_returned[0][0] + 1)
                print(self.list_of_values_to_insert)

                self.label1.configure(text=f"Inserte valor de: {self.clean_row_list[1]}") 


                
        else:
            self.text_box.insert(END, "No esta")


    '''
    Autor
    '''

    def insert_value_query(self):

        if self.table_of_insert_data_value.get() == "tblAUTOR": 
            try:
                self.label1.configure(text=f"Inserte valor de: {self.clean_row_list[self.contador + 1]}")
                self.label1.update()
            except Exception as e:
                pass
            
            if self.number_of_column_to_insert <= self.quantity_columns:
                if self.contador <= self.quantity_columns:
                    self.list_of_column_to_insert_value.append(self.clean_row_list[self.contador])
                    self.list_of_values_to_insert.append(self.value_to_table.get())

                else:
                    print("Ya se paso")

                # Cuando se inserte el ultimo valor haga lo siguiente
                if self.number_of_column_to_insert == self.quantity_columns:

                    # Reiniciar valores para que puedan volver a introducir registros
                    self.contador = 0
                    self.number_of_column_to_insert = 1
                    self.label1.configure(text=f"Inserte valor de: {self.clean_row_list[1]}")

                    # En teoria quedaria si:
                    #   self.list_of_column_to_insert_value = ['ID_AUTOR', 'NOMBRE', 'APELLIDO_PAT', 'APELLIDO_MAT'] Esto no -> , 'DIA_PUBLICACION', 'MES_PUBLICACION', 'AÑO_PUBLICACION']
                    #   self.list_of_values_to_insert) = [valor0, valor1, valor2, valor3]  Esto no -> , valor4, valor5, valor6]

                    self.cursor.execute(f"INSERT INTO {str(self.table_of_insert_data_value.get())} ({str(self.list_of_column_to_insert_value[0])}, {str(self.list_of_column_to_insert_value[1])}, {str(self.list_of_column_to_insert_value[2])}, {str(self.list_of_column_to_insert_value[3])}) VALUES ({str(self.list_of_values_to_insert[0])}, '{str(self.list_of_values_to_insert[1])}', '{str(self.list_of_values_to_insert[2])}', '{str(self.list_of_values_to_insert[3])}')")
                    self.cursor.commit()
        
                    # Cuando se inserte el registro de autor, actualizamos el contenido en la misma ventana.
                    self.text_box.delete(1.0, END)
                    self.cursor.execute(f"SELECT * FROM {self.table_of_insert_data_value.get()}")
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
                            
            else:
                pass
            

            # FIXME: Mandar mensaje si se inserto el ultimo valor de la tabla
            # NOTE: No es necesario avisar ya que cuando se inserte el ultimo valor, se cambiara
            #       el nombre del Label por el de la primera columna.
            self.number_of_column_to_insert += 1
            self.contador = self.contador + 1
            self.insert_value.delete(0, 'end')


        elif self.table_of_insert_data_value.get() == "tblPRESTAMOS":
            # print(self.contador)
            self.label1.configure(text=f"Inserte valor de: {self.clean_row_list[self.contador + 1]}")
            self.label1.update()
            print(self.clean_row_list[self.contador + 1])
            
            if self.number_of_column_to_insert <= self.quantity_columns :
                if self.contador <= self.quantity_columns:
                    self.list_of_column_to_insert_value.append(self.clean_row_list[self.contador])
                    self.list_of_values_to_insert.append(self.value_to_table.get())
                    print("APPEND", self.clean_row_list[self.contador])

                else:
                    print("Ya se paso")

                # Cuando se inserte el ultimo valor haga lo siguiente
                if self.number_of_column_to_insert == self.quantity_columns:

                    # Reiniciar valores para que puedan volver a introducir registros
                    self.contador = 0
                    self.number_of_column_to_insert = 1
                    self.label1.configure(text=f"Inserte valor de: {self.clean_row_list[1]}")

                    # En teoria quedaria si:
                    #   self.list_of_column_to_insert_value = ['ID_AUTOR', 'NOMBRE', 'APELLIDO_PAT', 'APELLIDO_MAT'] Esto no -> , 'DIA_PUBLICACION', 'MES_PUBLICACION', 'AÑO_PUBLICACION']
                    #   self.list_of_values_to_insert) = [valor0, valor1, valor2, valor3]  Esto no -> , valor4, valor5, valor6]

                    # self.cursor.execute(f"INSERT INTO {str(self.table_of_insert_data_value.get())} ({str(self.list_of_column_to_insert_value[0])}, {str(self.list_of_column_to_insert_value[1])}, {str(self.list_of_column_to_insert_value[2])}, {str(self.list_of_column_to_insert_value[3])}) VALUES ({str(self.list_of_values_to_insert[0])}, '{str(self.list_of_values_to_insert[1])}', '{str(self.list_of_values_to_insert[2])}', '{str(self.list_of_values_to_insert[3])}')")
                    # self.cursor.commit()
        
                    # Cuando se inserte el registro de autor, actualizamos el contenido en la misma ventana.
                    self.text_box.delete(1.0, END)
                    self.cursor.execute(f"SELECT * FROM {self.table_of_insert_data_value.get()}")
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


            


    # Insertar "DEFAULT" como valor para dar valor nulo a columna dada 
    def null_value(self):
        # self.console.print(f"columna: {self.clean_row_list[self.contador]}", style="bold red")
        self.list_of_column_to_insert_value.append(self.clean_row_list[self.contador] )
        self.list_of_values_to_insert.append("DEFAULT")
        self.label1.configure(text=f"Inserte valor de: {self.clean_row_list[self.contador + 1]}")
        self.label1.update()

        self.number_of_column_to_insert += 1
        self.contador += 1

'''
DONACION
'''

    # def 