import requests
import sqlite3

def bitcoin(moneda):
    url= "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url)
    data=response.json()
    precio=data['bpi'][moneda]['rate']
    return precio

def tipo_cambio():
    url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat'
    response=requests.get(url)
    data=response.json()
    tipo_cambio_pen= data['dolar']['compra']
    return tipo_cambio_pen

conn = sqlite3.connect('base.db')
cursor = conn.cursor()

sentencia=('''CREATE TABLE IF NOT EXISTS bitcoin (
                    fecha TEXT PRIMARY KEY,
                    precio_usd DECIMAL,
                    precio_gbp DECIMAL,
                    precio_eur DECIMAL,
                    precio_pen DECIMAL
                )''')

precio_usd=bitcoin('USD')
precio_gbp=bitcoin('GBP')
precio_eur=bitcoin('EUR')
tipo_cambio_pen=tipo_cambio()

precio_pen = precio_usd * tipo_cambio_pen


cursor.execute("INSERT INTO bitcoin VALUES (?, ?, ?, ?)", (precio_usd, precio_gbp, precio_eur, precio_pen))
conn.commit()

cursor.execute('SELECT precio_pen, precio_eur FROM bitcoin')
row = cursor.fetchone()
precio_compra_pen = 10 * row[0]
precio_compra_eur = 10 * row[1]

print(f"Precio de comprar 10 bitcoins en PEN: {precio_compra_pen} PEN")
print(f"Precio de comprar 10 bitcoins en EUR: {precio_compra_eur} EUR")

conn.close()