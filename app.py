from flask import Flask, render_template, request
import re

app = Flask(__name__)

def check_password(password):
    issues = []

    if len(password) < 8:
        issues.append("Minimum 8 characters")
    if not re.search(r"[A-Z]", password):
        issues.append("At least one uppercase letter")
    if not re.search(r"[a-z]", password):
        issues.append("At least one lowercase letter")
    if not re.search(r"[0-9]", password):
        issues.append("At least one number")
    if not re.search(r"[^A-Za-z0-9]", password):
        issues.append("At least one special character")

    return issues

@app.route("/", methods=["GET", "POST"])
def home():
    issues = []
    password = ""

    if request.method == "POST":
        password = request.form.get("password", "")
        issues = check_password(password)

    return render_template("index.html", issues=issues, password=password)

if __name__ == "__main__":
    app.run()
