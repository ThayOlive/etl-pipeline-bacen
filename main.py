from scripts.extract import extract_data
from scripts.transform import transform_data
from scripts.load import load_data
from scripts.logger import setup_logger
import pandas as pd

def run_pipeline():
    logger = setup_logger()

    try:
        logger.info("Iniciando pipeline")

        indicadores = {
            "selic": 11,
            "ipca": 433,
            "dolar": 1
        }

        dfs = []

        for nome, codigo in indicadores.items():
            logger.info(f"Extraindo {nome}")
            df = extract_data(codigo)

            logger.info(f"Transformando {nome}")
            df = transform_data(df, nome)

            dfs.append(df)

        df_final = pd.concat(dfs)

        logger.info("Carregando dados no banco")
        load_data(df_final)

        logger.info("Pipeline finalizado com sucesso")

    except Exception as e:
        logger.error(f"Erro no pipeline: {str(e)}")
        raise

if __name__ == "__main__":
    run_pipeline()