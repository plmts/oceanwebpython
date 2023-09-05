from flask import Flask, render_template

app = Flask("meu app")

posts = [
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
