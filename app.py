from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', titulo='Home')

@app.route('/agenda', methods=['GET', 'POST'])
def agenda():
    if request.method == 'POST':
    titulo_tarefa = "titulo_tarefa do form"
    data_conclusao = request.form[]
    return render_template('agenda.html',titulo='agenda')

@app.route('/ola')
def ola_mundo():
    return "Olá, Mundo!"    
