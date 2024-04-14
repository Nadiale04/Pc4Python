def tabla_multiplicar():
    while True:
        try:
            numero = int(input('Introduce un número entero entre 1 y 10: '))
            if numero < 1 or numero > 10:
                print('El número debe estar entre 1 y 10. Intente de nuevo.')
                continue
            else:
                nombre_fichero = f'tabla-{numero}.txt'
                with open(nombre_fichero, 'w') as archivo:
                    for i in range(1, 13):
                        tabla = numero * i
                        archivo.write(f'{numero} x {i} = {tabla}\n')
                print(f"La tabla de multiplicar del número {numero} ha sido guardada en el archivo '{nombre_fichero}'.")
                return nombre_fichero
            
        except ValueError:
            print('Por favor, introduce un número entero válido.')

def Buscar_fichero():
    while True:
        try:
            numero=int(input('Introduce un número entero entre 1 y 10: '))
            if numero<1 or numero>10:
               continue 
            else:
                nombre_fichero = f'tabla-{numero}.txt'
                with open(nombre_fichero, 'r') as archivo:
                    data = archivo.read()
                    print(data)
                    break
        except FileNotFoundError:
            print(f"El archivo '{nombre_fichero}' no se encontró.")

def mostrar_linea():
    try:
        n=int(input('Introduce un número entero entre 1 y 10: '))
        m=int(input('Introduce un número entero entre 1 y 10: '))
        nombre_fichero = f'tabla-{n}.txt'
        with open(nombre_fichero, 'r') as archivo:
            lineas=archivo.readlines()
            if 1 <= m <=len(lineas):
                print(lineas[m-1])
            else:
                print("El número de línea está fuera de rango.")
    except FileNotFoundError:
        print(f"El archivo 'tabla-{n}.txt' no se encontró.")



def opciones():
    while True:
        print('''Menú interactivo
              1.Guardar fichero
              2.Leer fichero
              3.Mostrar línea de fichero
              4.Salir''')
        opcion=int(input('Seleccione una acción: '))
        if opcion == 1:
            nombredearchivo=tabla_multiplicar()
        elif opcion == 2:
            Buscar_fichero()
        elif opcion == 3:
            mostrar_linea()
        elif opcion == 4:
            print("Adiós")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

opciones()