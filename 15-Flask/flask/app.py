from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to the flask course"

@app.route("/index")
def index():
    return "Welcome o index page"

if __name__ == "__main__":
    app.run(debug=True)