import pyodbc

data = (
    "Driver={SQL Server};",
    "Server=Saw;",
    "Database=Usuarios;"
)

try:
    connect = pyodbc.connect(data)
    print("Conexão bem sucedida!")
except Exception as e:
    print(f"Erro de conexão:{e}")

cursor = connect.cursor()


# Faz a execução no banco
# cursor.execute(comando)

# Faz as alterações no banco
# cursor.commit()