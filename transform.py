import pandas as pd
from extract import extract_data

def transform_data():
    json_raw = extract_data()
    filmes = json_raw["description"]

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

    print("DataFrame criado dentro do transform.py")

    df["ano"] = pd.to_numeric(df["ano"], errors="coerce").astype("Int64")
    df["ranking"] = pd.to_numeric(df["ranking"], errors="coerce")

    df["classificacao"] = df["ranking"].apply(
        lambda r: "Blockbuster" if r < 2000 else
                  "Popular" if r < 10000 else
                  "Cult"
    )

    df = df.sort_values(by="ano")

    print("\n📊 Dados transformados:")
    print(df[["titulo", "ano", "classificacao"]])

    return df


if __name__ == "__main__":
    df_final = transform_data()
