import requests
import pandas as pd
from datetime import datetime, timedelta

def extract_data(codigo_serie):
    hoje = datetime.today()
    dez_anos_atras = hoje - timedelta(days=365*10)

    data_inicial = dez_anos_atras.strftime("%d/%m/%Y")
    data_final = hoje.strftime("%d/%m/%Y")

    url = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo_serie}/dados?formato=json&dataInicial={data_inicial}&dataFinal={data_final}"

    response = requests.get(url)
    response.raise_for_status()

    df = pd.DataFrame(response.json())

    return df