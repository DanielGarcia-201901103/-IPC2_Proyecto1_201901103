from tkinter import filedialog
import sys
from tkinter.messagebox import showerror, showinfo, showwarning
from xml.dom import minidom
from Lista import Lista
from organismo import Organismo
from muestra import Muestra
from celdaViva import CeldaViva
import graphviz

# variables globales
lista_Organismos = Lista()
lista_Muestras = Lista()

filass = 0
columnass = 0
codigoMS = ""
descripcionMS = ""
lcv = Lista()

# leer archivo xml


def cargarArchivo():
    # contadores para saber las cantidades
    contadorCantidad_MaxOrganismo = 0
    contadorMuestra = 0
    contadorCeldaV = 0

    # abre ventana para seleccionar archivo
    urlarchivo = filedialog.askopenfilename(
        initialdir="./", title="Seleccione un Archivo", filetypes=(("xml", "*.xml"), ("all files", "*.*")))
    # urlarchivo = input()

    documento = minidom.parse(urlarchivo)

    # Se obtienen los datos de la lista organismos
    organismosdoc = documento.getElementsByTagName("organismo")
    for organismodoc in organismosdoc:
        contadorCantidad_MaxOrganismo += 1
        organismo_codigo = organismodoc.getElementsByTagName("codigo")[0]
        organismo_nombre = organismodoc.getElementsByTagName("nombre")[0]
        # print(organismo_codigo.firstChild.data)
        # print(organismo_nombre.firstChild.data)
        if contadorCantidad_MaxOrganismo <= 1000:
            # enviando los parametros al objeto y enviando el objeto a la lista
            objetoOrganismo = Organismo(
                str(organismo_codigo.firstChild.data), str(organismo_nombre.firstChild.data))
            # Agregando organismo a la lista de organismos
            lista_Organismos.addFinalNode(objetoOrganismo)
        else:
            showerror(
                title="Error", message="El tamaño maximo de organismos es: 1000 \nPorfavor ingrese menos organismos")
            break

    # Se obtienen los datos de listado muestras
    muestrasdoc1 = documento.getElementsByTagName("muestra")
    for muestradoc in muestrasdoc1:
        muestra_codigo = muestradoc.getElementsByTagName("codigo")[0]
        muestra_descripcion = muestradoc.getElementsByTagName("descripcion")[0]
        muestra_filas = muestradoc.getElementsByTagName("filas")[0]
        muestra_columnas = muestradoc.getElementsByTagName("columnas")[0]
        # recorriendo la listaa de celdas vivas
        celdasvivasdoc = muestradoc.getElementsByTagName("celdaViva")
        lista_CeldasVivas = Lista()
        for celdavivadoc in celdasvivasdoc:
            celdaViva_fila = celdavivadoc.getElementsByTagName("fila")[0]
            celdaViva_columna = celdavivadoc.getElementsByTagName("columna")[0]
            celdaViva_codigoOrganismo = celdavivadoc.getElementsByTagName("codigoOrganismo")[
                0]
            # .......enviando los parametros al objeto y enviando el objeto a la lista
            objetoCeldaViva = CeldaViva(str(celdaViva_fila.firstChild.data), str(
                celdaViva_columna.firstChild.data), str(celdaViva_codigoOrganismo.firstChild.data))
            # Agregando celda viva a la lista de celdas vivas
            if ((int(celdaViva_fila.firstChild.data) <= int(muestra_filas.firstChild.data)) and (int(celdaViva_columna.firstChild.data) <= int(muestra_columnas.firstChild.data))):
                lista_CeldasVivas.addFinalNode(objetoCeldaViva)
                contadorCeldaV = contadorCeldaV + 1
            else:
                showerror(title="Error", message="La celda Viva debe estar dentro del valor máximo de:\nfilas: 10000\ncolumnas: 10000 \n El codigo del organismo de la celda viva con el dato de la fila o columna que supera el máximo es:\n" + str(celdaViva_codigoOrganismo.firstChild.data))
                break

        if ((int(muestra_filas.firstChild.data) <= 10000) and (int(muestra_columnas.firstChild.data) <= 10000)):
            # enviando los parametros al objeto y enviando el objeto a la lista
            objetoMuestra = Muestra(str(muestra_codigo.firstChild.data), str(muestra_descripcion.firstChild.data), str(
                muestra_filas.firstChild.data), str(muestra_columnas.firstChild.data), lista_CeldasVivas)
            # Agregando muestra a la lista de muestras
            lista_Muestras.addFinalNode(objetoMuestra)
            contadorMuestra += 1
        else:
            showerror(title="Error", message="La muestra solo puede tener como máximo:\nfilas: 10000\ncolumnas: 10000\nEl codigo de la muestra con el dato de la fila o columna que supera el máximo es:\n" + str(muestra_codigo.firstChild.data))
            break

    showinfo(title="Guardado", message="Archivo leído exitosamente")
    # imprimiendo datos
    # lista_Organismos.printList()
    # crear otro metodo imprimir para la lista de muestras
    # lista_Muestras.printList()


def prosperidad():
    pass


def colocarOrganismo():
    pass


def actualizarMuestra():
    pass


def crearMuestra():
    pass


def menuListaMuestras():
    while True:
        try:
            print("\n------- Menu Lista de Muestras --------\n")
            # mostrar el listado de las muestras y elegir una opcion
            lista_Muestras.printListMuestra()

            # recibe la opcion ingresada y la guarda como entero

            opcion2 = int(input(
                "\nPara ver la lista de celdas vivas.\nIngrese el número que corresponde a la muestra: "))
            print()
            print("\n------- Lista de Celdas Vivas --------\n")
            lista_Muestras.recorrListMuestra(opcion2)
            obteniendodatos(opcion2)

            graficar1()
            print("\n1. Ver prosperidad de cada organismo"+"\n2. Colocar organismo" + "\n3. Actualizar Muestra"+"\n4. Crear Muestra"+"\n5. Regresar")
            opcionMenu = int(input("Ingrese una opción: "))
            print()
            if opcionMenu == 1:
                prosperidad()
            elif opcionMenu == 2:
                colocarOrganismo()
            elif opcionMenu == 3:
                actualizarMuestra()
            elif opcionMenu == 4:
                crearMuestra()
            elif opcionMenu == 5:
                break
            else:
                print("Ingrese una opcion correcta")
        except ValueError:
            print("\nPor favor ingrese solo numeros")

def obteniendodatos(opcion22):
    f = lista_Muestras.getDatoC(opcion22)
    global filass
    filass = f.getFilasMuestra()
    global columnass
    columnass = f.getColumnasMuestra()
    global codigoMS
    codigoMS = f.getCodigoMuestra()
    global descripcionMS
    descripcionMS = f.getDescripcionMuestra()
    global lcv
    lcv = f.listado_CVivas
    lcv.getListaCViva()


def graficar():
    fila = int(filass)
    columna = int(columnass)
    # INICIA CON LA CREACIÓN DEL ARCHIVO Y LE AGREGA EL CONTENIDO CON LA VARIABLE
    grafico = open("matriz.dot", "w")
    cadena = '''digraph matriz{\n 
    size=8.5; 
    ranksep=2; 
    
    margin = 0.1;
    node[ shape = record]; 
    matriz [label = "{X\\\Y'''
    # CONTADOR PARA ENUMERAR LAS FILAS EN LA MATRIZ
    aum = 1
    # Agrega el espacio en blanco de las filas y columnas
    aux = ''
    while aum <= fila:
        cadena = cadena + "|" + str(aum)
        aux = aux + '|'
        aum += 1
    cadena = cadena + '}"'
    # CONTADOR PARA ENUMERAR LAS COLUMNAS EN LA MATRIZ
    aum1 = 1
    # VARIABLE PARA AGREGAR LAS COLUMNAS Y SUS RESPECTIVOS ESPACIOS DE ACUERDO CON LAS FILAS
    cadena1 = ""
    while aum1 <= columna:
        cadena1 = cadena1 + '+"|{'+str(aum1) + aux + '}"'
        aum1 += 1
    cadena = cadena + cadena1
    cadena = cadena + "];\n"
    # en está parte debe ir la información del nodo de organismos
    cadena = cadena + 'subgraph d{ m[style = "filled", shape = box3d, fillcolor= yellow,label = '
    cadena = cadena + '"MUESTRA\ncodigo:'+ str(codigoMS) +'\n' + str(descripcionMS) +'"];}'

    cadena = cadena + 'subgraph d1{m1[style ="filled", shape = note, fillcolor = orange, label = "\nA- NOMBRE \nB - Nombre  \nx-lugares prosperos para el cultivo"]; }'
    # Finaliza el cierre de llaves del digraph
    cadena = cadena + "}"
    grafico.write(cadena)
    grafico.close()

 
def graficar1():
    fila = int(filass)
    columna = int(columnass)
    grafo = graphviz.Digraph('matriz',filename ='matriz.dot')
    grafo.attr(rankdir = 'LR',size='8,5', ranksep="0.2", margin = "0.05")
    grafo.attr('node', shape= 'plaintext')
    cadena = '''<
        <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" ALIGN="CENTER"> 
            <TR>
                <TD BGCOLOR="YELLOW" width= "35" height = "35"><b>x\y</b></TD>
            '''
    aum1 = 1
    # VARIABLE PARA AGREGAR LAS COLUMNAS Y SUS RESPECTIVOS ESPACIOS DE ACUERDO CON LAS FILAS
    cadenaColumas = ""
    while aum1 <= columna:
        cadenaColumas = cadenaColumas + '<TD width= "35" height = "35">'+str(aum1)+"</TD>"
        aum1 += 1
    cadena = cadena + cadenaColumas +"</TR>" 

    aum = 1
    cadenaFilas = ""
    while aum <= fila:  
        cadenaFilas =  cadenaFilas + '''<TR>
                <TD width= "35" height = "35">'''+str(aum)+'''</TD>'''
        aum2 = 1
        cadenaColumas1 = ""
        # validar la entrada de la fila  de la celda viva
        while aum2 <= columna:
            #validar la entrada de la columna de la celda viva
            cadenaColumas1 = cadenaColumas1 + '<TD width= "35" height = "35"> </TD>'
            aum2 += 1
        cadenaFilas = cadenaFilas + cadenaColumas1 +"</TR>" 
        aum += 1
    cadena = cadena + cadenaFilas
    cadena = cadena + '</TABLE>>'
    datoM = 'MUESTRA\ncodigo:'+ str(codigoMS) +'\n' + str(descripcionMS)
    grafo.node("tabla", cadena)

    grafo.attr('node',style='', color='')
    grafo.attr('node', shape= 'rectangle', style="filled", color="black",fillcolor="lightsalmon")
    grafo.node('muestra',datoM)
    grafo.edge('tabla'+':e', 'muestra', arrowhead = 'none')

    datoMCV = 'Organismos \n asdf'

    grafo.attr('node',style='', color='')
    grafo.attr('node', shape= 'rectangle', style="filled", color="black",fillcolor="lightsalmon")
    grafo.node('cv',datoMCV)
    grafo.edge('tabla'+':e', 'cv', arrowhead = 'none')
    #grafo.save(filename= "tabla.dot", directory="./Practica1") #,directory="Practica1\tabla.dot"
    #os.system("dot.exe -Tpdf Practica1/tabla.dot -o Practica1/peliculas.pdf")
    grafo.view(filename ="matriz.dot")

def guardarArchivo():
    pass

def inicializacion():
    pass

if __name__ == '__main__':
    while True:
        try:
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
seleccionar muestra -> colocar algun organismo de la muestra -> validar la forma en que cambia la muestra e indicar cuando la muestra ya no puede ser modificada
actualizar-> informacion de la muestra 
crear -> muestra con los cambios introducidos
guardar archivo ->con las muestras actualizadas con la misma estructura del archivo de entrada
Inicializacion -> cargar un archivo desde 0, si se carga y existen datos cargados anteriormente deben continuar existiendo y debe aumentar la informacion en el sistema


Pasos de graficos
1. CUANDO SE SELECCIONE LA MUESTRA GENERAR IMAGEN DE TABLA DEL TAMAÑO DE FILA Y COLUMNA CORRESPONDIENTE > Ya está funcionando
2. Obtener codigo de muestra y descripcion de la muestra y mostrarlos al lado en un nodo -> Ya está funcionando
3. Obtener fila, columna y codigo de organismo de la lista de celdas vivas
4. Comparar el codigo de organismo con el codigo de organismo almacenado en la lista de organismos, para obtener el nombre del organismo
4. AGREGAR A LA TABLA LOS DATOS DE LAS CELDAS VIVAS DEL ORGANISMO QUE SELECIONÓ
"""
