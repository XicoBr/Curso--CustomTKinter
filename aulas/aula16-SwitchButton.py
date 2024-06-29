import customtkinter as ctk

janela = ctk.CTk()  # a primeira janela
janela.title("APP TESTE")  # configura o título da aplicação
janela.geometry("700x400")  # configura a dimensão inicial da aplicação


# Aula 16 - Switch


switch_var = ctk.StringVar(value="on")


def event():
    if switch_var.get() == "Ativo":
        ctk.set_appearance_mode("light")
    else:
        ctk.set_appearance_mode("dark")


switch = ctk.CTkSwitch(janela,
                       text=None,
                       command=event,
                       variable=switch_var,
                       onvalue="Ativo",
                       offvalue="Desativado")
switch.pack(pady=30)


janela.mainloop()  # rodando o programa em loop
