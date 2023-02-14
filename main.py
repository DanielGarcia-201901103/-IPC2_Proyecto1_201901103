from tkinter import filedialog
from xml.dom import minidom
from organismo import Organismo
from muestra import Muestra
from celdaViva import CeldaViva
from lista import Lista

# leer archivo xml
def cargarArchivo():
    
    urlarchivo = filedialog.askopenfilename(initialdir="./",title="Seleccione un Archivo", filetypes=(("xml","*.xml"),("all files","*.*")))
    #urlarchivo = input()
    
    documento = minidom.parse(urlarchivo)

    #Se obtienen los datos de la lista organismos
    organismosdoc = documento.getElementsByTagName("organismo")
    for organismodoc in organismosdoc:
        organismo_codigo = organismodoc.getElementsByTagName("codigo")[0]
        organismo_nombre = organismodoc.getElementsByTagName("nombre")[0]
            #print(organismo_codigo.firstChild.data)
            #print(organismo_nombre.firstChild.data)
        
        #enviando los parametros al objeto y enviando el objeto a la lista
        objetoOrganismo = Organismo(organismo_codigo, organismo_nombre)
        #Agregando organismo a la lista de organismos

    
    #Se obtienen los datos de listado muestras
    muestrasdoc1 = documento.getElementsByTagName("muestra")
    for muestradoc in muestrasdoc1:
        muestra_codigo = muestradoc.getElementsByTagName("codigo")[0]
        muestra_descripcion = muestradoc.getElementsByTagName("descripcion")[0]
        muestra_filas = muestradoc.getElementsByTagName("filas")[0]
        muestra_columnas = muestradoc.getElementsByTagName("columnas")[0]
        #recorriendo la listaa de celdas vivas
        celdasvivasdoc = documento.getElementsByTagName("celdaViva")
        for celdavivadoc in celdasvivasdoc:
            celdaViva_fila = celdavivadoc.getElementsByTagName("fila")[0]
            celdaViva_columna = celdavivadoc.getElementsByTagName("columna")[0]
            celdaViva_codigoOrganismo = celdavivadoc.getElementsByTagName("codigoOrganismo")[0]
            #.......enviando los parametros al objeto y enviando el objeto a la lista
            objetoCeldaViva = CeldaViva(celdaViva_fila, celdaViva_columna, celdaViva_codigoOrganismo)
            #Agregando celda viva a la lista de celdas vivas

        #enviando los parametros al objeto y enviando el objeto a la lista
        objetoMuestra = Muestra(muestra_codigo, muestra_descripcion, muestra_filas, muestra_columnas)
        #Agregando muestra a la lista de muestras
        
    
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
        print("2. Guardar archivo xml")
        print("3. Salir")
        # recibe la opcion ingresada y la guarda como entero
        opcion = int(input("Ingrese una opcion: "))
        print()
        if opcion == 1:
            cargarArchivo()
        elif opcion == 2:
            print("opcion 2")
        elif opcion == 3:
            break
        else:
            print("Ingrese una opcion correcta")
