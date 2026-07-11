<<<<<<< HEAD
from flask import render_template, request, redirect
=======
from flask import app, render_template, request, redirect

from integration import dashboard_data
>>>>>>> 1d48700ee3650180e4e6b725fac7cbf69b8b6edd


def register_routes(app):

    # -----------------------------
    # HOME PAGE
    # -----------------------------
    @app.route("/")
    def home():
        return render_template("index.html")

    # -----------------------------
    # REPORT PAGE
    # -----------------------------
    @app.route("/report")
    def report():
        return render_template("report.html")

    # -----------------------------
    # DASHBOARD
    # -----------------------------
    @app.route("/dashboard")
    def dashboard():

        from integration import dashboard_data

        data = dashboard_data()

        return render_template(
            "dashboard.html",
            total_reports=data["total_reports"],
            total_resources=data["resources"],
            total_shelters=data["shelters"],
            reports=data["reports"]
        )

    # -----------------------------
    # RESOURCES PAGE
    # -----------------------------
    @app.route("/resources")
    def resources():
        return render_template("resources.html")

    # -----------------------------
    # SHELTERS PAGE
    # -----------------------------
    @app.route("/shelters")
    def shelters():
        return render_template("shelters.html")

    # -----------------------------
    # SUBMIT REPORT
    # -----------------------------
    @app.route("/submit-report", methods=["POST"])
    def submit_report():

        name = request.form["name"]
        contact = request.form["contact"]
        disaster = request.form["disaster"]
        location = request.form["location"]
        urgency = request.form["urgency"]
        description = request.form["description"]

        from integration import save_report

        save_report(
            name,
            contact,
            disaster,
            location,
            urgency,
            description
        )

        return redirect("/dashboard")