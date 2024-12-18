from flask import Flask, redirect, url_for, render_template, request
from decrappify_edited import grokOutput

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    output = "Summary will be displayed here."
    
    if request.method == "POST":
        user_input = request.form.get("input")

        output = grokOutput(user_input)
    return render_template("index.html", output=output)


if __name__ == "__main__":
    app.run()
