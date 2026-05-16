from sqlalchemy import create_engine, text
import pandas as pd


def load_data(df):
    user = "postgres"
    password = "visor4532"
    host = "localhost"
    port = "5432"
    database = "etl_bacen"

    engine = create_engine(
        f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"
    )

   
    with engine.connect() as conn:
        try:
            # pega última data
            query = text("SELECT MAX(data) FROM indicadores_economicos")
            result = conn.execute(query).fetchone()
            ultima_data = result[0]

        except:
            ultima_data = None

    if ultima_data:
        df = df[df["data"] > ultima_data]

    if not df.empty:
        df.to_sql("indicadores_economicos", engine, if_exists="append", index=False)
        print(f"{len(df)} novos registros inseridos.")
    else:
        print("Nenhum dado novo para inserir.")