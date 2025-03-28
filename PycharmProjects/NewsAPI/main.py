# No Front end, pure backend
# So, we built the program from the input data to the Output
# Input -> Output
# The input data comes from the API this time
import requests
from send_email import sendEmail

url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=d379715cbdb344548f8c01adbcd96e42&language=en"
API = "d379715cbdb344548f8c01adbcd96e42"

# Made a request
request = requests.get(url)

# Get a dictionary wth data
content = request.json()

# Access the article title and description
body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] \
               + "\n" + article["url"] + 2 * "\n"

body = body.encode("utf-8")
sendEmail(body)