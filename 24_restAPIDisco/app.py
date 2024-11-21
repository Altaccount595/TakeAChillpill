import urllib.request
import json
import webbrowser

with open('catAPIKey.txt', 'r') as file:
    api_key = file.read().strip()

# URL for the Cat API
url = "https://api.thecatapi.com/v1/images/search"

# Set the request headers with your API key
headers = {
    'x-api-key': api_key
}

# Create the request with the headers
request = urllib.request.Request(url, headers=headers)

# Fetch the data from the API using urllib
with urllib.request.urlopen(request) as response:
    # Read and decode the response
    data = response.read().decode('utf-8')

    # Parse the JSON data
    cat_data = json.loads(data)

    # Extract the image URL
    image_url = cat_data[0]['url']

    # Open the image URL in the default web browser
    webbrowser.open(image_url)
#purrrrrrrrrrrrrrfect
