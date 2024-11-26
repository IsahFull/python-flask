from flask import Flask, render_template, request

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

@app.route('/subtracao/<int:num1>/<int:num2>')
def subtracao(num1, num2):
    return f'Total da subtração: {num1 - num2}'

@app.route('/multiplicacao/<int:num1>/<int:num2>')
def multiplicacao(num1, num2):
    return f'Total da multiplicação: {num1 * num2}'

@app.route('/divisao/<int:num1>/<int:num2>')
def divisao(num1, num2):
    if num2 == 0:
        return 'Erro! Divisão por zero não é permitida.'
    return f'Total da divisão: {num1 / num2}'

#MINHA PAGINA PESSOAL
@app.route('/sobre')
def sobre ():
    return  render_template('sobre.html')

#ROTA PARA FORM DADOS
@app.route('/dados')
def dados ():
    return  render_template('dados.html')

#ROTA PARA FORM DADOS GET
#@app.route('/recebedados', methods=['GET'])
#def recebedados():
    #nome = request.args.get("nome")  # Pega o valor enviado no campo 'nome'
    #email = request.args.get("email") # Pega o valor enviado no campo 'email'
    #if nome and email:  # Verifica se um valor foi enviado
        #return f"Nome e email recebidos:" "{} - {}" .format (nome, email)
    #else:
        #return "Nenhum dado foi enviado. Por favor, preencha os campos."

#ROTA PARA FORM DADOS POST
@app.route('/recebedados', methods=['POST'])
def recebedados():
    nome = request.form.get("nome")  # Pega o valor enviado no campo 'nome'
    email = request.form.get("email") # Pega o valor enviado no campo 'email'
    if nome and email:  # Verifica se um valor foi enviado
        return f"Nome e email recebidos:" "{} e {}" .format (nome, email)
    else:
      return "Nenhum dado foi enviado. Por favor, preencha os campos."

    #ROTA PARA FORM DADOS POST -CAMPOS ESPECIAIS HTML-
#@app.route('/recebedados', methods=['POST'])
#def recebedados():
    #estado = request.form['estado'] #que vai receber ou RN, ou PB, ou PE ou CE

#@app.route('/recebedados', methods=['POST'])
#def recebedados():
    #estado = request.form['formacao'] #que vai receber ou fundamental, ou medio, ou superior

#@app.route('/recebedados', methods=['POST'])
#def recebedados():
    #estado = request.form.getlist('modalidades') #que vai ter todos os valores selecionados pelo usuário
if __name__ == '__main__':
    app.run()