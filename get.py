import requests
from get_token import token
# import validators
import json

class integration_get:
    def __init__(self, getUrl, token):
        self.getUrl = getUrl
        self.token = token
    
    def get(self):
        response = requests.get(url=self.getUrl, headers=self.token)

        if response.status_code >= 400 and response.status_code <= 499:
            return f'Error {response.status_code}, {response.text} {response.reason};'
        
        elif response.status_code >= 200 and response.status_code <= 299:
            return f'Sucesso: {response.status_code}, {response.json()}, {response.reason};'
        
        else:
            return response.status_code, response.reason

            
if __name__ == "__main__":

    url = "http://127.0.0.1:8000/atracoes/"

    headers = {
        'Authorization': token
    }
    
    x = integration_get(url, headers)
    print(x.get())

