import schedule
import time
from main import run_pipeline

def job():
    print("Rodando pipeline automático...")
    run_pipeline()

schedule.every(1).minutes.do(job)  # pra testar rápido

print("Scheduler iniciado...")

while True:
    schedule.run_pending()
    time.sleep(60)