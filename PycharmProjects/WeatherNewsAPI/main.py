from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__) # This takes the literal name of the file without .py

variable = "Hello there"

stations = pd.read_csv("data_small/stations.txt", skiprows=17)
stations = stations[["STAID", "STANAME                                 "]] # This is so that we only show those specific rows in the page.

@app.route('/') #This will be the starting page.
def home():
    return render_template('home.html', data=stations.to_html())


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    # Construct the file path
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    # Read the CSV file, considering the specific structure of your file
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"], sep=",", engine="python", skipfooter=1)

    # Directly use the 'date' string as it is already in the correct format
    formatted_date = pd.to_datetime(date)

    # Filter the DataFrame for the specified date
    filtered_df = df[df['    DATE'] == formatted_date]

    # Check if there are any rows after filtering
    if not filtered_df.empty:
        temperature = filtered_df['   TG'].iloc[0] / 10
    else:
        # Handle the case where no data is found for the given date
        temperature = None  # Or set a default value or message

    # Prepare the result dictionary
    weather_result = {
        "station": station,
        "date": date,
        "temperature": temperature
    }

    # Convert the result to JSON and return
    return jsonify(weather_result)

@app.route("/api/v1/<station>")
def all_data(station):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    result = df.to_dict(orient="records") # We get the selected data and we manipulate it to display as we please
    return result

@app.route("/api/v1/yearly/<station>/<year>") #This is another way to get the data and to not interfier with other routes to get the data-
def yearly(station, year):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20)
    df["    DATE"] = df["    DATE"].astype(str)
    result = df[df["    DATE"].str.startswith(str(year))].to_dict(orient="records")
    return result

if __name__ == "__main__": # This makes it so that only when we run this file, this code is actually executed, meaning creating the site on Flask
    app.run(debug=True)