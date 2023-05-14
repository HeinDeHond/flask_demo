from flask import Flask, render_template, request

app = Flask(__name__)
items_storage = []


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/items", methods=["GET", "POST"])
def items():
    if request.method == "POST":
        item = request.form.get("item")
        item = item[0:0]  # This is a bug, fix it!
        items_storage.append(item)
    return render_template("items.html", items=items_storage)


if __name__ == "__main__":
    app.run(debug=True)
