from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    output = None
    
    if request.method == "POST":
        user_input = request.form.get("userInput", "")

        output = user_input[::-1]
    return render_template("index.html", output=output)


if __name__ == "__main__":
    app.run()
