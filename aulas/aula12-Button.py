import customtkinter as ctk
from PIL import Image

# Utilizar a biblioteca PIL para carregar imagens
janela = ctk.CTk()  # a primeira janela
janela.title("APP TESTE")  # configura o título da aplicação
janela.geometry("700x400")  # configura a dimensão inicial da aplicação
janela._set_appearance_mode("dark")


img = ctk.CTkImage(light_image=Image.open("./limões.png"), dark_image=Image.open("./limões.png"), size=(40, 40))
# p/ adicionar imagens, utilizar o comando customtkinter.CTkImage(light/dark_image=Image.open(
#                                                                 "endereço_da_imagem.extensão"), size=(width, height))


def evento():
    frase = 'Botão clicado'
    label_text.configure(text=str(frase))
    pass


# Aula 12 - Botões
btn = ctk.CTkButton(janela,
                    text="Clicar no botão",
                    command=evento,
                    height=50,
                    width=200,
                    fg_color="white",
                    hover_color="green",
                    text_color="red",
                    font=("arial italic", 20),
                    bg_color="transparent",
                    border_color="blue",
                    border_width=2,
                    border_spacing=2,
                    corner_radius=100,
                    state="normal",
                    image=img)  # botão recebendo a imagem passada acima
btn.pack(pady=(20, 5))
label_text = ctk.CTkLabel(janela, text="", width=200)
label_text.pack()
janela.mainloop()  # rodando o programa em loop
