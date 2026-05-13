# Criação de currículo utilizando flask

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return '''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Currículo</title>
</head>
<body>
    <h1> Currículo <h1>
    
    <h2>Informações Pessoais</h2>
    <ul>
        <li><strong>Nome:</strong> Marcelo Rodrigues</li>   
        <li><strong>Email:</strong> 12400815@aluno.cotemig.com.br</li>   
        <li><strong>Telefone:</strong> (31) 99999-9999</li>
    </ul>

    <h2>Habilidades</h2>
    <ul>
        <li><strong>Boa explicação</strong></li>
        <li><strong>Facil entendimento</strong></li>
    </ul>
</body>
</html>'''

if (__name__ == "__main__"):
    app.run(debug = True)