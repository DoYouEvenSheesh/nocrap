from flask import Flask

app = Flask(__main__)


@app.route("/")
def home():
    return "Hello! This is the main page! <h1>STFU</h1>"

if __name__ == "__main__":
    app.run()
