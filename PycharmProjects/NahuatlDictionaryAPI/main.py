from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

df = pd.read_csv('dictionary.csv') # No es un diccionario Nahuatl, despues lo tendre que cambiar

# Sorry, la neta no me sentia tan motivado o mas bien tenia la mente en otro lado
# La verdad no me motiva mucho esto de aprender a hacer APIs, pense que seria mucho mejor, pero es puro dato
# Supongo que pense que era mas divertido manipular datos, pero hasta el momento, bastante meh

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/api/v1/<palabra>")
def api(palabra):
    definition = df.loc[df["palabra"] == palabra]['definition'].squeeze()
    result_dict = {"palabra": palabra, 'definition': definition}
    return result_dict

if __name__ == "__main__":
    app.run(debug=True)