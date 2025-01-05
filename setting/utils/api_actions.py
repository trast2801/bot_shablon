import requests

API_URL = 'http://127.0.0.1:8000/accounts/'

def get_path(code):
    response = requests.get(API_URL + f"get-file/?code={code}")
    if response:
        return response.json()
    return None

