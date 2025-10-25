import requests
import pandas as pd

BASE_URL = "https://imdb.iamidiotareyoutoo.com/search?q=Spiderman"

def extract_data():
    response = requests.get(BASE_URL)
    response.raise_for_status()
    data = response.json()

    filmes = data["description"]

    df = pd.DataFrame([
        {
            "titulo": filme["#TITLE"],
            "ano": filme["#YEAR"],
            "atores": filme["#ACTORS"],
            "id_imdb": filme["#IMDB_ID"],
            "ranking": filme["#RANK"],
            "aka": filme["#AKA"],
            "url_imdb": filme["#IMDB_URL"],
            "poster": filme["#IMG_POSTER"],
            "largura_poster": filme["photo_width"],
            "altura_poster": filme["photo_height"]
        }
        for filme in filmes
    ])

    print("Dados extraídos com sucesso!")
    return df
