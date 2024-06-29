import customtkinter as ctk
# ao invés de utilizarmos customtkinter toda vez, utilizamos um atalho para isso


janela = ctk.CTk()  # a primeira janela

# Aula 02 - configurando a janela principal
janela.title("APP TESTE")  # configura o título da aplicação
janela._set_appearance_mode("light")  # seleciona o modo claro da janela
janela.geometry("400x200")  # configura a dimensão inicial da aplicação
janela.maxsize(500, 300)  # configura a dimensão máxima da aplicação
janela.minsize(300, 200)  # configura a dimensão mínima da aplicação
janela.resizable(False, False)  # permite que o dev trave ou não a dimensão da aplição, não permitindo a alteração da
# mesma pelo usuário >> False=trava a dimensão
janela.iconify()  # fecha a aplicação
janela.deiconify()  # abre a janela de aplicação
janela.mainloop()  # rodando o programa em loop
