from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {"status": "API online"}

@app.route("/status")
def status():
    return {"status": "API online"}


@app.route("/")
def homes():
    return None
    ``

@app.route("/sobre")
def sobre():
    return "Projeto desenvolvido na disciplina de Integração e Entrega Contínua"

@app.route("/livros")
def livros():
    return "Lista de livros cadastrados"


@app.route("/autores")
def autores():
    return "Lista de autores cadastrados"

@app.route("/contato")
def contato():
    return "Página de contato"




if __name__ == "__main__":
    app.run(debug=True)

