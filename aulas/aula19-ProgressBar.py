import customtkinter as ctk

janela = ctk.CTk()  # a primeira janela
janela.title("APP TESTE")  # configura o título da aplicação
janela.geometry("700x400")  # configura a dimensão inicial da aplicação


# Aula 19 - Progress Bar
# Usada para controlar a execução de algo, download de arquivos, chamada ou leitura de algo etc


progressbar = ctk.CTkProgressBar(janela, width=300, height=30, corner_radius=30, progress_color="purple")
progressbar.pack(pady=10)
progressbar.start()
progressbar.set()

#progressbar.stop()

janela.mainloop()  # rodando o programa em loop
