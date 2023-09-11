from flask import Flask, render_template, request, session, flash, redirect, url_for
from posts import posts
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'blablabla' #procurar saber sobre

@app.config.from_object(__name__) #confg para que o python possa gerir as confg de frameworks que n sejam dele

DATABASE = "banco.bd" #variável para poder facilitar a manipulação do banco de dados no futuro

def conectar(): #função para se conectar ao banco de dados
    def sqlite3.connect(DATABASE)

@app.route('/')
def exibir_entradas():
    entradas = posts[::-1] #mock das postagens ordenadas da mais recente para mais antiga
    return render_template('exibir_entradas.html', entradas=entradas) #renderização do html na pasta /templates

@app.route('/layout')
def layout():
    return render_template('layout.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    erro = None
    if request.method == "POST":
        if request.form['username'] == 'admin' and request.form['password'] == 'admin':
            session['logado'] = True #manter usuário logado
            flash("Login efetuado com sucesso!") #mensagens
            return redirect(url_for('exibir_entradas'))
        erro = "Usuário ou senha inválido(a)"
    return render_template('login.html', erro=erro)

@app.route('/logout')
def logout():
    session.pop('logado') #remover session para o logout
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('login'))

@app.route('/inserir', methods=['POST'])
def inserir_entradas(): #rota para inserir novos posts
    if session['logado']:
        novo_post= { #criando um novo post para ser publicado
        "titulo": request.form['titulo'],
        "texto": request.form['texto']
        }
        posts.append(novo_post) #adicionando ao bd mockado
        flash("Post criado com sucesso!")
    return redirect(url_for('exibir_entradas'))

@app.route('/posts/<int:id>')
def exibir_entrada(id):
    try:
        entrada = posts[id-1]
        return render_template('exibir_entrada.html', entrada=entrada)
    except Exception:
        return abort(404)