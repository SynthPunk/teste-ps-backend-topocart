from flask import Flask, jsonify, request

app = Flask(__name__)

dados = [
    {
        'id': 1,
        'nome': 'Teste 1',
        'descricao': 'Isto é o primeiro teste'
    },
    {
        'id': 2,
        'nome': 'Teste 2',
        'descricao': 'Isto é o segundo teste'
    },
    {
        'id': 3,
        'nome': 'Teste 3',
        'descricao': 'Isto é o terceiro teste'
    },
    {
        'id': 4,
        'nome': 'Teste 4',
        'descricao': 'Isto é o quarto teste'
    },
    {
        'id': 5,
        'nome': 'Teste 5',
        'descricao': 'Isto é o quinto teste'
    }
]

# Função de Consulta Geral
@app.route('/dados')
def obter_dados():
    return jsonify(dados)

# Função de Consulta por ID
@app.route('/dados/<int:id>',methods=['GET'])
def obter_dado_por_id(id):
    for dado in dados:
        if dado.get('id') == id:
            return jsonify(dado)
# Função de Criação
@app.route('/dados',methods=['POST'])
def adicionar_dado():
    novo_dado = request.get_json()
    dados.append(novo_dado)

    return jsonify(dados)
# Função de Edição
@app.route('/dados/<int:id>',methods=['PATCH'])
def editar_dado_por_id(id):
    dado_editado = request.get_json()
    for indice,dado in enumerate(dados):
        if dado.get('id') == id:
            dados[indice].update(dado_editado)
            return jsonify(dados[indice])
# Função de Exclusão
@app.route('/daos/<int:id>',methods=['DELETE'])
def excluir_dado(id):
    for indice, dado in enumerate(dados):
        if dado.get('id') == id:
            del dados[indice]
            
    return jsonify(dados)                
app.run(port=1337,host='localhost',debug=True)