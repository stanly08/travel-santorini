from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "index.html"

app.run(host="0.0.0.0", port=50100, debug=True)
