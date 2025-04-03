import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days by ESuances")
place = st.text_input("Location: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:  # Ensure a location is entered before fetching data
    try:
        filtered_data = get_data(place, days)

        if option == "Temperature":
            # Extract temperatures and dates from the original data
            temperatures = [entry["main"]["temp"] / 10 for entry in filtered_data]
            dates = [entry["dt_txt"] for entry in filtered_data]
            # Create the plot with correct x and y values
            figure = px.line(x=dates, y=temperatures,
                             labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        elif option == "Sky":
            # Extract sky conditions and corresponding dates
            images = {"Clear":"images/clear.png", "Clouds":"images/cloud.png",
                      "Rain":"images/rain.png", "Snow":"images/snow.png"}
            sky_conditions = [entry["weather"][0]["main"] for entry in filtered_data]
            images_paths = [images[condition] for condition in sky_conditions]
            dates = [entry["dt_txt"] for entry in filtered_data]
            st.image(images_paths, width=115)
            st.write(sky_conditions)  # Placeholder for actual images
    except KeyError:
        st.text(f"Sorry, there is no location called {place} in our database, please try again")