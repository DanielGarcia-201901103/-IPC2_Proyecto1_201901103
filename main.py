from tkinter import filedialog
import sys
from tkinter.messagebox import showerror, showinfo, showwarning
from xml.dom import minidom
from Lista import Lista
from organismo import Organismo
from muestra import Muestra
from celdaViva import CeldaViva
#variables globales
lista_Organismos = Lista()
lista_Muestras = Lista()

# leer archivo xml
def cargarArchivo():
    #contadores para saber las cantidades
    contadorCantidad_MaxOrganismo = 0
    contadorMuestra = 0
    contadorCeldaV =0

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
            showerror(title="Error", message="El tamaño maximo de organismos es: 1000 \nPorfavor ingrese menos organismos")
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
            if ((int(celdaViva_fila.firstChild.data) <= int(muestra_filas.firstChild.data)) and (int(celdaViva_columna.firstChild.data) <= int(muestra_columnas.firstChild.data))):
                lista_CeldasVivas.addFinalNode(objetoCeldaViva)
                contadorCeldaV = contadorCeldaV + 1
            else:
                showerror(title="Error", message="La celda Viva debe estar dentro del valor máximo de:\nfilas: 10000\ncolumnas: 10000 \n El codigo del organismo de la celda viva con el dato de la fila o columna que supera el máximo es:\n"+ str(celdaViva_codigoOrganismo.firstChild.data))
                break

        if ((int(muestra_filas.firstChild.data) <= 10000) and (int(muestra_columnas.firstChild.data) <= 10000)):
            #enviando los parametros al objeto y enviando el objeto a la lista
            objetoMuestra = Muestra(str(muestra_codigo.firstChild.data), str(muestra_descripcion.firstChild.data), str(muestra_filas.firstChild.data), str(muestra_columnas.firstChild.data),lista_CeldasVivas)
            #Agregando muestra a la lista de muestras
            lista_Muestras.addFinalNode(objetoMuestra)
            contadorMuestra +=1
        else:
            showerror(title="Error", message="La muestra solo puede tener como máximo:\nfilas: 10000\ncolumnas: 10000\nEl codigo de la muestra con el dato de la fila o columna que supera el máximo es:\n"+ str(muestra_codigo.firstChild.data))
            break

    showinfo(title="Guardado", message="Archivo leído exitosamente")
    #imprimiendo datos
    #lista_Organismos.printList()
    #crear otro metodo imprimir para la lista de muestras
    #lista_Muestras.printList()

def listaCeldasVivas():
    pass

def actualizarMuestra():
    pass

def crearMuestra():
    pass

def menuListaMuestras():
    while True:    
        try:
            print("\n------- Menu Lista de Muestras --------\n")
            #mostrar el listado de las muestras y elegir una opcion

            lista_Muestras.printListMuestra()

            print("\n1. Mostrar lista de celdas Vivas"+"\n2. Actualizar Muestra"+"\n3. Crear Muestra"+"\n4. Regresar")
            # recibe la opcion ingresada y la guarda como entero
            opcion2 = int(input("Ingrese una opcion: "))
            print()
            if opcion2 == 1:
                listaCeldasVivas()
            elif opcion2 == 2:
                actualizarMuestra()
            elif opcion2 == 3:
                crearMuestra()
            elif opcion2 == 4:
                break
            else:
                print("Ingrese una opcion correcta")
        except ValueError:
            print("\nPor favor ingrese solo numeros")

def guardarArchivo():
    pass
def inicializacion():
    pass

if __name__ == '__main__':
    try:
        while True:
                print("------- Menu Principal --------")
                print("1. Cargar archivo xml")
                # esto permite volver a cargar un archivo nuevo desde 0, pero no se deben perder los datos anterioresf
                print("2. Lista de muestras")
                print("3. Guardar archivo en xml")
                print("4. Inicialización")
                print("5. Salir")
                # recibe la opcion ingresada y la guarda como entero
                opcion = int(input("Ingrese una opcion: "))
                print()
                if opcion == 1:
                    cargarArchivo()
                elif opcion == 2:
                    menuListaMuestras()
                elif opcion == 3:
                    guardarArchivo()
                elif opcion == 4:
                    inicializacion()
                elif opcion == 5:
                    sys.exit()
                else:
                    print("Ingrese una opcion correcta")
    except ValueError:
            print("\nPor favor ingrese solo numeros")
"""
cargar archivo -> Ya está hecha
seleccionar muestra -> colocar algun organismo de la muestra -> validar la forma en que cambia la muestra e indicar cuando la muestra ya no puede ser modificada
actualizar-> informacion de la muestra 
crear -> muestra con los cambios introducidos
guardar archivo ->con las muestras actualizadas con la misma estructura del archivo de entrada
Inicializacion -> cargar un archivo desde 0, si se carga y existen datos cargados anteriormente deben continuar existiendo y debe aumentar la informacion en el sistema
"""