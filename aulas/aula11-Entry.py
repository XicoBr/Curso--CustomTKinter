import customtkinter as ctk
from tkinter import *

janela = ctk.CTk()  # a primeira janela
janela.title("APP TESTE")  # configura o título da aplicação
janela.geometry("700x400")  # configura a dimensão inicial da aplicação
janela._set_appearance_mode("dark")

# Aula 10 - Entry
# Serve para manipular


var_entry = ctk.CTkEntry(janela, width=300, placeholder_text="Digite seu nome completo")
var_entry.pack(pady=(20, 10))


def pegar():
    frase = var_entry.get()
    var_label.configure(text=str(frase))
    #print(var_entry.get())  # pega o texto da variável entry e printa na tela
    var_entry.delete(0, END)  # comando que apaga o texto digitado ao clicar no botão

# def apagar():
#     entry.delete(0, END)
#     pass


# Adiciona-se um botao para "pegar" a informação digitada pelo usuário
var_label = ctk.CTkLabel(janela,
                         width=200,
                         text="",
                         text_color="black",
                         fg_color="darkorange")
var_label.pack(pady=10)
ctk.CTkButton(master=janela, width=300, text="Pegar texto", command=pegar).pack()
#ctk.CTkButton(master=janela, width=300, text="Apagar texto", command=apagar).pack(pady=5)
janela.mainloop()  # rodando o programa em loop
