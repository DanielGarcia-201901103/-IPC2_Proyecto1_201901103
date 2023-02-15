from tkinter import filedialog
from xml.dom import minidom
from organismo import Organismo
from muestra import Muestra
from celdaViva import CeldaViva
from lista import Lista

#variables globales
lista_Organismos = Lista()
lista_Muestras = Lista()

# leer archivo xml
def cargarArchivo():
    #contadores para saber las cantidades de organismos
    contadorCantidad_MaxOrganismo = 0

    #abre ventana para seleccionar archivo
    urlarchivo = filedialog.askopenfilename(initialdir="./",title="Seleccione un Archivo", filetypes=(("xml","*.xml"),("all files","*.*")))
    #urlarchivo = input()
    
    documento = minidom.parse(urlarchivo)

    #Se obtienen los datos de la lista organismos
    organismosdoc = documento.getElementsByTagName("organismo")
    for organismodoc in organismosdoc:
        contadorCantidad_MaxOrganismo +=1
        organismo_codigo = organismodoc.getElementsByTagName("codigo")[0]
        organismo_nombre = organismodoc.getElementsByTagName("nombre")[0]
            #print(organismo_codigo.firstChild.data)
            #print(organismo_nombre.firstChild.data)
        if contadorCantidad_MaxOrganismo <= 1000:
            #enviando los parametros al objeto y enviando el objeto a la lista
            objetoOrganismo = Organismo(str(organismo_codigo.firstChild.data), str(organismo_nombre.firstChild.data))
            #Agregando organismo a la lista de organismos
            lista_Organismos.addFinalNode(objetoOrganismo)
        else:
            print("El tamaño maximo de organismos es: 1000 \nPorfavor no ingrese una cantidad mayor")
            break
    #Se obtienen los datos de listado muestras
    muestrasdoc1 = documento.getElementsByTagName("muestra")
    for muestradoc in muestrasdoc1:
        muestra_codigo = muestradoc.getElementsByTagName("codigo")[0]
        muestra_descripcion = muestradoc.getElementsByTagName("descripcion")[0]
        muestra_filas = muestradoc.getElementsByTagName("filas")[0]
        muestra_columnas = muestradoc.getElementsByTagName("columnas")[0]
        #recorriendo la listaa de celdas vivas
        celdasvivasdoc = documento.getElementsByTagName("celdaViva")
        lista_CeldasVivas = Lista()

        for celdavivadoc in celdasvivasdoc:
            celdaViva_fila = celdavivadoc.getElementsByTagName("fila")[0]
            celdaViva_columna = celdavivadoc.getElementsByTagName("columna")[0]
            celdaViva_codigoOrganismo = celdavivadoc.getElementsByTagName("codigoOrganismo")[0]
            #.......enviando los parametros al objeto y enviando el objeto a la lista
            objetoCeldaViva = CeldaViva(str(celdaViva_fila.firstChild.data), str(celdaViva_columna.firstChild.data), str(celdaViva_codigoOrganismo.firstChild.data))
            #Agregando celda viva a la lista de celdas vivas
            lista_CeldasVivas.addFinalNode(objetoCeldaViva)

        if ((int(muestra_filas.firstChild.data) <= 10000) and (int(muestra_columnas.firstChild.data) <= 10000)):
            #enviando los parametros al objeto y enviando el objeto a la lista
            objetoMuestra = Muestra(str(muestra_codigo.firstChild.data), str(muestra_descripcion.firstChild.data), str(muestra_filas.firstChild.data), str(muestra_columnas.firstChild.data),lista_CeldasVivas)
            #Agregando muestra a la lista de muestras
            lista_Muestras.addFinalNode(objetoMuestra)
        else:
            print("La muestra solo puede tener como máximo:\nfilas: 10000\ncolumnas: 10000 \n")
            print("El codigo de la muestra con el dato de la fila o columna que supera el máximo es:\n"+ str(muestra_codigo.firstChild.data))
    #imprimiendo datos
    lista_Organismos.printList()
    #lista_Muestras.printList()

if __name__ == '__main__':
    # menu    '''
# '''
    while True:
        print("------- Menu Principal --------")
        print("1. Cargar archivo xml")
        # esto permite volver a cargar un archivo nuevo desde 0, pero no se deben perder los datos anterioresf
        print("2. Mostrar datos")
        print("3. Guardar archivo xml")
        print("4. Salir")
        # recibe la opcion ingresada y la guarda como entero
        opcion = int(input("Ingrese una opcion: "))
        print()
        if opcion == 1:
            cargarArchivo()
        elif opcion == 2:
            
            print("opcion 2")
        elif opcion == 3:
            print("opcion 3")
        elif opcion == 4:
            break
        else:
            print("Ingrese una opcion correcta")
