import customtkinter as ctk
from PIL import Image


# Utilizar o módulo PIL para carregar imagens
janela = ctk.CTk()  # a primeira janela
janela.title("APP TESTE")  # configura o título da aplicação
janela.geometry("700x400")  # configura a dimensão inicial da aplicação
janela._set_appearance_mode("dark")
ctk.CTkLabel(janela, text="AULA 13 - IMAGENS", font=("arial bold", 25)).pack(pady=(20, 10))

img1 = ctk.CTkImage(light_image=Image.open("./images/option-icon.png"), dark_image=Image.open(
    "./images/option-icon.png"), size=(30, 30))
ctk.CTkLabel(janela, text="", text_color="purple", image=img1, bg_color="orange").pack()


# p/ adicionar imagens, utilizar o comando customtkinter.CTkImage(light/dark_image=Image.open(
#                                                                 "endereço_da_imagem.extensão"), size=(width, height))
# depois, utilizar um label com o parâmetro image=variável_image

'''def evento():
    frase = 'Botão clicado'
    label_text.configure(text=str(frase))
    pass'''


# Aula 13 - Imagens
'''btn = ctk.CTkButton(janela,
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
btn.pack(pady=(20, 5))'''
label_text = ctk.CTkLabel(janela, text="", width=200)
label_text.pack()
janela.mainloop()  # rodando o programa em loop
