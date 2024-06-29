

import customtkinter as ctk
from tkinter import *
from PIL import Image

app = ctk.CTk()


class Application:

    def __init__(self):
        self.app = app
        self.tema()
        self.tela()
        self.login_screen()
        # self.login_fun()
        app.mainloop()

    def tema(self):
        ctk.set_appearance_mode("dark")
        ctk.set_appearance_mode("dark-blue")

    def tela(self):
        app.geometry("900x500")
        app.title("Sistema de Login")
        app.resizable(False, False)
        app.iconbitmap("./images/icon-starrr.ico")  # usado para alterar o ícone do programa

    def login_screen(self):
        image_frame = ctk.CTkFrame(app, fg_color="#000000",
                                   width=450, height=500,
                                   corner_radius=10)
        image_frame.grid(row=0, column=0)
        image = ctk.CTkImage(light_image=Image.open("./images/bg-rocket-blackbg.jpg"), size=(400, 250))
        img_label = ctk.CTkLabel(image_frame, image=image,
                                 text="", corner_radius=50)
        img_label.place(x=10, y=200)
        ctk.CTkLabel(image_frame, text="Acesse agora a \nnossa plataforma!",
                     font=("Helvetica", 40), fg_color="transparent",
                     text_color="#FCD112").place(x=65, y=50)

        login_frame = ctk.CTkFrame(app, fg_color="#14213d",
                                   width=450, height=500,
                                   corner_radius=0)
        login_frame.grid(row=0, column=1)
        login_intro = ctk.CTkLabel(login_frame,
                                   text="SISTEMA DE LOGIN",
                                   font=("Helvetica", 30),
                                   text_color="#e5e5e5")
        login_intro.place(x=85, y=50)

        # Entrada de Usuário e Senha
        username_entry = ctk.CTkEntry(login_frame, placeholder_text="Username",
                                      width=300, height=40,
                                      corner_radius=10, font=("Helvetica", 20), fg_color="white",
                                      text_color="black", placeholder_text_color="#A2A2A2")
        username_entry.place(x=80, y=150)

        user_name_obrigatorio = ctk.CTkLabel(login_frame, text="** Este campo é obrigatório",
                                             font=("Roboto", 12), text_color="red",
                                             bg_color="transparent", fg_color="transparent")
        user_name_obrigatorio.place(x=80, y=190)

        password_entry = ctk.CTkEntry(login_frame, placeholder_text="Password",
                                      width=300, height=40,
                                      show="*", corner_radius=10,
                                      font=("Helvetica", 20), fg_color="white",
                                      text_color="black", placeholder_text_color="#A2A2A2")
        password_entry.place(x=80, y=220)

        # def login_fun():
        #     password_entry.delete(0, END)
        #     username_entry.delete(0, END)
        #     login_checkbox.deselect(True)

        # Imagem de Login e Senha
        # Checkbox e Button
        login_checkbox = ctk.CTkCheckBox(login_frame, text="Lembrar-me", font=("Helvetica", 20))
        login_checkbox.place(x=80, y=300)
        login_button = ctk.CTkButton(login_frame, text="ENTRAR",
                                     width=200, height=50,
                                     corner_radius=10, fg_color="#D2AD0B",
                                     hover_color="#A18507", text_color="#000000")
        login_button.place(x=130, y=370)


Application()
