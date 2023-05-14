from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/greet/<name>")
def greet(name):
    return render_template("greet.html", name=name)


@app.route("/multiply/<int:first_arg>/<int:second_arg>")
def multiply(first_arg: int, second_arg: int):
    return f"{first_arg * second_arg}"


if __name__ == "__main__":
    app.run(debug=True)
