import customtkinter as ctk

janela = ctk.CTk()  # a primeira janela
janela.title("Grid Test")  # configura o título da aplicação
janela.geometry("400x400")  # configura a dimensão inicial da aplicação
janela.minsize(200, 200)
janela.columnconfigure(0, weight=1)
# janela.rowconfigure(0, weight=1)

# Aula 22 - Grid
# Resolução com Responsividade TOTAL com o aplicativo ;
# rowspan / columnspan - configura o tamanho que o widget irá ocupar na coluna ou na linha ;

def btn_call():
    pass


btn = ctk.CTkButton(janela, text="Botão 1".upper(), command=btn_call, height=50)
btn.grid(row=0, column=0, pady=20, padx=20, sticky="EW", columnspan=2)
btn2 = ctk.CTkButton(janela, text="Botão 2".upper(), command=btn_call, height=50)
btn2.grid(row=1, column=0, pady=(0, 20), padx=20, sticky="EW", columnspan=2)

check1 = ctk.CTkCheckBox(janela, text="Checkbox 1")
check1.grid(row=2, column=0)
check2 = ctk.CTkCheckBox(janela, text="Checkbox 2")
check2.grid(row=2, column=1)
janela.mainloop()  # rodando o programa em loop
