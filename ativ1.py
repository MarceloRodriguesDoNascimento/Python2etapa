# Crie uma aplicação Flask que contenha uma rota específica responsável por explicar o conceito de decorator em Python.
# Requisitos
# Crie uma rota acessível por meio do caminho: /decorator
# Ao acessar essa rota no navegador, deve ser exibido um texto explicando:
# O que é um decorator em Python
# Para que ele serve
# Como ele é utilizado no Flask (exemplo: @app.route)

from flask import Flask

app = Flask(__name__)


@app.route("/")
def decorator():
    return "O que: funções que modificam ou estendem o comportamento de outras funções, métodos ou classes sem alterar seu código original." \
    "\n Função: servem para modificar ou estender o comportamento de funções, métodos ou classes sem alterar seu código original." \
    "\n Uso no flask: são fundamentais para associar URLs a funções de visualização (views) e estender comportamentos, como roteamento, autenticação e gerenciamento de contexto, sem alterar o código original da função"

if (__name__ == "__main__"):
    app.run(debug = True)