from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index ():
    return  render_template('index.html')

@app.route('/contato')
def contato ():
    return render_template('contato.html', tel = '(87)98165-6521', nome = 'Isadora Sá')

@app.route('/pagina')
def pagina ():
    return  render_template('pagina.html')

@app.route('/redes')
def redes ():
    return render_template('redes.html', rs = 'isa_ttavares', git = 'FullIsah')

#calculadora operação parametro dinamico
@app.route('/soma/<int:num1>/<int:num2>')
def soma (num1, num2):
    return f'Total: {num1 + num2}'


if __name__ == '__main__':
    app.run()