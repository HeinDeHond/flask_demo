from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    return  # Put any string here


if __name__ == "__main__":
    app.run(debug=True)
