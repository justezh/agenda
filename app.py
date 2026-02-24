from flask import Flask, render_template, request, redirect, url_for
from models.Midia import Midia
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():
    midias = Midia.obter_midias()
    return render_template("index.html", midias=midias)


@app.route("/criar", methods=["GET", "POST"])
def criar():

    if request.method == "POST":

        titulo = request.form["titulo"]
        tipo = request.form["tipo"]
        indicado_por = request.form.get("indicado_por")

        imagem_nome = None

        file = request.files.get("imagem")

        if file and file.filename:
            filename = secure_filename(file.filename)
            caminho = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(caminho)
            imagem_nome = filename

        nova_midia = Midia(
            titulo=titulo,
            tipo=tipo,
            indicado_por=indicado_por,
            imagem=imagem_nome
        )

        nova_midia.salvar()

        return redirect(url_for("home"))

    return render_template("criar.html")


@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):

    midia = Midia.id(id)

    if request.method == "POST":

        midia.titulo = request.form["titulo"]
        midia.tipo = request.form["tipo"]
        midia.indicado_por = request.form.get("indicado_por")

        file = request.files.get("imagem")

        if file and file.filename:
            filename = secure_filename(file.filename)
            caminho = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(caminho)
            midia.imagem = filename

        midia.atualizar()

        return redirect(url_for("home"))

    return render_template("editar.html", midia=midia)


@app.route("/excluir/<int:id>")
def excluir(id):

    midia = Midia.id(id)
    midia.excluir()

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)