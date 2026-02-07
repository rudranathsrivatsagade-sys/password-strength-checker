from flask import Flask, render_template, request
import re

app = Flask(__name__)

def analyze_password(password):
    rules = {
        "length": len(password) >= 8,
        "uppercase": re.search(r"[A-Z]", password) is not None,
        "lowercase": re.search(r"[a-z]", password) is not None,
        "number": re.search(r"[0-9]", password) is not None,
        "special": re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is not None,
    }

    score = sum(rules.values())
    percentage = int((score / len(rules)) * 100)

    if percentage < 40:
        level = "Weak"
        color = "red"
    elif percentage < 80:
        level = "Medium"
        color = "orange"
    else:
        level = "Strong"
        color = "green"

    return rules, percentage, level, color


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    rules = {}
    percentage = 0
    level = ""
    color = ""

    if request.method == "POST":
        password = request.form.get("password", "")
        rules, percentage, level, color = analyze_password(password)

    return render_template(
        "index.html",
        rules=rules,
        percentage=percentage,
        level=level,
        color=color
    )


if __name__ == "__main__":
    app.run(debug=True)
