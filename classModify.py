import traceback
import tkinter as tk
from tkinter import messagebox
import re
from tkinter import *
from rich.console import Console
from rich import style, text
from datetime import datetime, timedelta, date
import time

class Modify:
    def __init__(self, master, cursor):
        self.master = master
        self.cursor = cursor
        self.frame = Frame(self.master)
        self.master.title("Modify Window")
        self.master.geometry("600x600")


        self.label1 = Label(self.master, text="Tabla por modificar:")
        self.label1.pack()

        self.value_to_table = StringVar()
        self.insert_value = Entry(self.master, textvariable=self.value_to_table)
        self.insert_value.pack()

        self.users_button = Button(self.master, text="Aceptar", command=self.modify_actions)
        self.users_button.pack()
        
        self.label1 = Label(self.master, text="ID:")
        self.label1.pack()

        self.value_of_id = StringVar()
        self.insert_value_id = Entry(self.master, textvariable=self.value_of_id)
        self.insert_value_id.pack()

        self.value_of_id.trace("w", self.validate)
        
        self.label2 = Label(self.master, text="Columna:")
        self.label2.pack()

        self.value_of_column = StringVar()
        self.insert_value_column = Entry(self.master, textvariable=self.value_of_column)
        self.insert_value_column.pack()

        self.value_of_column.trace("w", self.validate)


        self.label3 = Label(self.master, text="Valor a insertar:")
        self.label3.pack()

        self.value_to_insert = StringVar()
        self.value_entry = Entry(self.master, textvariable=self.value_to_insert)
        self.value_entry.pack()

        self.value_to_insert.trace("w", self.validate)


        self.id_button = Button(self.master, text="Aceptar", command=self.insert_value_modify, state="disabled")
        self.id_button.pack()

        self.text_box = Text(self.master, width=500, height=500)
        self.text_box.pack()

        self.cursor.execute("SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME LIKE 'tbl%'")
        self.row_to_list = [row for row in self.cursor]


        # Mostramos tablas para que el usuario vea cuales estan disponibles.
        # self.clean_row_list = [] 
        # for x in self.row_to_list:
        #     for y in x:
        #         if re.search('tbl\w+', y):
        #             self.clean_row_list.append(y)

        self.clean_row_list = [ "LIBRO", "AUTOR", "USUARIO", "DONACION"]

        self.text_box.insert(END, "Tablas a modificar:\n")
        for item in self.clean_row_list:
            self.text_box.insert(END, "\t"+item+"\n")




    def modify_actions(self):
        try:
            print("tbl"+self.value_to_table.get())

            self.v = self.value_to_table.get()

            self.upper_case = self.v.upper()

            self.value_with_tbl = "tbl"+self.upper_case
            
            if self.value_to_table.get() == "":
                raise Exception


            # Mostrar tabla autor
            if self.value_with_tbl == "tblAUTOR":
                print("Es autor")
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


            elif self.value_with_tbl == "tblLIBRO":
                print("Es libro")
                self.text_box.delete(1.0, END)

                self.cursor.execute(f"SELECT * FROM tblLIBRO")
                for column in self.cursor.description:
                    self.text_box.insert(END, str(column[0]) + " | ")

                self.row_to_list = [row for row in self.cursor]

                for item in self.row_to_list:
                    try:
                        self.text_box.insert(END, "\n"+str(item)) 
                    except Exception as e:
                        print(str(e))


            elif self.value_with_tbl == "tblUSUARIO":
                print("Es usuario")
                self.text_box.delete(1.0, END)

                self.cursor.execute(f"SELECT * FROM tblUSUARIO")
                for column in self.cursor.description:
                    self.text_box.insert(END, str(column[0]) + " | ")

                self.row_to_list = [row for row in self.cursor]

                for item in self.row_to_list:
                    try:
                        self.text_box.insert(END, "\n"+str(item)) 
                    except Exception as e:
                        print(str(e)) 


            elif self.value_with_tbl == "tblDONACION":
                print("Es usuario")
                self.text_box.delete(1.0, END)

                self.cursor.execute(f"SELECT * FROM tblDONACION")
                for column in self.cursor.description:
                    self.text_box.insert(END, str(column[0]) + " | ")

                self.row_to_list = [row for row in self.cursor]

                for item in self.row_to_list:
                    try:
                        self.text_box.insert(END, "\n"+str(item)) 
                    except Exception as e:
                        print(str(e))
            

            # elif self.value_with_tbl == "tblPRESTAMO":
            #     print("Es prestamo")
            #     self.text_box.delete(1.0, END)

            #     self.cursor.execute(f"SELECT * FROM tblPRESTAMO")
            #     for column in self.cursor.description:
            #         self.text_box.insert(END, str(column[0]) + " | ")

            #     self.row_to_list = [row for row in self.cursor]

            #     for item in self.row_to_list:
            #         try:
            #             self.text_box.insert(END, "\n"+str(item)) 
            #         except Exception as e:
            #             print(str(e))

            else:
                raise Exception

            



        except:
            messagebox.showinfo(message=f"Valor no valido")
            # print(traceback.format_exc())


    def insert_value_modify(self):
        self.insert_value.delete(0, 'end')
        print("entro")


        try:
            '''
            AUTOR
            '''

            if self.value_with_tbl == "tblAUTOR":
                print("entro autor")

                self.cursor.execute("SELECT ID_AUTOR FROM tblAUTOR")
                self.x = [row for row in self.cursor]
                self.clean_x = []

                for item in self.x:
                    self.clean_x.append(item[0])
                
                if int(self.insert_value_id.get()) in self.clean_x:
                    print("Se encuentra el valor en tabla")
                
                else:
                    raise Exception

                # Obtener nombres de columnas
                self.cursor.execute(f"SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'tblAUTOR'")
                self.row_to_list = [row for row in self.cursor]
                self.clean_row_list = []
                for item in self.row_to_list:
                    self.clean_row_list.append(item[3])

                print(self.clean_row_list)

                self.column = self.value_of_column.get()
                self.upper_column = self.column.upper()

                try:
                    if self.upper_column in self.clean_row_list:
                        print("si se encuentra la columna")
                        print(self.upper_column)
                    
                    else:
                        print("No se encuentras")
                except Exception as e:
                    print(e)

                print(f"UPDATE tblAUTOR SET {self.upper_column}='{self.value_to_insert.get()}' WHERE ID_AUTOR={int(self.value_of_id.get())}")
                self.cursor.execute(f"UPDATE tblAUTOR SET {self.upper_column}='{self.value_to_insert.get()}' WHERE ID_AUTOR={int(self.value_of_id.get())}")
                self.cursor.commit()
                print(self.upper_column, self.value_to_insert.get(), self.value_of_id.get())


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

                if (self.value_to_table  == "") or (self.value_of_column == "") or (self.value_of_id == ""):
                    raise Exception




            '''
            LIBRO
            '''
            if self.value_with_tbl == "tblLIBRO":
                print("entro autor")

                self.cursor.execute("SELECT ID_LIBRO FROM tblLIBRO")
                self.x = [row for row in self.cursor]
                self.clean_x = []

                for item in self.x:
                    self.clean_x.append(item[0])
                
                if int(self.insert_value_id.get()) in self.clean_x:
                    print("Se encuentra el valor en tabla")
                
                else:
                    raise Exception

                # Obtener nombres de columnas
                self.cursor.execute(f"SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'tblLIBRO'")
                self.row_to_list = [row for row in self.cursor]
                self.clean_row_list = []
                for item in self.row_to_list:
                    self.clean_row_list.append(item[3])

                print(self.clean_row_list)

                self.column = self.value_of_column.get()
                self.upper_column = self.column.upper()

                try:
                    if self.upper_column in self.clean_row_list:
                        print("si se encuentra la columna")
                        print(self.upper_column)
                    
                    else:
                        print("No se encuentras")
                except Exception as e:
                    print(e)

                print(f"UPDATE tblLIBRO SET {self.upper_column}='{self.value_to_insert.get()}' WHERE ID_LIBRO={int(self.value_of_id.get())}")
                self.cursor.execute(f"UPDATE tblLIBRO SET {self.upper_column}='{self.value_to_insert.get()}' WHERE ID_LIBRO={int(self.value_of_id.get())}")
                self.cursor.commit()
                print(self.upper_column, self.value_to_insert.get(), self.value_of_id.get())


                self.text_box.delete(1.0, END)

                self.cursor.execute(f"SELECT * FROM tblLIBRO")
                for column in self.cursor.description:
                    self.text_box.insert(END, str(column[0]) + " | ")

                self.row_to_list = [row for row in self.cursor]

                for item in self.row_to_list:
                    try:
                        self.text_box.insert(END, "\n"+str(item)) 
                    except Exception as e:
                        print(str(e))

                if (self.value_to_table  == "") or (self.value_of_column == "") or (self.value_of_id == ""):
                    raise Exception


            # '''
            # Prestamos
            # '''
            # if self.value_with_tbl == "tblPRESTAMO":
            #     print("entro autor")

            #     self.cursor.execute("SELECT ID_PRESTAMO FROM tblPRESTAMO")
            #     self.x = [row for row in self.cursor]
            #     self.clean_x = []

            #     for item in self.x:
            #         self.clean_x.append(item[0])
                
            #     if int(self.insert_value_id.get()) in self.clean_x:
            #         print("Se encuentra el valor en tabla")
                
            #     else:
            #         raise Exception

            #     # Obtener nombres de columnas
            #     self.cursor.execute(f"SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'tblPRESTAMO'")
            #     self.row_to_list = [row for row in self.cursor]
            #     self.clean_row_list = []
            #     for item in self.row_to_list:
            #         self.clean_row_list.append(item[3])

            #     print(self.clean_row_list)

            #     self.column = self.value_of_column.get()
            #     self.upper_column = self.column.upper()

            #     try:
            #         if self.upper_column in self.clean_row_list:
            #             print("si se encuentra la columna")
            #             print(self.upper_column)
                    
            #         else:
            #             print("No se encuentras")
            #     except Exception as e:
            #         print(e)

            #     print(f"UPDATE tblPRESTAMO SET {self.upper_column}='{self.value_to_insert.get()}' WHERE ID_PRESTAMO={int(self.value_of_id.get())}")
            #     self.cursor.execute(f"UPDATE tblPRESTAMO SET {self.upper_column}='{self.value_to_insert.get()}' WHERE ID_PRESTAMO={int(self.value_of_id.get())}")
            #     self.cursor.commit()
            #     print(self.upper_column, self.value_to_insert.get(), self.value_of_id.get())


            #     self.text_box.delete(1.0, END)

            #     self.cursor.execute(f"SELECT * FROM tblPRESTAMO")
            #     for column in self.cursor.description:
            #         self.text_box.insert(END, str(column[0]) + " | ")

            #     self.row_to_list = [row for row in self.cursor]

            #     for item in self.row_to_list:
            #         try:
            #             self.text_box.insert(END, "\n"+str(item)) 
            #         except Exception as e:
            #             print(str(e)) 


            '''
            Usuarios
            '''

            if self.value_with_tbl == "tblUSUARIO":
                print("entro autor")

                self.cursor.execute("SELECT ID_USUARIO FROM tblUSUARIO")
                self.x = [row for row in self.cursor]
                self.clean_x = []

                for item in self.x:
                    self.clean_x.append(item[0])
                
                if int(self.insert_value_id.get()) in self.clean_x:
                    print("Se encuentra el valor en tabla")
                
                else:
                    raise Exception

                # Obtener nombres de columnas
                self.cursor.execute(f"SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'tblUSUARIO'")
                self.row_to_list = [row for row in self.cursor]
                self.clean_row_list = []
                for item in self.row_to_list:
                    self.clean_row_list.append(item[3])

                print(self.clean_row_list)

                self.column = self.value_of_column.get()
                self.upper_column = self.column.upper()

                try:
                    if self.upper_column in self.clean_row_list:
                        print("si se encuentra la columna")
                        print(self.upper_column)
                    
                    else:
                        print("No se encuentras")
                except Exception as e:
                    print(e)

                print(f"UPDATE tblUSUARIO SET {self.upper_column}='{self.value_to_insert.get()}' WHERE ID_USUARIO={int(self.value_of_id.get())}")
                self.cursor.execute(f"UPDATE tblUSUARIO SET {self.upper_column}='{self.value_to_insert.get()}' WHERE ID_USUARIO={int(self.value_of_id.get())}")
                self.cursor.commit()
                print(self.upper_column, self.value_to_insert.get(), self.value_of_id.get())


                self.text_box.delete(1.0, END)

                self.cursor.execute(f"SELECT * FROM tblUSUARIO")
                for column in self.cursor.description:
                    self.text_box.insert(END, str(column[0]) + " | ")

                self.row_to_list = [row for row in self.cursor]

                for item in self.row_to_list:
                    try:
                        self.text_box.insert(END, "\n"+str(item)) 
                    except Exception as e:
                        print(str(e))
                if (self.value_to_table  == "") or (self.value_of_column == "") or (self.value_of_id == ""):
                    raise Exception


            '''
            Donacion
            '''

            if self.value_with_tbl == "tblDONACION":
                print("entro autor")

                self.cursor.execute("SELECT ID_DONACION FROM tblDONACION")
                self.x = [row for row in self.cursor]
                self.clean_x = []

                for item in self.x:
                    self.clean_x.append(item[0])
                
                if int(self.insert_value_id.get()) in self.clean_x:
                    print("Se encuentra el valor en tabla")
                
                else:
                    raise Exception

                # Obtener nombres de columnas
                self.cursor.execute(f"SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'tblDONACION'")
                self.row_to_list = [row for row in self.cursor]
                self.clean_row_list = []
                for item in self.row_to_list:
                    self.clean_row_list.append(item[3])

                print(self.clean_row_list)

                self.column = self.value_of_column.get()
                self.upper_column = self.column.upper()

                try:
                    if self.upper_column in self.clean_row_list:
                        print("si se encuentra la columna")
                        print(self.upper_column)
                    
                    else:
                        print("No se encuentras")
                except Exception as e:
                    print(e)

                print(f"UPDATE tblDONACION SET {self.upper_column}='{self.value_to_insert.get()}' WHERE ID_DONACION={int(self.value_of_id.get())}")
                self.cursor.execute(f"UPDATE tblDONACION SET {self.upper_column}='{self.value_to_insert.get()}' WHERE ID_DONACION={int(self.value_of_id.get())}")
                self.cursor.commit()
                print(self.upper_column, self.value_to_insert.get(), self.value_of_id.get())


                self.text_box.delete(1.0, END)

                self.cursor.execute(f"SELECT * FROM tblDONACION")
                for column in self.cursor.description:
                    self.text_box.insert(END, str(column[0]) + " | ")

                self.row_to_list = [row for row in self.cursor]

                for item in self.row_to_list:
                    try:
                        self.text_box.insert(END, "\n"+str(item)) 
                    except Exception as e:
                        print(str(e))

                if (self.value_to_table  == "") or (self.value_of_column == "") or (self.value_of_id == ""):
                    raise Exception                       

   
        except:
            messagebox.showinfo(message=f"Valor no valido")
            # print(traceback.format_exc())
            self.value_of_id.delete(0, 'end')
            self.insert_value_column.delete(0, 'end')
            self.value_entry.delete(0, 'end')


    def validate(self, *args):

        self.ones = []
        if self.value_of_id.get():
            # self.id_button.config(state="normal")
            self.ones.append("1")

        if self.value_of_column.get():
            self.ones.append("1")

        if self.value_to_insert.get():
            self.ones.append("1")

        if len(self.ones) == 3:
            self.id_button.config(state="normal")
            self.ones = []


#FIXME : VER FORMA DE HASTA QUE SE LLENEN PERMITIR PICARLE ACEPTAR

    def validate_column(self, *args):
        if self.value_of_column.get():
            print("Si hay valor")
            # self.id_button.config(state="normal")