from flask import Flask, request, render_template

app = Flask("app")

@app.route("/dados/<cidade>")
def get_dados_cidade(cidade):
    cidade = request.args.get("cidade")

    return render_template("lista_de_noticias.html", noticias=noticias), 200

