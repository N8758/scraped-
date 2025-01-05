from flask import Flask, jsonify, render_template
from scrape_twitter import scrape_twitter

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/run-script")
def run_script():
    result = scrape_twitter()
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
