from flask import Flask, render_template, request
import re

app = Flask(__name__)

def check_password(password):
    score = 0
    reasons = []

    if len(password) >= 8:
        score += 1
    else:
        reasons.append("Minimum 8 characters")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        reasons.append("Add at least one uppercase letter")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        reasons.append("Add at least one lowercase letter")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        reasons.append("Add at least one number")

    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        reasons.append("Add at least one special character")

    percentage = int((score / 5) * 100)
    return percentage, reasons


@app.route("/", methods=["GET", "POST"])
def home():
    percentage = 0
    reasons = []

    if request.method == "POST":
        password = request.form.get("password", "")
        percentage, reasons = check_password(password)

    return render_template(
        "index.html",
        percentage=percentage,
        reasons=reasons
    )


if __name__ == "__main__":
    app.run()
