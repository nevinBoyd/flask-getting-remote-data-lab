import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        # Send GET request and return raw response body (bytes)
        response = requests.get(self.url)
        return response.content
      
    def load_json(self):
        # Use get_response_body, convert bytes to Python data with json.loads
        data = self.get_response_body()
        return json.loads(data)