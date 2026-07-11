from flask import render_template


def register_routes(app):

    @app.route("/")
    def home():
        return render_template("index.html")


    @app.route("/report")
    def report():
        return render_template("report.html")


    @app.route("/dashboard")
    def dashboard():
        return render_template("dashboard.html")


    @app.route("/resources")
    def resources():
        return render_template("resources.html")


    @app.route("/shelters")
    def shelters():
        return render_template("shelters.html")