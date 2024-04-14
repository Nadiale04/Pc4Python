import requests
import sqlite3
try:
    cantidad = int(input("Ingrese la cantidad de Bitcoins: "))
except ValueError:
       print("Ha ocurrido un error, introduce bien el número")
       exit()
       

url= "https://api.coindesk.com/v1/bpi/currentprice.json"

response = requests.get(url)
datos = response.json()

precio_dolares = datos['bpi']['USD']['rate']
precio_gbp = datos['bpi']['GBP']['rate']
precio_euro = datos['bpi']['EUR']['rate']

url= "https://api.coindesk.com/v1/bpi/currentprice.json"

sentencia = ('''CREATE TABLE IF NOT EXISTS bitcoin (
                    fecha TEXT PRIMARY KEY,
                    precio USD DECIMAL,
                    precio GBP DECIMAL,
                    precio EUR DECIMAL,
                    precio PEN DECIMAL
                )''')
