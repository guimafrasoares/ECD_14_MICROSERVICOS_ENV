from fastapi import FastAPI 
from ariadne import load_schema_from_path 
from ariadne import make_executable_schema
from ariadne import QueryType
from ariadne import MutationType
from ariadne.asgi import GraphQL
import requests
import os

app = FastAPI(
    title="GraphQL API Gateway para Contatos"
)

# URLs dos serviços REST (definidos via variáveis de ambiente no Docker Compose)
CONTACT_SERVICE_URL = os.getenv("CONTACT_SERVICE_URL", "http://localhost:9002")

# Carrega o esquema GraphQL 
type_defs = load_schema_from_path("schema.graphql")

query = QueryType()
mutation = MutationType()

# mapeia uma consulta a 'contatos' (lista de contatos)
@query.field("contatos")
def resolve_contatos(_, info):
    try:
        # consulta o microsserviço de contatos
        response = requests.get(f"{CONTACT_SERVICE_URL}/contatos")
        response.raise_for_status() # Dispara um HTTPError para status 4xx/5xx
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao consultar serviço de contatos: {e}")
        return [] # Retorna lista vazia ou um erro mais específico para o cliente GraphQL

# mapeia uma consulta a 'contato' (um contato específico)
@query.field("contato")
def resolve_product(_, info, id: int):
    try:
        response = requests.get(f"{CONTACT_SERVICE_URL}/contato/{id}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            return None # Retorna null para contato não encontrado, conforme o esquema
        print(f"Erro HTTP ao consultar serviço de contatos (contato/{id}): {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão ao consultar serviço de contatos (contato/{id}): {e}")
        return None

# mapeia um mutation para criar novos contatos
@mutation.field("createContato")
def resolve_create_contato(_, info, input: dict):
    id = input.get("id")
    nome = input.get("nome")
    telefone = input.get("telefone")
    categoria = input.get("categoria")
    tipoTelefone = input.get("tipoTelefone")

    try:
        # faz um POST no microsserviço de pedidos
        response = requests.post(
            f"{CONTACT_SERVICE_URL}/contato",
            json={"id": id, "nome": nome, "telefone": telefone, "categoria": categoria, "tipoTelefone": tipoTelefone}
        )
        response.raise_for_status()
        response_data = response.json()
        return {
            "message": response_data.get("message", "Contato criado com sucesso."),
            "contato": response_data.get("contato")
        }
    except requests.exceptions.HTTPError as e:
        print(f"Erro HTTP ao criar contato: {e}. Resposta: {e.response.text}")
        error_detail = e.response.json().get("detail", "Erro desconhecido ao criar contato.")
        return {
            "message": error_detail,
            "contato": None 
        }
    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão ao criar contato: {e}")
        return {
            "message": "Erro de rede ao comunicar com o serviço de contatos.",
            "contato": None
        }

schema = make_executable_schema(type_defs, [query, mutation])

# Adiciona o Endpoint GraphQL ao FastAPI 
app.mount("/graphql", GraphQL(schema, debug=True)) # debug=True para habilitar o GraphQL IDE