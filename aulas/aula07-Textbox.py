import customtkinter as ctk

janela = ctk.CTk()  # a primeira janela
janela.title("APP TESTE")  # configura o título da aplicação
janela.geometry("700x400")  # configura a dimensão inicial da aplicação
janela._set_appearance_mode("dark")


# Aula 07 - CAIXA DE TEXTO(textbox)
textbox = ctk.CTkTextbox(master=janela, width=350, height=350, scrollbar_button_color="#4000bf",
                         activate_scrollbars=True, scrollbar_button_hover_color="#660099", border_color="#660099",
                         border_width=3, corner_radius=10, fg_color="#ba8c2e", border_spacing=5)
# border_spacing = padding de html


textbox.pack()
textbox.insert("0.0", "Título do seu texto\n\n" + ("Olá mundo, vamos programar interface gráfica usando  "
                                                   "CustomTKinter\n\n" * 20))
# insert(pos, child, **kw)
# Inserts a pane at the specified position.pos is either the string “end”, an integer index, or the name of a
# managed child. If is already managed by the notebook, moves it to the specified position.


janela.mainloop()  # rodando o programa em loop
