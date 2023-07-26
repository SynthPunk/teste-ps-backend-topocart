Crie um fork deste repositório e realize as seguintes ações:

## Objetivo

- Desenvolver uma API expondo os métodos CRUD da tabela `dados`

## Critérios de aceitação

- Deve existir um endpoint `GET` em `{API}/dados` para obter todos os dados
- Deve existir um endpoint `GET` em `{API}/dados/:id` para obter o dado com o ID selecionado
- Deve existir um endpoint `POST` em `{API}/dados` que crie um novo dado ao enviar o seguinte JSON:

```JSON
{
    "nome": "Teste",
    "descricao": "Isto é um teste"
}
```

- Deve existir um endpoint `PATCH` em `{API}/dados/:id` para atualizar o dado com o ID selecionado que receba o seguinte JSON:

```JSON
{
    "nome": "Outro teste",
    "descricao": "Isto também é um teste"
}
```

- Deve existir um endpoint `DELETE` em `{API}/dados/:id` para excluir o dado com o ID selecionado 

## Observações

- A API pode ser desenvolvida em qualquer framework Javascript, Typescript, Python ou Java
- A API deve manipular alguma base de dados, pode ser um JSON ou algum SGBD de sua preferência
- Ao finalizar, envie um email para `victor.santos@topocart.com.br` com o link do repositório no Github onde executou as tarefas