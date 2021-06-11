from flask import render_template, redirect, url_for
from brasileirao.views.controllers import pegar_times_do_banco


def init_app(app):

    @app.route("/")
    def index():
        return redirect(url_for("times_cadastrados"))

    @app.route("/times")
    def times_cadastrados():
        times = pegar_times_do_banco()
        print(times)
        return render_template("times_da_serie_a.html", times=times)
