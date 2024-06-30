import customtkinter as ctk
from tkinter import *
import database

app = ctk.CTk()
app.geometry("900x600")
app.resizable(False, False)
main_frame = ctk.CTkFrame(app, fg_color="#716969", width=900, height=600)
main_frame.grid(column=0, row=0)
#main_frame.grid_columnconfigure(0, weight=1)
#main_frame.grid_rowconfigure(0, weight=1)

button_frame = ctk.CTkFrame(main_frame, fg_color="#BCABAE", height=300)
button_frame.grid(column=0, row=0)

table_frame = ctk.CTkFrame(main_frame, fg_color="blue", width=800, height=600)
# table_frame.place(x=200, y=0)
table_frame.grid(column=1, row=0, columnspan=4, rowspan=4)


def importar_tab():
    pass
    cursor = database.conection_var.cursor()
    database.cursor.execute("SELECT * FROM users")
    dados = database.cursor.fetchall()
    result_label = database.cursor.fetchall().get()
    cursor.close()


import_button = ctk.CTkButton(button_frame, text="Importar tabela", command=importar_tab)
import_button.grid(column=0, row=0)
delete_button1 = ctk.CTkButton(button_frame, text="Excluir")
delete_button1.grid(column=0, row=1, pady=10)

result_label = ctk.CTkLabel(table_frame, text="", fg_color="purple", width=800, height=600)
result_label.place(x=0, y=0)
app.mainloop()
