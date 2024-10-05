import requests
import json

class GetRequester:

    def __init__(self, url):
        # initialize with a url
        self.url = url

    def get_response_body(self):
        # Sends a GET request to the provided URL
        response=requests.get(self.url)
         # Return the raw response text (body)
        return response.content


    # def get_response_body(self):
    # # Sends a GET request to the provided URL
    #     response = requests.get(self.url)

    #     try:
    #          # Check if the response can be returned as JSON
    #          return response.json()
    #     except requests.exceptions.JSONDecodeError:
    #         # Return raw text if not JSON
    #         return response.text
    
   


    def load_json(self):
        # get response body
        response_body = self.get_response_body().decode('utf-8')  # decode bytes to string
        try:
            # Convert the response body to JSON (list/dict) and return it
            return json.loads(response_body)
        except json.JSONDecodeError:
            # Handle cases where response is not valid JSON
            return None