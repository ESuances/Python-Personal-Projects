from flask import Flask, render_template
import pandas as pd

app = Flask(__name__) # This takes the literal name of the file without .py

@app.route('/') #This will be the starting page.
def home():
    return render_template('home.html')

@app.route("/api/v1/<station>/<date>")
def api(station, date):
    # df = pd.read_csv
    temperature = 33
    return {"station": station,
            "date": date,
            "temperature": temperature,}

if __name__ == "__main__": # This makes it so that only when we run this file, this code is actually executed, meaning creating the site on Flask
    app.run(debug=True)