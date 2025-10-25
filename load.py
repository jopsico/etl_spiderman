from sqlalchemy import create_engine

def load_data(df):
    user = "etl_user"         # seu usuário
    password = "12345"        # sua senha
    host = "localhost"        # IP do servidor
    port = "5432"             # porta padrão do PostgreSQL
    database = "spiderman_etl"

    engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}")

    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].astype(str).apply(lambda x: x.encode('utf-8', errors='ignore').decode('utf-8', errors='ignore'))

    df.to_sql("filmes_spiderman", con=engine, schema="etl_user_schema", if_exists="append", index=False)

    print("Dados carregados com sucesso no PostgreSQL!")


