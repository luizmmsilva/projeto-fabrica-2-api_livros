# No terminal:
# 1) Criamos um ambiente virtual com o comando:
# python -m venv . venv
# 2) Ativamos o ambiente virtual com o comando:
# .\.venv\Scripts\activate
# 3) Instalamos o flask com o comando:
# pip install flask
# Caso o seu ambiente virtual não seja ativado pe preciso pesquisar na
# internet como liberarr a execução 
# dele no PowerShell e voltar a ativar o ambiente depois

from flask import Flask, jsonify,make_response,request
from bd_livros import livros # aqui eu estou importando a lista de livros criado (banco de dados)

# BIBLIOTECAS
# jsonify = transforma lista, dicionários etc em arquivos json. Só funciona com status code 20, ou seja
#quando a requisição é bem sucedida
#make_response = ransforma os json em métodos HTTP e permite que estilizemos nossa resposta 
# e trata os erros 
#request = faz as requisições

app = Flask(__name__) # instanciandoi o flask, ou seja estou tornando o molde num objeto 
app.config['JSON_SORT_KEYS']= False

# Get - Listar todos os livros do nossso "banco de dados"
@app.route('/livros', methods=['GET'])
def get_livros():
    return make_response(jsonify(
        mensagem = 'Lista de Livros Cadastrados',
        dados = livros 
    ),200)

# GET _ Buscar apenas um livro pelo ID
@app.route('/livros/<int:id>', methods=['GET'])
def get_livro(id):
    for livro in livros: # percorrer a lista de livros 
        if livro.get('id') == id:
            return make_response(jsonify(
                mensagem=f'Livro de ID {id} encontrado.',
                dados = livro

            ),200)
    return make_response(jsonify(mensagem='Livro não encontrado'),404)

# Post - Adicionar um novo livro
@app.route('/livros',methods=['POST'])
def create_livro():
    novo_livro = request.json
    livros.append(novo_livro)
    return make_response(jsonify(
        mensagem = 'Novo livro adicionado com sucesso',
        dados = novo_livro
    ),201)

# PUT - Atualizar livro por completo
@app.route('/livros/<int:id>',methods=['PUT'])
def update_livro(id):
    for livro in livros:
        if livro.get('id') == id:
            novo_dados = request.json
            livro.update(novo_dados) # substitui todos os dados
            return make_response(jsonify(
            mensagem=f'Livro ID{id} atualizado com susesso (PUT).'
            ),200)
    return make_response(jsonify(mensagem='Livro não encontrado'),404)

# PATCH - Atualizar parcialmente um livro 
@app.route('/livros/<int:id>',methods=['PATCH'])
def patch_livro(id):
    for livro in livros:
        if livro.get('id') == id:
            dados = request.json
            livro.update(dados) # só altera os campos enviados
            return make_response(jsonify(
                mensagem=f'Livro ID {id} ataulizado parcialmente (PATCH).',
            ),200)
    return make_response(jsonify(mensagem='Livro não encontrado'),404)


# DELETE - Remover um livro
@app.route('/livros/<int:id>',methods=['DELETE'])
def delete_livro(id):
    for livro in livros:
        if livro.get('id') == id:
            livros.remove(livro)
            return make_response(jsonify(
                mensagem=f'Livro ID{id} foi removido com sucesso.'
            ),200)
    return make_response(jsonify(mensagem='Livro não encontrado'),404)






if __name__ == '__main__': # esse comando permite que a api seja executada
    # de maneirar imdependente em outros arquivos
    app.run(debug=True)



