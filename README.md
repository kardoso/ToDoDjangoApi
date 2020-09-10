# ToDo Django API
API Simples utilizando os frameworks Django e Django Rest Framework para registro de uma ToDo List com autenticação simples com login e senha para obtenção do token; apenas usuários autenticados podem acessar as principais rotas da API; um usuário só tem acesso às operações referentes a uma task que foi criada por esse mesmo usuário (visualização, edição e exclusão).

- [Execução da aplicação](#execução-da-api)
- [Executando a aplicação com Docker](#execução-da-api-com-docker)
- [Endpoints da API](#endpoints-da-api)

## Execução da API

É necessário ter [Python](https://www.python.org/downloads/release/python-382/) instalado.

Para executar o aplicativo utilize o comando:

```
pip install -r requirements.txt && python manage.py migrate && python manage.py runserver
```

O comando acima irá instalar os requerimentos necessários para a aplicação, efetuar as migrations e executar a aplicação.

Após isso a aplicação estará disponível em: http://localhost:8000/api/

## Execução da API com Docker

É necessário ter [Docker](https://www.docker.com/products/docker-desktop) instalado.

Para fazer a build e executar o aplicativo com docker:

```
docker build -t todos -f Dockerfile . && docker run -it -p 80:8000 todos
```

Ao concluir a build e execução a aplicação poderá ser acessada a partir da url: http://localhost/api

## Endpoints da API

| Rota                    | Método | Descrição                                      | Autenticação necessária | Campos necessários no corpo da requisição |
| ----------------------- | ------ | ---------------------------------------------- | ----------------------- | ----------------------------------------- |
| /task-list/             | GET    | Lista todas as tasks                           | :heavy_check_mark:      | -                                         |
| /task/\<str:id>/        | GET    | Retorna detalhes de uma task com id específica | :heavy_check_mark:      | -                                         |
| /create-task/           | POST   | Cria uma nova task                             | :heavy_check_mark:      | title, completed                          |
| /update-task/\<str:id>/ | PATCH  | Atualiza uma task com id específica            | :heavy_check_mark:      | -                                         |
| /delete-task/\<str:id>/ | DELETE | Deleta uma task com id específica              | :heavy_check_mark:      | -                                         |
| /register/              | POST   | Registra novo usuário                          | :x:                     | username, password                        |
| /token-auth/            | POST   | Retorna Token de autenticação                  | :x:                     | username, password                        |
