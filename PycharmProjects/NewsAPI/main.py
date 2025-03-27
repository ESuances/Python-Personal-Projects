# No Front end, pure backend
# So, we built the program from the input data to the Output
# Input -> Output
# The input data comes from the API this time
import requests

url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=d379715cbdb344548f8c01adbcd96e42"
API = "d379715cbdb344548f8c01adbcd96e42"

# Made a request
request = requests.get(url)

# Get a dictionary wth data
content = request.json()

# Access the article title and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])