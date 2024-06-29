import customtkinter as ctk

janela = ctk.CTk()  # a primeira janela
janela.title("APP TESTE")  # configura o título da aplicação
janela.geometry("700x400")  # configura a dimensão inicial da aplicação
janela._set_appearance_mode("dark")


# Aula 06 - TabView(abas)
tabview = ctk.CTkTabview(master=janela, width=300, height=250, corner_radius=10, fg_color="teal", border_color="white",
                         border_width=2, text_color="green", segmented_button_selected_hover_color="red",
                         segmented_button_unselected_hover_color="pink", segmented_button_fg_color="purple",
                         segmented_button_selected_color="yellow", segmented_button_unselected_color="white")
tabview.pack()  # pack = centraliza o elemento
tabview.add("Nome")
tabview.add("Idade")
tabview.add("Genero")
tabview.tab("Nome").grid_columnconfigure(0, weight=1)  # centralizando na largura da tela
tabview.tab("Idade").grid_columnconfigure(0, weight=1)
tabview.tab("Genero").grid_columnconfigure(0, weight=1)

# Adicionando elementos nas abas
# para adicionar, usamos o ctklabel, ficando assim: customtkinter.CTkLabel(master=nome_da_variavel.tab("nome_aba"),
#                                                                          text="informações a serem passadas")
text_name = ctk.CTkLabel(master=tabview.tab("Nome"), text="Joaozinho Desgraça\nChayenne Rodrigues\nCleyton Rasta",
                         text_color="black")  # text é onde colocamos as informações da tabela
text_name.pack()

text_idade = ctk.CTkLabel(master=tabview.tab("Idade"), text="24 anos\n33 anos\n40 anos")
text_idade.pack()

text_genero = ctk.CTkLabel(master=tabview.tab("Genero"), text="Masculino\nFeminino\nMasculino")
text_genero.pack()

janela.mainloop()  # rodando o programa em loop
