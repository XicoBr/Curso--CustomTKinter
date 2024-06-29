import customtkinter as ctk

janela = ctk.CTk()  # a primeira janela
janela.title("APP TESTE")  # configura o título da aplicação
janela.geometry("700x400")  # configura a dimensão inicial da aplicação


# Aula 20 - Posicionamento .place
# funciona através do posicionamento dos eixos X e Y ;
# para dar meia responsividade ao aplicativo, usa-se o relx e rely, que adequará o tamanho dos widgets de acordo com a
# dimensão da aplicação ;


ctk.CTkButton(janela, text="Botao 1", width=140).place(x=0, y=0)  # largura padrão de botão = 140px
ctk.CTkButton(janela, text="Botao 2", round_width_to_even_numbers=True).place(x=150, y=0)
ctk.CTkButton(janela, text="Botao 3", width=140).place(relx=0.1, rely=0.1)  # relx = posicionamento em relação à
# dimensão da tela
ctk.CTkButton(janela, text="Botao 4", width=140).place(x=70, rely=0.3)
janela.mainloop()  # rodando o programa em loop
