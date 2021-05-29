import traceback
import tkinter as tk
from tkinter import messagebox
from tkinter import *


class Delete:
    def __init__(self, master, cursor):
        self.master = master
        self.cursor = cursor
        self.frame = Frame(self.master)
        self.master.title("Delete Window")
        self.master.geometry("600x600")


        self.label1 = Label(self.master, text="Tabla:")
        self.label1.pack()

        self.value_to_table = StringVar()
        self.insert_value = Entry(self.master, textvariable=self.value_to_table)
        self.insert_value.pack()

        self.users_button = Button(self.master, text="Aceptar", command=self.modify_actions, state='disabled')
        self.users_button.pack()

        self.value_to_table.trace("w", self.validate1)

        
        self.label1 = Label(self.master, text="ID:")
        self.label1.pack()

        self.value_of_id = StringVar()
        self.insert_value_id = Entry(self.master, textvariable=self.value_of_id)
        self.insert_value_id.pack()

        self.value_of_id.trace("w", self.validate)

        self.id_button = Button(self.master, text="Aceptar", command=self.insert_value_modify, state="disabled")
        self.id_button.pack()

        self.text_box = Text(self.master, width=500, height=500)
        self.text_box.pack()

        self.clean_row_list = [ "LIBRO", "AUTOR", "USUARIO", "DONACION", "EMPLEADOS"]

        self.text_box.insert(END, "Tablas:\n")
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
            
            elif self.value_with_tbl == "tblEMPLEADOS":
                print("Es empleado")
                self.text_box.delete(1.0, END)

                self.cursor.execute(f"SELECT * FROM tblEMPLEADOS")
                for column in self.cursor.description:
                    self.text_box.insert(END, str(column[0]) + " | ")

                self.row_to_list = [row for row in self.cursor]

                for item in self.row_to_list:
                    try:
                        self.text_box.insert(END, "\n"+str(item)) 
                    except Exception as e:
                        print(str(e))
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
                
                if int(self.value_of_id.get()) in self.clean_x:
                    print("Se encuentra el valor en tabla")
                    print(self.value_of_id.get())
                
                else:
                    raise Exception

                self.cursor.execute(f"DELETE FROM tblAUTOR WHERE ID_AUTOR={self.value_of_id.get()}")
                self.cursor.commit()


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
                print("entro autor")

                self.cursor.execute("SELECT ID_LIBRO FROM tblLIBRO")
                self.x = [row for row in self.cursor]
                self.clean_x = []

                for item in self.x:
                    self.clean_x.append(item[0])
                
                if int(self.value_of_id.get()) in self.clean_x:
                    print("Se encuentra el valor en tabla")
                    print(self.value_of_id.get())
                
                else:
                    raise Exception

                self.cursor.execute(f"DELETE FROM tblLIBRO WHERE ID_LIBRO={self.value_of_id.get()}")
                self.cursor.commit()


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


            elif self.value_with_tbl == "tblAUTOR":
                print("entro autor")

                self.cursor.execute("SELECT ID_AUTOR FROM tblAUTOR")
                self.x = [row for row in self.cursor]
                self.clean_x = []

                for item in self.x:
                    self.clean_x.append(item[0])
                
                if int(self.value_of_id.get()) in self.clean_x:
                    print("Se encuentra el valor en tabla")
                    print(self.value_of_id.get())
                
                else:
                    raise Exception

                self.cursor.execute(f"DELETE FROM tblAUTOR WHERE ID_AUTOR={self.value_of_id.get()}")
                self.cursor.commit()


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


            elif self.value_with_tbl == "tblUSUARIO":
                print("entro autor")

                self.cursor.execute("SELECT ID_USUARIO FROM tblUSUARIO")
                self.x = [row for row in self.cursor]
                self.clean_x = []

                for item in self.x:
                    self.clean_x.append(item[0])
                
                if int(self.value_of_id.get()) in self.clean_x:
                    print("Se encuentra el valor en tabla")
                    print(self.value_of_id.get())
                
                else:
                    raise Exception

                self.cursor.execute(f"DELETE FROM tblUSUARIO WHERE ID_USUARIO={self.value_of_id.get()}")
                self.cursor.commit()


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
                print("entro donacion")

                self.cursor.execute("SELECT ID_DONACION FROM tblDONACION")
                self.x = [row for row in self.cursor]
                self.clean_x = []

                for item in self.x:
                    self.clean_x.append(item[0])
                
                if int(self.value_of_id.get()) in self.clean_x:
                    print("Se encuentra el valor en tabla")
                    print(self.value_of_id.get())
                
                else:
                    raise Exception

                self.cursor.execute(f"DELETE FROM tblDONACION WHERE ID_DONACION={self.value_of_id.get()}")
                self.cursor.commit()


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


            elif self.value_with_tbl == "tblEMPLEADOS":
                print("entro autor")

                self.cursor.execute("SELECT ID_EMPLEADO FROM tblEMPLEADOS")
                self.x = [row for row in self.cursor]
                self.clean_x = []

                for item in self.x:
                    self.clean_x.append(item[0])
                
                if int(self.value_of_id.get()) in self.clean_x:
                    print("Se encuentra el valor en tabla")
                    print(self.value_of_id.get())
                
                else:
                    raise Exception

                self.cursor.execute(f"DELETE FROM tblEMPLEADOS WHERE ID_EMPLEADO={self.value_of_id.get()}")
                self.cursor.commit()


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


            else:
                raise Exception
               

        except:
            messagebox.showinfo(message=f"Valor no valido")
            # print(traceback.format_exc())
            self.insert_value.delete(0, 'end')
            self.insert_value_id.delete(0, 'end')

    def validate(self, *args):

        self.ones = []
        if self.value_of_id.get():
            # self.id_button.config(state="normal")
            self.ones.append("1")


        if len(self.ones) == 1:
            self.id_button.config(state="normal")
            self.ones = []

        else:
            self.id_button.config(state="disabled")


    def validate1(self, *args):

        self.ones1 = []
        if self.value_to_table.get():
            # self.id_button.config(state="normal")
            self.ones1.append("1")


        if len(self.ones1) == 1:
            self.users_button.config(state="normal")
            self.ones1 = []

        else:
            self.users_button.config(state="disabled")

