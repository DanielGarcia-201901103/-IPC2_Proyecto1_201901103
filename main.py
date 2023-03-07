import os
import random
from tkinter import filedialog
import sys
from tkinter.messagebox import showerror, showinfo, showwarning
from xml.dom import minidom
import xml.etree.cElementTree as ET
from Lista import Lista
from organismo import Organismo
from muestra import Muestra
from celdaViva import CeldaViva
from color import Color
import graphviz

# variables globales
lista_Colores = Lista()
lista_Organismos = Lista()
lista_Muestras = Lista()

filass = 0
columnass = 0
codigoMS = ""
descripcionMS = ""
lcv = Lista()
coordenadas = Lista()  # almacena las coordenadas donde prosperan los datos
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
    if urlarchivo != "":
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
                objetoOrganismo = Organismo(str(organismo_codigo.firstChild.data).strip(), str(organismo_nombre.firstChild.data).strip())
                colorS = "#"+''.join(random.choice('0123456789ABCDEF')for j in range(6))
                objetoColor = Color(str(organismo_codigo.firstChild.data).strip(), str(colorS).strip(), str(organismo_nombre.firstChild.data).strip())
                # Agregando organismo a la lista de organismos y agregando color al organismo
                lista_Organismos.addFinalNode(objetoOrganismo)
                lista_Colores.addFinalNode(objetoColor)
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
                objetoCeldaViva = CeldaViva(str(celdaViva_fila.firstChild.data).strip(), str(celdaViva_columna.firstChild.data).strip(), str(celdaViva_codigoOrganismo.firstChild.data).strip())
                # Agregando celda viva a la lista de celdas vivas
                if ((int(celdaViva_fila.firstChild.data) <= int(muestra_filas.firstChild.data)) and (int(celdaViva_fila.firstChild.data) > 0) and (int(celdaViva_columna.firstChild.data) <= int(muestra_columnas.firstChild.data)) and (int(celdaViva_columna.firstChild.data) > 0 )):
                    lista_CeldasVivas.addFinalNode(objetoCeldaViva)
                    contadorCeldaV = contadorCeldaV + 1
                else:
                    showerror(title="Error", message="La celda Viva debe estar dentro del valor máximo de:\nfilas: 10000\ncolumnas: 10000 \n El codigo del organismo de la celda viva con el dato de la fila o columna que supera el máximo es:\n" + str(celdaViva_codigoOrganismo.firstChild.data))
                    break

            if ((int(muestra_filas.firstChild.data) <= 10000) and (int(muestra_columnas.firstChild.data) <= 10000)):
                # enviando los parametros al objeto y enviando el objeto a la lista
                objetoMuestra = Muestra(str(muestra_codigo.firstChild.data).strip(), str(muestra_descripcion.firstChild.data).strip(), str(
                    muestra_filas.firstChild.data).strip(), str(muestra_columnas.firstChild.data).strip(), lista_CeldasVivas)
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
    else :
        print("canceló la opción\n")


def prosperidad(opcionMuestra):
    print("\nLos organismos prosperan en las siguientes coordenadas\n")
    # Validar para cuando sea horizontal
    lcv.validandoHorizontal(int(filass), int(columnass), lcv)
    """
comenzar con las validaciones para que los organismos vivos prosperen
practicamente obtener la fila y la columna en la que se encuentra el organismo y hacer lo siguiente
validar horizontalmente
ejemplo si tenemos la fila 8 y  columna 10
mantener la fila y validar si en cualquier otra columna hay otro organismo del mismo tipo obtener la columna de ese organismo 
y tambien validar que si hay algun otro organismo dentro de este rango entonces la muestra vuelve a cambiar y ahora todos los organismos dentro de este rango se convierten en el otro organismo, solo se envia el codigo y nombre con los setter a sustituir los datos de ese organismo
    """
    # recorrido para validar cuando sea vertical


    # recorrido para validar cuando sea en diagonal
"""
comenzar con las validaciones para que los organismos vivos prosperen
practicamente obtener la fila y la columna en la que se encuentra el organismo y hacer lo siguiente

validar verticalmente
ejemplo si tenemos la fila 8 y  columna 10
mantener la columna y validar si en cualquier otra fila hay otro organismo del mismo tipo obtener la fila de ese organismo 
y tambien validar que si hay algun otro organismo dentro de este rango entonces la muestra vuelve a cambiar y ahora todos los organismos dentro de este rango se convierten en el otro organismo, solo se envia el codigo y nombre con los setter a sustituir los datos de ese organismo
validar en diagonal 
si fila -1 y columna +1 y fila debe ser mayor o igual a 1 columna deben ser menor o igual a tamaño de columnas de la muestra y tienen un organismo del mismo tipo validar que exista otro organismo de otro tipo para poder alimentarse
si fila -1 y columna -1 y fila columna deben ser mayor o igual a 1 tienen un organismo del mismo tipo validar que exista otro organismo de otro tipo para poder alimentarse
si fila +1 y columna -1 y fila debe ser menor o igual a tamaño de filas de la muestra y columna debe ser mayor o igual a 1
si fila +1 y columna +1 y fila columna deben ser menor o igual a tamaño de MxN de la muestra
si en cualquier otra fila o columna hay otro organismo del mismo tipo obtener la fila y columna de ese organismo 

si un organismo no se puede alimentar entonces morirá
"""


def colocarOrganismo():
    print("\n-------Ingresar Organismo --------\n")
    # mostrar el listado de las muestras y elegir una opcion
    lista_Muestras.printListMuestra()
    # recibe la opcion ingresada y la guarda como entero
    opcion3 = int(input("\nIngrese el número de la muestra donde agregara el organismo: "))
    print()
    # obtiene los datos de la lista de muestras
    ac = lista_Muestras.getDatoC(opcion3)
    try:
        print("\n------- Lista de Celdas Vivas --------\n")
        # si desea agregar a la lista de celdas vivas entonces mostrar la lista de celdas vivas
        ac.listado_CVivas.recorrListaCViva1()
        # seleccione el dato a editar
        print("\nPor favor ingrese una celda donde no exista un organismo (ver tabla)\n ingrese solamente codigo existente en la muestra")
        
        #         obtener el dato a editar
        cv = ac.listado_CVivas
        #poderEditar = cv.getDatoC(opcionListaCV)
        #         buscar el dato a editar y enviar los nuevos datos
        opcionPFila = int(input("\nIngrese la posición de la fila: "))
        opcionPColumna = int(input("\nIngrese la posición de la columna: "))
        opcionCodigoCV = input("\nIngrese el nuevo codigo: ")
        validacionBooleana = cv.ingresandoLCeldasVivas(opcionPFila, opcionPColumna)
        validacionBooleana1 = cv.validandoCodigoIgual(opcionCodigoCV.strip())
        if (validacionBooleana == False) and (validacionBooleana1 == True):
            if (opcionPFila <= int(ac.getFilasMuestra())) and (opcionPColumna <= int(ac.getColumnasMuestra())):
                #crear objeto y agregarlo a la lista de celdas vivas
                objetoCeldaViva = CeldaViva(str(opcionPFila).strip(), str(opcionPColumna).strip(), str(opcionCodigoCV).strip() )
                ac.listado_CVivas.addFinalNode(objetoCeldaViva)
                print("\nDatos ingresados correctamente\n")
            else:
                print("\nFila o Columna supera el valor del tamaño de la matriz, por favor ingrese los datos con una cantidad menor.\n O elcodigo no se encuentra entre los datos")
        elif validacionBooleana == True:
            print("\nPor favor no ingrese posiciones en las cuales ya existe otro organismo, y ingrese un codigo que exista en la muestra")
    except ValueError:
        print("\nPor favor ingrese solo numeros en fila y columna")

def actualizarMuestra():

    print("\n-------Actualizar Muestra --------\n")
    # mostrar el listado de las muestras y elegir una opcion
    lista_Muestras.printListMuestra()
    # recibe la opcion ingresada y la guarda como entero
    opcion3 = int(input("\nIngrese el número de la muestra a Actualizar: "))
    print()
    # obtiene los datos de la lista de muestras
    ac = lista_Muestras.getDatoC(opcion3)

    while True:
        try:
            # preguntar al usuario que datos desea actualizar
            print("\n1. Tamaño de la muestra"+"\n2. Codigo de Muestra" +"\n3. Descripción de Muestra" + "\n4. Lista de celdas vivas"+"\n5. Regresar\n")
            opcionActualizar = int(input("Ingrese una opción: "))
            print()
            if opcionActualizar == 1:
                #   si desea actualizar el tamaño de la muestra (matriz)
                opcionFila = int(input("\nIngrese el tamaño de filas: "))
                ac.setFilasMuestra(str(opcionFila))
                opcionColumna = int(input("\nIngrese el tamaño de columnas: "))
                if (opcionFila <= 10000) and (opcionColumna <= 10000):
                    ac.setFilasMuestra(str(opcionFila).strip())
                    ac.setColumnasMuestra(str(opcionColumna).strip())
                    print("Fila y Columna editado correctamente")
                else:
                    print(
                        "\nFila o Columna supera el valor maximo de 10000, por favor ingrese los datos con una cantidad menor.")
            elif opcionActualizar == 2:
                # codigo de la Muestra
                opcionCodigo = (input("\nIngrese el nuevo codigo: "))
                ac.setCodigoMuestra(opcionCodigo.strip())
            elif opcionActualizar == 3:
                # Descripcion de la muestra
                opcionDescripcion = (input("\nIngrese la nueva descripcion: "))
                ac.setDescripcionMuestra(opcionDescripcion.strip())
            elif opcionActualizar == 4:
                print("\n------- Lista de Celdas Vivas --------\n")
                # si desea editar la lista de celdas vivas entonces mostrar la lista de celdas vivas
                lista_Muestras.recorrListMuestra(opcion3)
                # seleccione el dato a editar
                opcionListaCV = int(
                    input("\nIngrese el número de la celda viva a Actualizar: "))
                #         obtener el dato a editar
                cv = ac.listado_CVivas
                poderEditar = cv.getDatoC(opcionListaCV)
                #         buscar el dato a editar y enviar los nuevos datos
                opcionPFila = int(input("\nIngrese la posición de la fila: "))
                opcionPColumna = int(
                    input("\nIngrese la posición de la columna: "))
                validacionBooleana = cv.actualizandoLCeldasVivas(
                    opcionPFila, opcionPColumna)
                if validacionBooleana == False:
                    if ((opcionPFila <= int(ac.getFilasMuestra())) and (opcionPColumna <= int(ac.getColumnasMuestra()))) and ((opcionPFila > 0) and (opcionPColumna > 0)):
                        poderEditar.setFilaCeldaViva(str(opcionPFila).strip())
                        poderEditar.setColumnaCeldaViva(str(opcionPColumna).strip())
                        print("\nFila y Columna editado correctamente\n")
                    else:
                        print(
                            "\nFila o Columna supera el valor del tamaño de la matriz, por favor ingrese los datos con una cantidad menor.")
                elif validacionBooleana == True:
                    print(
                        "\nPor favor no ingrese posiciones en las cuales ya existe otro organismo")
                validarSN = input(
                    "\nPara editar el codigo, escriba si de lo contrario escriba no:")
                if validarSN.lower() == "si":
                    opcionCodigoCV = input("\nIngrese el nuevo codigo: ")
                    validacionBooleana1 = lista_Organismos.actualizandoCodigoCV(
                        opcionCodigoCV)
                    if validacionBooleana1 == True:
                        poderEditar.setCodigoCeldaOrganismoVivo(opcionCodigoCV.strip())
                    elif validacionBooleana1 == False:
                        print(
                            "\nPor favor no ingrese codigo que no exista en la lista de organismos")
                elif validarSN.lower() == "no":
                    print("\nCodigo no editado")
                else:
                    pass
            elif opcionActualizar == 5:
                break
            else:
                print("\nIngrese una opcion correcta")
        except ValueError:
            print("\nPor favor ingrese solo numeros")


def menuListaMuestras():
    while True:
        try:
            print("\n------- Menu Lista de Muestras --------\n")
            # mostrar el listado de las muestras y elegir una opcion
            lista_Muestras.printListMuestra()
            # recibe la opcion ingresada y la guarda como entero
            opcion2 = int(input("\nPara ver la lista de celdas vivas.\nIngrese el número que corresponde a la muestra: "))
            print()
            print("\n------- Lista de Celdas Vivas --------\n")
            lista_Muestras.recorrListMuestra(opcion2)
            obteniendodatos(opcion2)

            print("\n1. Graficar"+"\n2. Ver prosperidad"+"\n3. Colocar organismo" +"\n4. Actualizar Muestra"+"\n5. Regresar\n")
            opcionMenu = int(input("Ingrese una opción: "))
            print()
            if opcionMenu == 1:
                graficar1()
            elif opcionMenu == 2:
                prosperidad(opcion2)
            elif opcionMenu == 3:
                colocarOrganismo()
            elif opcionMenu == 4:
                actualizarMuestra()
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
    # lcv.getListaCViva()


def graficar1():
    lcv.BubbleSort()
    lcv.BubbleSortC()
    fila = int(filass)
    columna = int(columnass)
    grafo = graphviz.Digraph('matriz', filename='matriz.dot')
    grafo.attr(rankdir='LR', size='8,5', ranksep="0.2", margin="0.05")
    grafo.attr('node', shape='plaintext')
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
    cadena = cadena + cadenaColumas + "</TR>"
    aum = 1
    cadenaFilas = ""
    while aum <= fila:
        cadenaFilas = cadenaFilas + '''<TR>
        <TD width= "35" height = "35">'''+str(aum)+'''</TD>'''
        aum2 = 1
        cadenaColumas1 = ""
        # validar la entrada de la fila  de la celda viva
        while aum2 <= columna:
            v = lcv.getDatoCV(aum, aum2)
            if v != None:
                if int(v.getColumnaCeldaViva()) == aum2:
                    # validar que cada vez que sea un diferente codigo entonces obtenga un color diferente
                    # hacer la validacion que cada vez que tenga el codigo del organismo recorra la lista de colores para obtener el color
                    colordif = lista_Colores.getColorO(str(v.getCodigoCeldaOrganismoVivo()))
                    cadenaColumas1 = cadenaColumas1 + '<TD width= "35" height = "35" BGCOLOR= "' + str(colordif)+'"></TD>'
                else:
                    cadenaColumas1 = cadenaColumas1 + '<TD width= "35" height = "35"> </TD>'
            elif v == None:
                cadenaColumas1 = cadenaColumas1 + '<TD width= "35" height = "35"> </TD>'
            # si la fila es igual a la fila en la lista de la celda viva entonces ingresar al if donde se evalua si la columna es igual a la columna donde se encuentra el dato
            # validar la entrada de la columna de la celda viva
            aum2 += 1

        cadenaFilas = cadenaFilas + cadenaColumas1 + "</TR>"
        aum += 1
    cadena = cadena + cadenaFilas
    cadena = cadena + '</TABLE>>'
    datoM = 'MUESTRA\ncodigo:' + str(codigoMS) + '\n' + str(descripcionMS)
    grafo.node("tabla", cadena)

    grafo.attr('node', style='', color='')
    grafo.attr('node', shape='rectangle', style="filled", color="black", fillcolor="lightsalmon")
    grafo.node('muestra', datoM)
    grafo.edge('tabla'+':e', 'muestra', arrowhead='none')

    # Tabla para mostrar los colores de cada uno de los datos
    cadenaA = '''<
        <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" ALIGN="CENTER"> 
            <TR>
                <TD COLSPAN="2" BGCOLOR="YELLOW" width= "35" height = "35"><b>Organismos</b></TD>
            </TR>
            '''
    codiO = lista_Colores.getDatoNOCO()
    datoMCV = cadenaA + codiO
    datoMCV = datoMCV + '</TABLE>>'
    grafo.attr('node', style='', color='')
    grafo.attr('node', shape='plaintext')
    grafo.node('cv', datoMCV)
    grafo.edge('tabla'+':e', 'cv', arrowhead='none')
    # grafo.save(filename= "tabla.dot", directory="./Practica1") #,directory="Practica1\tabla.dot"
    os.system("dot.exe -Tpng matriz.dot -o matriz.png")
    grafo.view(filename="matriz.dot")


def guardarArchivo():
    guardar = filedialog.asksaveasfilename(
        initialdir="./", title="Guardar Como", filetypes=(("Archivos xml", "*.xml"), ("all files", "*.*")))
    ruta = str(guardar)
    if guardar != "":
        # dato raíz
        root = ET.Element('datosMarte')
        # dato hijo
        lOrganismos = ET.SubElement(root, 'listaOrganismos')
        # crear un recorrido que obtenga cada dato del la lista de organismos
        boleanoOrganismo = True
        contadorOr = 1
        while boleanoOrganismo:
            x = lista_Organismos.agregarEscrituraOrganismo(
                contadorOr, boleanoOrganismo)
            if x == False:
                boleanoOrganismo = False
                break
            else:
                # agrega un dato hijo al hijo
                datoOrganismo = ET.SubElement(lOrganismos, 'organismo')
                ET.SubElement(datoOrganismo, 'codigo').text = str(
                    x.getCodigoOrganismo())
                ET.SubElement(datoOrganismo, 'nombre').text = str(
                    x.getNommbreOrganismo())
            contadorOr += 1

        # dato hijo
        lMuestras = ET.SubElement(root, 'listadoMuestras')

        # desde aqui se debe iterar ya que pueden haber varios hijos muestra
        boleanoOrganismo1 = True
        contadorOr1 = 1
        while boleanoOrganismo1:
            x1 = lista_Muestras.agregarEscrituraOrganismo(
                contadorOr1, boleanoOrganismo1)
            if x1 == False:
                boleanoOrganismo1 = False
                break
            else:
                # agrega un dato hijo al hijo
                lmuestra = ET.SubElement(lMuestras, 'muestra')
                ET.SubElement(lmuestra, 'codigo').text = str(x1.getCodigoMuestra())
                ET.SubElement(lmuestra, 'descripcion').text = str(
                    x1.getDescripcionMuestra())
                ET.SubElement(lmuestra, 'filas').text = str(x1.getFilasMuestra())
                ET.SubElement(lmuestra, 'columnas').text = str(
                    x1.getColumnasMuestra())
                # hacer otro recorrido para este dato
                lCeldaVivas = ET.SubElement(lmuestra, 'listadoCeldasVivas')
                # obteniendo la lista de celdas vivas
                obteniendoLista = x1.listado_CVivas
                boleanoOrganismo2 = True
                contadorOr2 = 1
                while boleanoOrganismo2:

                    x2 = obteniendoLista.agregarEscrituraOrganismo(
                        contadorOr2, boleanoOrganismo2)
                    if x2 == False:
                        boleanoOrganismo2 = False
                        break
                    else:
                        # agrega un dato hijo al hijo
                        datoCeldaViva = ET.SubElement(lCeldaVivas, 'celdaViva')
                        ET.SubElement(datoCeldaViva, 'fila').text = str(
                            x2.getFilaCeldaViva())
                        ET.SubElement(datoCeldaViva, 'columna').text = str(
                            x2.getColumnaCeldaViva())
                        ET.SubElement(datoCeldaViva, 'codigoOrganismo').text = str(
                            x2.getCodigoCeldaOrganismoVivo())
                    contadorOr2 += 1
            contadorOr1 += 1

        # Crea el archivo con los datos del arbol xml
        archivoXml = ET.ElementTree(root)
        archivoXml.write(ruta + '.xml')
        print("\nArchivo guardado exitosamente\n")
    else :
        print("canceló la opción\n")

def inicializacion():
    lista_Colores.vaciarLista()
    lista_Organismos.vaciarLista()
    lista_Muestras.vaciarLista()
    lcv.vaciarLista()


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
                validarVacia = lista_Muestras.ValidarListaVacia()
                if validarVacia == True:
                    menuListaMuestras()
                elif validarVacia == False:
                    print(
                        "Por favor cargue un archivo ya que no hay datos para procesar")
            elif opcion == 3:
                validarVacia1 = lista_Muestras.ValidarListaVacia()
                if validarVacia1 == True:
                    guardarArchivo()
                elif validarVacia1 == False:
                    print(
                        "Por favor cargue un archivo ya que no hay datos para procesar")
            elif opcion == 4:
                validarVacia2 = lista_Muestras.ValidarListaVacia()
                if validarVacia2 == True:
                    inicializacion()
                elif validarVacia2 == False:
                    print(
                        "Por favor cargue un archivo ya que no hay datos para procesar")
            elif opcion == 5:
                sys.exit()
            else:
                print("Ingrese una opcion correcta")
        except ValueError:
            print("\nPor favor ingrese solo numeros")


#CORREGIR ERROR DE ORDENAMIENTO BURBUJA
#SOLAMENTE FALTA LAS VALIDACIONES EN HORIZONTAL, VERTICAL, DIAGONAL Y TERMINAR LA DOCUMENTACION