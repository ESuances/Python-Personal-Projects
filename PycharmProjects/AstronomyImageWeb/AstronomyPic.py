import requests
import streamlit as st


# I was going to safe this key in a not included git file, but since I want to show this page and I'm not sure on how to make it safe, f it
APIKEY = "XwvDfj3KCHdqKSaHshdcleaLWRVlMGxrCFvkbFXw"
url = "https://api.nasa.gov/planetary/apod?api_key=XwvDfj3KCHdqKSaHshdcleaLWRVlMGxrCFvkbFXw"

# Make the request for the information from the PAI
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article tittle and description
# I just wanted to know which data to inlcude
# print(content)
# print(content['title'] + '\n') # Title of the image
# print(content['url'] + '\n') # Image URL
# print(content['explanation'] + '\n') # Description of the photo
# print(content['date'] + '\n') # Date of the image

title = content['title']

st.set_page_config(layout="centered")

col1, col2, = st.columns(2)



with col1:
    st.text("Astronomy picture of the day! - By ESuances using Nasa's API")
    st.text(f"Today's date is {content['date']}")
    st.markdown(f"![Alt Text]({content['url']})")
with col2:
    st.title(title)
    st.text(content['explanation'])

st.text("Thank you for comming! see you tomorrow! :D")
st.markdown("![Alt Text](https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif)")
