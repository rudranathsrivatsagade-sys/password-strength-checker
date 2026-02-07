from flask import Flask, render_template, request
import re

app = Flask(__name__)

def check_password(password):
    reasons = []

    if len(password) < 8:
        reasons.append("❌ Must be at least 8 characters long")

    if not re.search(r"[A-Z]", password):
        reasons.append("❌ Must contain at least one uppercase letter")

    if not re.search(r"[a-z]", password):
        reasons.append("❌ Must contain at least one lowercase letter")

    if not re.search(r"[0-9]", password):
        reasons.append("❌ Must contain at least one number")

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        reasons.append("❌ Must contain at least one special character")

    if not reasons:
        return "✅ Strong password!", []

    return "⚠️ Weak password", reasons


@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    reasons = []

    if request.method == "POST":
        password = request.form["password"]
        result, reasons = check_password(password)

    return render_template("index.html", result=result, reasons=reasons)


if __name__ == "__main__":
    app.run(debug=True)
