import pandas as pd

def transform_data(df, nome_indicador):
    df["data"] = pd.to_datetime(df["data"], dayfirst=True)
    df["valor"] = df["valor"].astype(float)

    df = df.sort_values("data")

    df["indicador"] = nome_indicador

    df["variacao_mensal"] = df["valor"].pct_change()
    df["media_movel_3m"] = df["valor"].rolling(window=3).mean()

    return df