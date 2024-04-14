import requests
import sqlite3

url = "https://api.apis.net.pe/v1/tipo-cambio-sunat?date={}-{}-{}"

sentencia = ('''CREATE TABLE IF NOT EXISTS sunat_info (
                    fecha TEXT PRIMARY KEY,
                    compra DECIMAL,
                    venta DECIMAL
                )''')

with sqlite3.connect('base.db') as conexion:
    cursor = conexion.cursor()
    cursor.execute(sentencia)
    conexion.commit()

for year in range(2023, 2024):
    for month in range(1, 13):
        for day in range(1, 32):
            urlcompleto=url.format(year, month, day)
            response=requests.get(url)

            try:
                data = response.json()
                fecha = data['fecha']
                compra = data['dolar']['compra']
                venta = data['dolar']['venta']

                with sqlite3.connect('base.db') as conexion:
                    cursor = conexion.cursor()
                    cursor.execute("INSERT INTO sunat_info VALUES (?, ?, ?)", (fecha, compra, venta))
                    conexion.commit()

            except (KeyError, TypeError, requests.exceptions.JSONDecodeError):
                continue
