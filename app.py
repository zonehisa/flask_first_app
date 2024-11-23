from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World"


@app.route("/goodbye")
def goodbye():
    return "Good Bye"


@app.route("/user/<name>")
def hi(name):
    return f"Hi, {name}"


@app.route("/about/<name>")
def show_profile(name):
    return f"{name}'s profile"


@app.route("/hello")
def hello():
    html = "<html><body><h1>Hello</h1></body></html>"
    return html


@app.route("/profile/<name>")
def profile(name):
    html = f"<html><body><h1>{name}'s profile</h1></body></html>"
    return html


if __name__ == "__main__":
    app.run(port=8000, debug=True)
