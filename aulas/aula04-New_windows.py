import customtkinter as ctk
# ao invés de utilizarmos customtkinter toda vez, utilizamos um atalho para isso


janela = ctk.CTk()  # a primeira janela
janela.title("APP TESTE")  # configura o título da aplicação
janela.geometry("700x400")  # configura a dimensão inicial da aplicação

# Aula 04 - Criando novas janelas
def nova_tela():
    nova_janela = ctk.CTkToplevel(janela, fg_color="teal")  #Toplevel cria uma nova janela, recebendo como argumento
    # a janela em que estará situada(?) |fg_color = foreground color = cor do primeiro plano
    nova_janela.geometry("200x200")


btn_nova_tela = ctk.CTkButton(master=janela, text="Abrir nova Janela", command=nova_tela).place(x=300, y=100)
janela.mainloop()  # rodando o programa em loop
