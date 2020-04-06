# USAGE
# python simple_request.py

# import the necessary packages
import requests

# initialize the CHATSPACE REST API endpoint URL along with the input
# image path
CHATSPACE_REST_API_URL = "http://localhost:3000/proofread"

text = "아버지가방에들어가신다"
payload = {"text": text}

# submit the request
r = requests.post(CHATSPACE_REST_API_URL, json=payload).json()

# ensure the request was sucessful
if r["success"]:
    # loop over the predictions and display them
    print(r["spaced_text"])

# otherwise, the request failed
else:
    print("Request failed")
