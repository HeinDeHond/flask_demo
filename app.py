from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    return "Hello index page"


@app.route("/greet/<name>")
def greet(name):
    # modify this function to return "Hello, name"
    return f"Hello, {'replace_me'}"


@app.route("/multiply/<int:first_arg>/<int:second_arg>")
def multiply(first_arg: int, second_arg:int):
    return f"{'replace_me'}" # multiply args


if __name__ == "__main__":
    app.run(debug=True)
