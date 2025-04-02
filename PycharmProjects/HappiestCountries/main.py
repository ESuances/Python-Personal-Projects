import streamlit as st
import plotly.express as px
import pandas as pd

st.title("In search for Happiness - By ESuances")
option_X = st.selectbox("Select the data for the X-axis",
                        ("GDP", "Happiness", "Generosity"))
option_Y = st.selectbox("Select the data for the Y-axis",
                        ("GDP", "Happiness", "Generosity"))

st.title(f"{option_X} and {option_Y}")

data = pd.read_csv("happy.csv")

match option_X:
    case "Happiness":
        x_array = data["happiness"]
    case "GDP":
        x_array = data["gdp"]
    case "Generosity":
        x_array = data["generosity"]

match option_Y:
    case "Happiness":
        y_array = data["happiness"]
    case "GDP":
        y_array = data["gdp"]
    case "Generosity":
        y_array = data["generosity"]


figure = px.scatter(x=x_array, y=y_array, labels={"x": f"{option_X}", "y": f"{option_Y}"})
st.plotly_chart(figure)
