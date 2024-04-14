ruta=input('Indroduce una ruta de archivo .py: ')
try:
    if ruta[-3:]=='.py':
        with open(ruta, 'r') as archivo:
            contenido = archivo.read()
            lineascodigo = 0
            for linea in contenido.split('\n'):
                linea_limpia = linea.strip()
                if linea_limpia and not linea_limpia[0]=='#':
                    lineascodigo += 1
            print(f'El número de líneas de código es de {lineascodigo}')
    else:
        print("El archivo no tiene extensión .py.")
        pass
except FileNotFoundError:
    print("No se encontró el archivo o la ruta es inválida.")


   