from flask import Flask
import webbrowser

app = Flask(__name__)

@app.route('/ola')
def ola_mundo():
    return "Olá, mundo."

if __name__ == '__main__':
    # Abre o navegador automaticamente
    webbrowser.open('http://127.0.0.1:5000')
    # Executa o aplicativo Flask
    app.run()
