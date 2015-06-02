from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/<name>")
def hello_name(name):    
    return "Hello <b>%s</b>! How are you?" % (name)


if __name__ == "__main__":
    app.debug = True
    app.run()