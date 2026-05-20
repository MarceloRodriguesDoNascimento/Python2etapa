from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")


@app.route("/page1")
def page1():
    return "page1"


@app.route("/page2")
def page2():
    return "page2"


if __name__ == "__main__":
    app.run(debug=True)