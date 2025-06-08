from fastapi import FastAPI, HTTPException
from contato import Contato, TipoTelefone, Categoria
import re
import os

app = FastAPI()

CONTACT_SERVICE_URL = os.getenv("CONTACT_SERVICE_URL", "http://contact_service:8002")

contatos_db = {
    1: Contato(id=1, nome="Maria", telefone="54 99999-9999", tipoTelefone=TipoTelefone.MOVEL, categoria=Categoria.FAMILIA),
    2: Contato(id=2, nome="Zé", telefone="54 99999-9999", tipoTelefone=TipoTelefone.MOVEL, categoria=Categoria.AMIGO),
    3: Contato(id=3, nome="Pangaré", telefone="54 2131-2211", tipoTelefone=TipoTelefone.FIXO, categoria=Categoria.AMIGO),
    4: Contato(id=4, nome="Casa e Construção", telefone="54 3131-0001", tipoTelefone=TipoTelefone.COMERCIAL, categoria=Categoria.COMERCIAL),
}

@app.get("/contato/{contato_id}", response_model=Contato)
def get_contato(contato_id: int):
    """
    Retorna os detalhes de um contato específico.
    """
    contato = contatos_db.get(contato_id)
    if contato is None:
        raise HTTPException(status_code=404, detail="Contato não encontrado")
    return contato

@app.get("/contatos", response_model=list[Contato])
def list_contatos():
    """
    Lista todos os contatos cadastrados.
    """
    return list(contatos_db.values())

@app.post("/contato", status_code=201)
def create_contato(contato: Contato):
    """
    Adiciona um novo contato.
    """
    if contato.id in contatos_db:
        raise HTTPException(status_code=400, detail="Contato com este ID já existe")
    
    if re.match(r'[A-Za-z]', contato.telefone):
        raise HTTPException(status_code=400, detail="Número de telefone inválido")

    contatos_db[contato.id] = contato

    return {"message": "Contato criado com sucesso", "contato": contato}