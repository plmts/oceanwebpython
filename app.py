from flask import Flask, render_template, request, session, flash, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'blablabla'

posts = [ #tabela em forma de mock
    {
        "titulo": "Minha primeira postagem",
        "texto": "postagem 1"
    },
    {
        "titulo":"Minha segunda postagem",
        "texto":"postagem 2"
    }
]

@app.route('/')
def exibir_entradas():
    entradas = posts #mock das postagens
    return render_template('exibir_entradas.html', entradas=entradas) #renderização do html na pasta /templates

@app.route('/layout')
def layout():
    return render_template('layout.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    erro = None
    if request.method == "POST":
        if request.form['username'] == 'admin' and request.form['password'] == 'admin':
            session['logado'] = True
            flash("Login efetuado com sucesso!")
            return redirect(url_for('exibir_entradas'))
        erro = "Usuário ou senha inválido(a)"
    return render_template('login.html', erro=erro)
