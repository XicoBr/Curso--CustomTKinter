import customtkinter as ctk

janela = ctk.CTk()  # a primeira janela
janela.title("APP TESTE")  # configura o título da aplicação
janela.geometry("700x400")  # configura a dimensão inicial da aplicação
janela._set_appearance_mode("dark")


# Aula 10 - Label
# Funciona como linha única, diferentemente da caixa de texto
ctk.CTkLabel(janela, text="Aula 10 - Labels", font=("arial", 40)).pack(pady=20)
ctk.CTkLabel(janela, text="Este texto é estático de um Label").pack()

# Trabalhando com Label Dinâmico:
# 1 - Introduzindo texto por Input
#
# text_var = ctk.StringVar(value=input("Digite o seu nome: "))  # define uma variável string, que é dinâmica. Não é
# # recomendado, pois para passar o valor p/ a variável, utiliza-se o terminal, algo que o usuário não deve ter acesso
#
# lab = ctk.CTkLabel(janela,
#                    textvariable=text_var,
#                    width=200,
#                    height=25,
#                    text_color="purple",
#                    font=("arial bold", 16))
# lab.pack(pady=10)


# 2 - Introduzindo texto por Entry (forma mais prática)


def enviar():
    frase = entry.get()
    lab.configure(text=str(frase))  # puxa a string digitada e coloca dentro da janela do programa, não aparecendo
    # mais no terminal


lab = ctk.CTkLabel(janela,
                   text="",  # deixar vazio para receber a string dinâmica
                   width=200,
                   height=25,
                   text_color="black",
                   font=("arial bold", 20),
                   fg_color="cyan",  # fg_color no padrão é transparente
                   corner_radius=10)
lab.pack(pady=10)

entry = ctk.CTkEntry(master=janela, width=200)
entry.pack(pady=20)

ctk.CTkButton(janela, width=200, text="Enviar", command=enviar).pack(pady=10)

janela.mainloop()  # rodando o programa em loop
