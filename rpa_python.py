from time import sleep

from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
 
driver = webdriver.Chrome(options=options)
driver.get("https://www.google.com/search?q=dolar&rlz=1C1GCEU_pt-BRBR1077BR1077&oq=dolar&gs_lcrp=EgZjaHJvbWUqDggAEEUYJxg7GIAEGIoFMg4IABBFGCcYOxiABBiKBTIMCAEQABhDGIAEGIoFMg0IAhAAGIMBGLEDGIAEMg0IAxAAGIMBGLEDGIAEMgwIBBAAGEMYgAQYigUyDAgFEAAYQxiABBiKBTIKCAYQABixAxiABDIPCAcQABhDGLEDGIAEGIoFMgwICBAAGEMYgAQYigUyBwgJEAAYjwLSAQk1MDI4OGowajeoAgCwAgA&sourceid=chrome&ie=UTF-8")
 
sleep(3)
dolar = driver.find_element('xpath','//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').text
tempo = driver.find_element('xpath','//*[@id="knowledge-currency__updatable-data-column"]/div[2]/span').text
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
    dbname="dbcotacoes",
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