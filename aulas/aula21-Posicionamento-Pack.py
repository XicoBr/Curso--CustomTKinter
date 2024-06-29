import customtkinter as ctk

janela = ctk.CTk()  # a primeira janela
janela.title("Sistema de Login")  # configura o título da aplicação
janela.geometry("400x500")  # configura a dimensão inicial da aplicação
janela.columnconfigure(0, weight=1)  # configura todos os widgets centralizados
# janela.rowconfigure(0, weight=0)  # aqui, não necessita dessa configuração ;
janela.resizable(False, False)
# Aula 21 - Pack
mainframe = ctk.CTkFrame(janela, fg_color="#152B26")
mainframe.grid(column=0, row=0, sticky="N, S, E, W")
ctk.CTkLabel(mainframe,
             text="Faça Login",
             font=("arial", 40, "bold"),
             text_color="white").pack(pady=(10, 30))
ctk.CTkEntry(mainframe,
             placeholder_text="username",
             font=("arial", 20),
             width=250,
             height=45,
             fg_color="#12263A").pack(pady=10)
ctk.CTkEntry(mainframe,
             placeholder_text="password",
             font=("arial", 20),
             width=250,
             height=45,
             show="*",
             fg_color="#12263A").pack(pady=0)
ctk.CTkButton(mainframe,
              text="Log in".upper(),
              width=250,
              height=45,
              fg_color="#4A345D").pack(pady=30)
janela.mainloop()  # rodando o programa em loop
