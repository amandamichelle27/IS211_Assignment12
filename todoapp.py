# Standard library imports.
from re import search

# Third-party imports.
from flask import Flask, redirect, render_template, request, url_for

items = [
    {
        "description": "Buy Milk",
        "email":       "test@123.com",
        "priority":    "Low",
    }, {
        "description": "Buy Eggs",
        "email":       "test2@123.com",
        "priority":    "High",
    }
]
        

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("todo.html", items=items)
    
@app.route("/submit", methods=["POST"])
def add_item():
    if (request.form["description"] and
        request.form["priority"] in ["Low", "Medium", "High"] and
        search("^\S+@\S+\.\S+$", request.form["email"])):
        items.append(request.form)
    return redirect(url_for("index"))
    
@app.route("/clear", methods=["POST"])
def clear_item():
    del items[:]
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
