import sqlite3

conection_var = sqlite3.connect("sistema.db")

# criando o cursor, que será a ponte dos dados ao banco de dados ;
cursor = conection_var.cursor()  # objeto
# passando o comando para o cursor criar uma tabela SE não existir uma tabela "usuario" ;
# meus comandos em minusculo; COMANDOS SQL EM MAIUSCULO;
# CRIA UM ID INTEIRO NÃO VAZIO, SENDO UMA CHAVE PRIMÁRIA(IDENTIFICADORA), E QUE VAI SE AUTO INCREMENTAR se não
# passarmos nenhum valor ;
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS users (
#     Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#     Username TEXT NOT NULL,
#     Email TEXT NOT NULL,
#     Password TEXT NOT NULL,
#     ConfPassword TEXT NOT NULL
# )""")
# cursor.execute("SELECT * FROM users")
# # inserindo manualmente os dados no banco de dados
#
# usuarios = cursor.fetchall()

