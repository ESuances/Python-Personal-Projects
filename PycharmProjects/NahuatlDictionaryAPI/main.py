from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/api/v1/<palabra>")
def api(palabra):
    definition = palabra.upper()
    result_dict = {"palabra": palabra, 'definition': definition}
    return result_dict

if __name__ == "__main__":
    app.run(debug=True)