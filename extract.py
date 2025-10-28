import requests

BASE_URL = "https://imdb.iamidiotareyoutoo.com/search?q=Spiderman"

def extract_data():
    response = requests.get(BASE_URL)
    response.raise_for_status()
    data = response.json()
    print("JSON bruto extraído com sucesso!")
    return data

