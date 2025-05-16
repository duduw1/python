/* Este code cria um serve que pode ser acessado de qualquer maquina na rede 
no terminal mostra os ip das maquinas que acesso */

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "hi"

if __name__=='__main__':
    app.run(host='0.0.0.0', port=30006, debug=True)
