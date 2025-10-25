import pandas as pd

def transform_data(df):
    df["ano"] = pd.to_numeric(df["ano"], errors="coerce").astype("Int64")
    df["ranking"] = pd.to_numeric(df["ranking"], errors="coerce")

    df["classificacao"] = df["ranking"].apply(
        lambda r: "Blockbuster" if r < 2000 else "Popular" if r < 10000 else "Cult"
    )

    df = df.sort_values(by="ano")

    print("Dados transformados:")
    print(df[["titulo", "ano", "classificacao"]])
    return df
