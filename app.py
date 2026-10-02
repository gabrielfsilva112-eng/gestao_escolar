from flask import Flask, request

from database import criar_tabelas, conectar_banco

app = Flask(__name__)

criar_tabelas()

@app.route("/")
def inicio():
    return "Sistema de Gerenciamento Escolar"


@app.route("/alunos", methods=["POST"])
def cadastrar_aluno():
    dados = request.get_json()

    nome = dados["nome"]
    email = dados["email"]
    idade = dados["idade"]

    conexao = conectar_banco()

    conexao.execute(
        """
        INSERT INTO alunos (nome, email, idade)
        values (?, ?, ?)
        """, (nome, email, idade)
    )

    conexao.commit()
    conexao.close()

    return "Aluno cadastrado com sucesso", 200

if __name__ == "__main__":
    app.run(debug=True)