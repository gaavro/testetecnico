# API de Expressões Lógicas
Este é um exemplo de API de Expressões Lógicas construída em Flask com Docker e PostgreSQL. A API permite criar, listar e avaliar expressões lógicas.

## Instalação
Para rodar a aplicação é necessário ter o Docker e o Docker Compose instalados na máquina.

Clone o repositório para a sua máquina
Navegue para a pasta do projeto
Construa a imagem do Docker com o comando:

docker-compose build
Inicie os containers com o comando:

docker-compose up
Agora a aplicação está sendo executada e pode ser acessada no endereço http://localhost:5000.

Endpoints
GET /expressoes
Este endpoint retorna todas as expressões lógicas cadastradas na base de dados.

Resposta

```shell
[
    {
        "id": 1,
        "expressao": "(x OR y) AND z"
    },
    {
        "id": 2,
        "expressao": "((x OR y) AND (z OR k) OR j)"
    }
]
```

POST /expressoes
Este endpoint permite criar uma nova expressão lógica ou atualizar uma expressão existente. É necessário informar a expressão lógica no corpo da requisição no formato JSON.

Requisição
```shell

{
    "expressao": "(x OR y) AND z"
}
```

Resposta
```shell

{
    "id": 1,
    "expressao": "(x OR y) AND z"
}
```

GET /avaliar/{expression_id}
Este endpoint permite avaliar uma expressão lógica para um conjunto de valores de entrada. Os valores de entrada devem ser informados na query string da requisição.

Requisição

GET /avaliar/1?x=1&y=0&z=1
Resposta
```shell
{
    "expressao": "(x OR y) AND z",
    "valores": {
        "x": 1,
        "y": 0,
        "z": 1
    },
    "resultado": true
}
```

DELETE /expressoes/{expression_id}
Este endpoint permite excluir uma expressão lógica da base de dados.

Requisição

DELETE /expressoes/1
Resposta
```shell

{
    "mensagem": "Expressão excluída com sucesso"
}
```
