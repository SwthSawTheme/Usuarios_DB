import pyodbc
import os
from time import sleep
from datetime import datetime

# Configuração da string de conexão
data = (
    "Driver={SQL Server};"
    "Server=Saw;"
    "Database=Usuarios;"
)

try:
    conexao = pyodbc.connect(data)
    print("Conexão bem sucedida!")
except Exception as e:
    print(f"Erro de conexão: {e}")
    exit()

# Criação de um cursor para a manipulação
cursor = conexao.cursor()

data_atual = datetime.now()
data_formatada = data_atual.strftime('%Y-%m-%d')

def clear():
    return os.system("cls")

def addUser(date: str, name: str, user: str, password: str):
    insert = """
        INSERT INTO Registro (Data_Registro, Nome, Usuario, Senha)
        VALUES (?, ?, ?, ?)
    """
    # Retorna o comando e os parâmetros
    return insert, (date, name, user, password)

def main():
    while True:
        clear()
        sleep(0.5)
        print("Registro Simplificado de Usuario:")

        try:
            name = input("Digite seu nome: ")
            user = input("Digite seu usuario: ")
            password = input("Digite sua senha: ")

            command, params = addUser(data_formatada, name, user, password)

            cursor.execute(command, params)
            cursor.commit() 

            print(f"Parabéns {name}! O Usuario {user} foi cadastrado com sucesso!")
            input()

        except Exception as e:
            print(f"Erro: {e}")
            input()

# Faz a execução no banco
# cursor.execute(comando)

# Faz as alterações no banco
# cursor.commit()

if __name__ == "__main__":
    main()