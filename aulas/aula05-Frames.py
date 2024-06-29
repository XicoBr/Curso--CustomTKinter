import customtkinter as ctk

janela = ctk.CTk()  # a primeira janela
janela.title("APP TESTE")  # configura o título da aplicação
janela.geometry("700x400")  # configura a dimensão inicial da aplicação
janela._set_appearance_mode("dark")

# Aula 05 - Frames
# Frame é um CONTAINER para outros widgets ;
# A própria janela principal(ou root window) é um frame ;
# Cada frame tem suas próprias dimensões de GRID, então o posicionamento por GRID dos widgets DENTRO de cada frame
# funciona de forma independente ;

frame1 = ctk.CTkFrame(master=janela, width=200, height=330, fg_color="blue", bg_color="transparent", border_width=10,
                      border_color="red", corner_radius=30).place(x=10, y=60)
frame2 = ctk.CTkFrame(janela, width=200, height=330, fg_color="#ffffff").place(x=230, y=60)
frame3 = ctk.CTkFrame(janela, width=200, height=330, fg_color="cyan").place(x=450, y=60)
janela.mainloop()  # rodando o programa em loop
