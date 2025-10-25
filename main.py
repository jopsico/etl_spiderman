from extract import extract_data
from transform import transform_data
from load import load_data

def main():
    print("Iniciando ETL dos filmes do Spider-Man...")
    df_raw = extract_data()
    df_clean = transform_data(df_raw)
    load_data(df_clean)
    print("Processo ETL finalizado com sucesso!")

if __name__ == "__main__":
    main()
