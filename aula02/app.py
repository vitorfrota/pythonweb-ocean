from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  usuario = [1, "Vitor", "Desenvolvedor"]
  alunos = ['a', 'b','c']
  return render_template("index.html", usuario=usuario, alunos=alunos)

@app.route('/contatos')
def contato():
  nomeAula = "Aula python para web"
  return render_template("contatos.html", nome=nomeAula)
