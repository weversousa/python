from flask import render_template, redirect, url_for
from supermercado.controllers import pegar_produtos_do_banco


def init_app(app):

    @app.route("/")
    def index():
        return redirect(url_for("produtos_cadastrados"))

    @app.route("/produtos")
    def produtos_cadastrados():
        produtos = pegar_produtos_do_banco()
        print(produtos)
        return render_template("produtos.html", produtos=produtos)
