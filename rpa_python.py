from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
 
driver = webdriver.Chrome(options=options)
driver.get("https://br.investing.com/currencies/usd-brl")
 
sleep(8)
dolar = driver.find_element(By.CSS_SELECTOR, "#__next > div.md\:relative.md\:bg-white > div.relative.flex > div.grid.flex-1.grid-cols-1.px-4.pt-5.font-sans-v2.text-\[\#232526\].antialiased.xl\:container.sm\:px-6.md\:grid-cols-\[1fr_72px\].md\:gap-6.md\:px-7.md\:pt-10.md2\:grid-cols-\[1fr_420px\].md2\:gap-8.md2\:px-8.xl\:mx-auto.xl\:gap-10.xl\:px-10 > div.min-w-0 > div.flex.flex-col.gap-6.md\:gap-0 > div.flex.gap-6 > div.flex-1 > div.mb-3.flex.flex-wrap.items-center.gap-x-4.gap-y-2.md\:mb-0\.5.md\:gap-6 > div.text-5xl\/9.font-bold.text-\[\#232526\].md\:text-\[42px\].md\:leading-\[60px\]").text
tempo = driver.find_element(By.CSS_SELECTOR, '#__next > div.md\:relative.md\:bg-white > div.relative.flex > div.grid.flex-1.grid-cols-1.px-4.pt-5.font-sans-v2.text-\[\#232526\].antialiased.xl\:container.sm\:px-6.md\:grid-cols-\[1fr_72px\].md\:gap-6.md\:px-7.md\:pt-10.md2\:grid-cols-\[1fr_420px\].md2\:gap-8.md2\:px-8.xl\:mx-auto.xl\:gap-10.xl\:px-10 > div.min-w-0 > div.flex.flex-col.gap-6.md\:gap-0 > div.flex.gap-6 > div.flex-1 > div.flex.items-center.gap-2 > div.flex.items-center.gap-1.text-xs\/4.text-\[\#5B616E\] > time').text
driver.close()
dolar = dolar.replace(',','.')

print(dolar)
print(tempo)

from datetime import datetime

data_atual = datetime.now()
data_atual = data_atual.strftime("%Y-%m-%d")

horario = tempo

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
