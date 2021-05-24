# import pyodbc

# try:
#     connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
#                                         'SERVER=localhost;'
#                                         'DATABASE=dbBiblioteca;'
#                                         'Trusted_Connection=yes;')
#     cursor = connection.cursor()
#     cursor.execute('SELECT * FROM dbBiblioteca.dbo.catCATEGORIA_USUARIO')
#     for row in cursor:
#         print(row)

# except pyodbc.Error as e:
#     print(str(e))
#     # cursor = connection.cursor()
#     # cursor.execute('SELECT * FROM dbBiblioteca.dbo.tblLIBRO')

#     # for row in cursor:
#     #     print(row)

from tkinter import *


def get_variable_value():
    valueresult.set( strlname.get() + ' ' + strfname.get() ) #assign val variable to other
    print(valueresult.get()) #if you want see the result in the console



root = Tk()

strfname = StringVar()
strlname = StringVar()
valueresult = StringVar()

labelf = Label(root, text = 'First Name').pack()
fname = Entry(root, justify='left', textvariable = strfname).pack() #strlname get input 

labell = Label(root, text = 'Last Name').pack()
lname = Entry(root, justify='left', textvariable = strlname).pack() #strfname get input 

button = Button(root, text='Show', command=get_variable_value).pack()
res = Entry(root, justify='left', textvariable = valueresult).pack() #only to show result

print(valueresult.get())
root.mainloop()