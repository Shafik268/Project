from flask import app, render_template, request, redirect


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