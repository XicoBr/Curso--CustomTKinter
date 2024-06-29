import customtkinter as ctk

janela = ctk.CTk()  # a primeira janela
janela.title("APP TESTE")  # configura o título da aplicação
janela.geometry("700x400")  # configura a dimensão inicial da aplicação
janela._set_appearance_mode("dark")


# Aula 08 - CAIXA DE DIÁLOGO(dialog)
# usado quando o sistema pede alguma informação do usuário, que será manipulada
# necessita de uma função para funcionar


def abrir():
    dialog = ctk.CTkInputDialog(title="Caixa de Diálogo(func)", text="Digite sua Credencial:",
                                button_fg_color="orange", button_text_color="black", button_hover_color="purple",
                                entry_border_color="purple", entry_fg_color="green")
    dialog_value = dialog.get_input()  # printa no terminal o valor da variável com input
    print(f"Credencial: {dialog_value}")



btn = ctk.CTkButton(master=janela, text="Abrir Caixa de Diálogo", command=abrir)
btn.pack(padx=20, pady=20)


janela.mainloop()  # rodando o programa em loop
