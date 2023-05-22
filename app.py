#API-CUSTOMER_POINTS
#Importando a biblioteca 
import mysql.connector #Conexão do banco

from fastapi import FastAPI

# Conecta-se ao banco de dados MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="seu_usuario",
    password="sua_senha",
    database="seu_banco_de_dados"
)

# Executa uma consulta SQL
cur.execute("SELECT * FROM CostumerPoints") #No caso ele está acessando a tabela 

app = FastAPI()

admin_list = []

#Criando endpoints admin

#Get - listar os admin
@app.get("/Admin")
async def listar_admin(nomeAdmin: str):
    for admin in admin:
        if admin["nome"] == nomeAdmin:
            return {"id": admin["id"], "nome": admin["nome"]}
    return {"message": "Admin não encontrado"}

#Post - adicionar admin
@app.post("/Admin")
async def adicionar_admin(admin: dict):
    admin_list.append(admin)
    return {"message": "Admin adicionado com sucesso"}

#Put - atualizar o admin
@app.put("/Admin/{id}")
async def atualizar_admin(id: int, admin_atualizado: dict):
    for admin in admin_list:
        if admin["id"] == id:
            admin.update(admin_atualizado)
            return {"message": "Admin atualizado com sucesso"}
    return {"message": "Admin não encontrado"}

#Delete- deleter o admin pelo id
@app.delete("/Admin/{id}")
async def remover_admin(id: int):
    indice_admin = -1
    for admin in admin_list:
        if admin["id"] == id:
            admin_list.remove(admin)
            return {"message": "Admin deletado com sucesso"}

#EndPoints Cliente

clientes = [
    {"id": 1, "nome": "Cliente 1", "desempenho": "alto", "divida": "baixo", "risco": "baixo"},
    {"id": 2, "nome": "Cliente 2", "desempenho": "médio", "divida": "médio", "risco": "médio"},
    {"id": 3, "nome": "Cliente 3", "desempenho": "ruim", "divida": "alto", "risco": "alto"},
    {"id": 4, "nome": "Cliente 4", "desempenho": "baixo", "divida": "baixo", "risco": "médio"},
]

#Consultar cliente
@app.get("/cliente/{id}")
async def obter_cliente(id: int):
    for cliente in clientes:
        if cliente["id"] == id:
            return {
                "desempenho": cliente["desempenho"],
                "divida": cliente["divida"],
                "risco": cliente["risco"]
            }
    return {"message": "Cliente não encontrado"}

