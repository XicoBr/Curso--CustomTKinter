import customtkinter as ctk


janela = ctk.CTk()  # a primeira janela
janela.title("APP TESTE")  # configura o título da aplicação
janela.geometry("700x400")  # configura a dimensão inicial da aplicação
janela._set_appearance_mode("dark")


def slider_value(value):

    if value == 0:
        slider.configure(fg_color="red")
    else:
        slider.configure(fg_color="yellow")
    print(int(value))


# Aula 14 - Slider
slider = ctk.CTkSlider(master=janela,
                       width=200,
                       from_=0,
                       to=100,
                       number_of_steps=50,  # total de passos dentro da barra de progresso(pega o final e divide pelos
                       # passos)
                       command=slider_value,
                       button_color="red",
                       button_hover_color="purple",
                       bg_color="blue",
                       height=20,
                       fg_color="yellow",
                       progress_color="darkorange",
                       corner_radius=10)
slider.pack(pady=30)

janela.mainloop()  # rodando o programa em loop
