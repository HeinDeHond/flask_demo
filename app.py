from flask import Flask, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello index page"


@app.route("/greet/<name>")
def greet(name):
    # modify this function to return "Hello, name"
    return f"Hello, {name}"


@app.route("/multiply/<int:first_arg>/<int:second_arg>")
def multiply(first_arg: int, second_arg:int):
    return f"{first_arg * second_arg}" # multiply args


with app.test_request_context():
    print(url_for("index"))
    print(url_for("multiply", first_arg=333, second_arg=3))
    print(url_for("multiply", first_arg=333, second_arg=3, as_complex=True))


if __name__ == "__main__":
    app.run(debug=True)
