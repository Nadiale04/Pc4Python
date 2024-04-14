import requests
import os
import zipfile

url='https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}

response = requests.get(url, headers=headers)

with open('cachorro.jpg', 'wb') as f:
    f.write(response.content)
    pass


with zipfile.ZipFile('archivo.zip', 'w') as zip:
    zip.write('cachorro.jpg', 'cachorro.jpg')

if not os.path.isdir('./unzip'): 
    os.mkdir('./unzip') 

with zipfile.ZipFile('archivo.zip', 'r') as zip_ref:
    zip_ref.extractall(path='./unzip')