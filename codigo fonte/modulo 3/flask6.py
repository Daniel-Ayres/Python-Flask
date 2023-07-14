from flask import Flask, request
import webbrowser
import threading

app = Flask(__name__)

@app.route('/')
def index():
    return "Página principal"

@app.route('/ola/')
@app.route('/ola/<nome>')
def ola_mundo(nome=""):
    return "Olá, " + nome if nome else "Olá, mundo"

@app.route('/logar', methods=['GET', 'POST'])
def logar():
    if request.method == 'POST':
        return "Recebeu post! Fazer login!"
    else:
        return "Recebeu get! Exibir FORM de login."

def abrir_navegador():
    webbrowser.open('http://127.0.0.1:5000/')

if __name__ == '__main__':
    # Inicia uma thread para abrir o navegador
    threading.Timer(1, abrir_navegador).start()
    app.run()
