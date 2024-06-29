
import customtkinter as ctk

janela = ctk.CTk()  # a primeira janela
janela.title("APP TESTE")  # configura o título da aplicação
janela.geometry("700x400")  # configura a dimensão inicial da aplicação
janela._set_appearance_mode("dark")


# Aula 09 - Menu Option

ctk.CTkLabel(master=janela, text="Menu de Opções. Aula - 09", font=("arial bold", 20)).pack(pady=20, padx=5)
ctk.CTkLabel(janela, text="Mês de nascimento: ", font=("arial bold", 14)).pack()

mes_var = ctk.StringVar(value="Escolha o mês ae meu consagrado: ")  # mesma função de mes.set("Junho")  # var.set(
# valor), porém utilizando diretamente uma variável


def call_month(choice):
    print(f'O seu mês de nascimento é: {choice}')


mes = ctk.CTkOptionMenu(master=janela,
                  values=["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro",
                          "Outubro", "Novembro", "Dezembro"],  # valores que serão mostrados no menu de opções
                        command=call_month,  # puxa a função definida
                        variable=mes_var,  # exibe a mensagem na barra do menu de opções definida na variável
                        dropdown_fg_color="cyan",  # altera cor do 1o. plano das opções
                        dropdown_text_color="black")
mes.pack(pady=10)
#  mes.set("Junho")  # var.set(valor) = define o valor (representativo, que também pode ser apenas uma mensagem
# ilustrativa fora dos valores da variável) inicial do menu de opções



# mes = ctk.CTkOptionMenu(master=janela,
#                   values=["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro",
#                           "Outubro", "Novembro", "Dezembro"],
#                         command=call_month)
# mes.pack(pady=10)
# mes.set("Junho")  # var.set(valor) = define o valor (representativo, que também pode ser apenas uma mensagem
# # ilustrativa fora dos valores da variável) inicial do menu de opções
janela.mainloop()  # rodando o programa em loop
