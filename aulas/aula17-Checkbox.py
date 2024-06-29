import customtkinter as ctk

janela = ctk.CTk()  # a primeira janela
janela.title("APP TESTE")  # configura o título da aplicação
janela.geometry("700x400")  # configura a dimensão inicial da aplicação


# Aula 17 - Checkbox
ctk.CTkLabel(janela, text="Aula - Checkbox", font=("Arial", 20)).pack(pady=(20, 10))


check_var = ctk.StringVar(value="on")  # define um valor inicial para a variable "check_var" dentro da variável
# "checkbox"


def check_value():
    if check_var.get() == "on":
        ctk.set_appearance_mode("dark")
        print("Modo escuro ativado")
    else:
        ctk.set_appearance_mode("light")
        print("Modo escuro desativado")



checkbox = ctk.CTkCheckBox(janela, text="Checa teste", variable=check_var, onvalue="on", offvalue="off", command=check_value)
checkbox.pack()

janela.mainloop()  # rodando o programa em loop
