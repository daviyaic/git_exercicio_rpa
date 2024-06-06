from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
 
driver = webdriver.Chrome(options=options)
driver.get("https://br.investing.com/currencies/usd-brl")
 
sleep(8)
dolar = driver.find_element(By.CLASS_NAME, "text-5xl/9 font-bold text-[#232526] md:text-[42px] md:leading-[60px]").text
tempo = driver.find_element(By.TAG_NAME, 'time').text
driver.close()
dolar = dolar.replace(',','.')

print(dolar)
print(tempo)

from datetime import datetime

data_atual = datetime.now()
data_atual = data_atual.strftime("%Y-%m-%d")

horario = tempo.split()[3]

print(data_atual)
print(horario)

import psycopg2

conn = psycopg2.connect(
    host='pg-323b90ad-davi-955e.e.aivencloud.com',
    port='27366',
    dbname="defaultdb",
    user="avnadmin",
    password="AVNS_palAwjGYG_WtL1R0SM3"
)
cur = conn.cursor()

cur.execute(f"call inserir_cotacao_dolar('{data_atual}','{horario}',{dolar})")    

conn.commit()

cur.execute("SELECT * FROM cotacao_dolar")

rows = cur.fetchall()
for row in rows:
    print(row)

conn.commit()
