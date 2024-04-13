import requests

try:
    cantidad = int(input("Ingrese la cantidad de Bitcoins: "))
except ValueError:
       print("Ha ocurrido un error, introduce bien el número")
       exit()
       

url= "https://api.coindesk.com/v1/bpi/currentprice.json"

response = requests.get(url)

datos = response.json()

precio_dolares = datos['bpi']['USD']['rate']


precio_dolares = float(precio_dolares.replace(',', ''))

total_dolares = cantidad * precio_dolares

print(f'Precio en dólares (USD): {precio_dolares}')
print(f'Tienes ${ total_dolares:.4f} USD')