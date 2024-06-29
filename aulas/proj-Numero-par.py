

import customtkinter as ctk
from tkinter import *
# ao invés de utilizarmos customtkinter toda vez, utilizamos um atalho para isso


def par_check():
    numero = entrada.get()  # necessário formatar a string em int, para transformar em número inteiro
    entrada.delete(0, END)
    if numero.isnumeric():
        numero = int(numero)  # conversão necessária para funcionar
        if numero % 2 == 0:
            label_result.configure(text=f"O número {numero} é par.")
        else:
            label_result.configure(text=f'O número {numero} não é par.')
    else:
        label_result.configure(text=f"Valor inválido! Digite um número inteiro!")


janela = ctk.CTk()  # a primeira janela
janela.columnconfigure(0, weight=1)
janela.rowconfigure(0, weight=1)
janela.resizable(False, False)
mainframe = ctk.CTkFrame(janela, fg_color="#E8FFB7")
mainframe.grid(column=0, row=0, sticky="N, W, E, S")  # coloca como plano de fundo o próprio frame, com o parâmetro
# "sticky"
janela.title("Contador de PAR")  # configura o título da aplicação
janela.geometry("600x400")  # configura a dimensão inicial da aplicação
ctk.CTkLabel(mainframe, text="CONTADOR DE PARES",
             font=("Helvetica Bold", 30), text_color="#090C9B",
             fg_color="#D0E1AC", text_color_disabled="red",
             bg_color="transparent", corner_radius=10).pack(pady=(20, 10))
label_result = ctk.CTkLabel(mainframe,
                            width=230,
                            bg_color="transparent",
                            fg_color="transparent",
                            text="",
                            text_color="black",
                            font=("Arial", 25))
label_result.pack(pady=(15, 5))
entrada = ctk.CTkEntry(mainframe, width=300, placeholder_text="digite um número inteiro")
entrada.pack()

btn = ctk.CTkButton(mainframe, text="CALCULAR", command=par_check, width=300)
btn.pack(pady=5)

janela.mainloop()  # rodando o programa em loop
