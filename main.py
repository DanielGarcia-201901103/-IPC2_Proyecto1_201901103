from xml.dom import minidom

# leer archivo xml
def cargarArchivo():
    print('Ingrese la url del archivo:')
    urlarchivo = input()
    documento = minidom.parse(urlarchivo)
    organismo = documento.getElementsByTagName("codigo")[0]
    print(organismo.firstChild.data)

'''
Los datos iniciales serán cargados en un archivo XML, este archivo contendrá el listado de 
los organismos que podrán ser incluidos en las muestras.  Por cada muestra se indicará la 
cantidad M (filas) y la cantidad N (columnas), y luego se identificará cada celda que tenga un 
organismo vivo y el nombre del organismo vivo que contiene.
'''
if __name__ == '__main__':
    # menu    '''
# '''
    while True:
        print("------- Menu Principal --------")
        print("1. Cargar archivo xml")
        # esto permite volver a cargar un archivo nuevo desde 0, pero no se deben perder los datos anterioresf
        print("1. Reiniciar programa")
        print("1. Guardar archivo xml")
        print("2. Salir")
        # recibe la opcion ingresada y la guarda como entero
        opcion = int(input("Ingrese una opcion: "))
        print()
        if opcion == 1:
            cargarArchivo()

        elif opcion == 2:
            break
        else:
            print("Ingrese una opcion correcta")
