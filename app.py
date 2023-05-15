from flask import Flask, render_template, request

app = Flask(__name__)
items_storage = []


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/greet/<name>")
def greet(name):
    return render_template("greet.html", name=name)


@app.route("/items", methods=["GET", "POST"])
def items():
    if request.method == "POST":
        item = request.form.get("item")
        items_storage.append(item)
    return render_template("items.html", items=items_storage)


if __name__ == "__main__":
    app.run(debug=True)
