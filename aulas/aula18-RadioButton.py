import customtkinter as ctk

janela = ctk.CTk()  # a primeira janela
janela.title("APP TESTE")  # configura o título da aplicação
janela.geometry("700x400")  # configura a dimensão inicial da aplicação


# Aula 18 - RadioButton
radio_var = ctk.IntVar(value=0)  # nenhum valor selecionado inicialmente


def radio_event():
    valor = radio_var.get()
    if valor == 1:
        print("Sexo Masculino")
    else:
        print("Sexo Feminino")


radio1 = ctk.CTkRadioButton(janela, text="Masculino", command=radio_event, variable=radio_var, value=1)
radio2 = ctk.CTkRadioButton(janela, text="Feminino", command=radio_event, variable=radio_var, value=2)
radio1.pack(pady=10)
radio2.pack(pady=10)
janela.mainloop()  # rodando o programa em loop
