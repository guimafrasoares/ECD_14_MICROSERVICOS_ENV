# O trabalho final é o micro_final, no qual foi trabalhado utilizando fastapi e GraphQL

## A API foi criada para retornar toda a lista de contatos, um único contato com base no ID e cadastrar um novo contato
- Consultar contato -> /contato/{contato_id}
- Listar contatos cadastrados -> /contatos
- Cadastrar novo contato -> /contato
  - Request Body:
{
  "id": 0,
  "nome": "string",
  "telefone": "string",
  "tipoTelefone": 0,
  "categoria": 0
}

### execute com docker compose up --build  

### acesse o gateway graphql em http://127.0.0.1:9004/graphql

### termine os containers com CTRL+C
