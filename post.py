import requests
from get_token import token
# import validators

class integration_post:
    def __init__(self, getUrl, data, token):
        self.getUrl = getUrl
        self.token = token
        self.data = data
    
    def post(self):
        response = requests.post(url=self.getUrl, json=data, headers=self.token)

        if response.status_code >= 400 and response.status_code <= 499:
            return f'Error {response.status_code}, {response.text} {response.reason};'
        
        elif response.status_code >= 200 and response.status_code <= 299:
            return f'Sucesso: {response.status_code}, {response.text} {response.reason};'
        
        else:
            return response.status_code, response.reason

            
if __name__ == "__main__":

    url = "http://127.0.0.1:8000/atracoes/"

    data = {
        "nome": "MC Donizete",
        "descricao": "Entrevista com MC doni.",
        "horario_funcionamento": "21h",
        "idade_minima": 20
    }

    headers = {
        'Authorization': token
    }
    
    x = integration_post(url, data, headers)
    print(x.post())
