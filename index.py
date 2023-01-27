from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

@app.route("/")
def home():
    name = "John"
    items = ["item1", "item2", "item3"]
    return render_template("home.html", name=name, items=items)

@app.route("/works")
def works():
    works = ["work1", "work2", "work3"]
    return render_template("works.html", works=works)


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)