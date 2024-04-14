import requests

url = 'https://api.coindesk.com/v1/bpi/currentprice.json'

response = requests.get(url)
data = response.json()

with open('precio_bitcoin.txt', mode='w', encoding='utf-8') as f:
    for h, moneda in data['bpi'].items():
        TipoMoneda = moneda['code']
        Valor = moneda ['rate']
        Descripcion = moneda['description']

        f.writelines([f'>>>>>>>>>>>>>>> {TipoMoneda} <<<<<<<<<<<<<<<\n', f'Valor: {Valor}\n', f'Descripcion: {Descripcion}\n\n'])