import customtkinter as ctk


janela = ctk.CTk()  # a primeira janela
janela.title("APP TESTE")  # configura o título da aplicação
janela.geometry("700x400")  # configura a dimensão inicial da aplicação
janela._set_appearance_mode("dark")


def btn(value):

    print(f"Está no segmento: {value}")


segment = ctk.CTkSegmentedButton(janela,
                                 values=["Tkinter", "Django", "Flask"],
                                 command=btn)
segment.pack(pady=20)
segment.set("Flask")  # configura a aba que estará selecionada ao iniciar o programa

janela.mainloop()  # rodando o programa em loop
