import customtkinter as ctk
# ao invés de utilizarmos customtkinter toda vez, utilizamos um atalho para isso


janela = ctk.CTk()  # a primeira janela
janela.title("APP TESTE")  # configura o título da aplicação
janela.geometry("400x200")  # configura a dimensão inicial da aplicação


# Aula 03 - mudando o tema da aplicação
# janela._set_appearance_mode("light")
# janela._set_appearance_mode("system")
# janela._set_appearance_mode("dark")
janela.mainloop()  # rodando o programa em loop
