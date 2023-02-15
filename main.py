from tkinter import CENTER, RIGHT, Y, Scrollbar, filedialog, Tk, ttk
import sys
import tkinter
from tkinter.messagebox import showerror, showinfo, showwarning
import tkinter as tk
from xml.dom import minidom
from organismo import Organismo
from muestra import Muestra
from celdaViva import CeldaViva
from lista import Lista
from pickle import FALSE, TRUE


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
            print("El tamaño maximo de organismos es: 1000 \nPorfavor ingrese menos organismos")
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
    
    showinfo(title="Guardado", message="Archivo leído exitosamente")
    #imprimiendo datos
    #lista_Organismos.printList()
    #crear otro metodo imprimir para la lista de muestras
    #lista_Muestras.printList()

def seleccionarMuestra():
    pass
def actualizarMuestra():
    pass
def crearMuestra():
    pass
def guardarArchivo():
    pass
def inicializacion():
    pass

def salir():
    # menu.destroy()
    sys.exit()

if __name__ == '__main__':
    menu = tkinter.Tk()
    menu.title("ORGANISMOS")
    menu.geometry("700x450")
    menu.configure(bg="black")
    menu.resizable(False, False)
    tk.Label(menu, text="Nombre del curso:", bg="black", fg="lightgreen", font=("Arial Black", 13)).place(x=20, y=15)
    tk.Label(menu, text="Laboratorio Introducción a la Programación y Computación 2 D", bg="black", fg="orange", font=("Calibri", 13)).place(x=250, y=15)
    tk.Label(menu, text="Nombre del Estudiante:", bg="black", fg="lightgreen", font=("Arial Black", 13)).place(x=20, y=45)
    tk.Label(menu, text="Josué Daniel Rojché García", bg="black", fg="orange", font=("Calibri", 13)).place(x=250, y=45)
    tk.Label(menu, text="Carné del Estudiante:", bg="black", fg="lightgreen", font=("Arial Black", 13)).place(x=20, y=75)
    tk.Label(menu, text="201901103", bg="black", fg="orange", font=("Calibri", 13)).place(x=250, y=75)
    '''
    crea los botones, se envia como parametro el objeto de la ventana a la que agregará, también se le envia configuraciones y 
    posición en la cual estarán ubicados dentro de la ventana, así como los metodos que harán las acciones al hacer click sobre el boton
    '''
    tk.Button(menu, text="Cargar archivo xml", width=20, anchor="c", bg="orange", fg="Black", font=("Arial Black", 10), command=lambda: cargarArchivo()).place(x=190, y=130)
    tk.Button(menu, text="Seleccionar muestra", width=20, anchor="c", bg="orange", fg="Black", font=("Arial Black", 10), command=lambda: seleccionarMuestra()).place(x=190, y=175)
    tk.Button(menu, text="Actualizar muestra", width=20, anchor="c", bg="orange", fg="Black", font=("Arial Black", 10), command=lambda: actualizarMuestra()).place(x=190, y=220)
    tk.Button(menu, text="Crear muestra", width=20, anchor="c", bg="orange", fg="Black", font=("Arial Black", 10), command=lambda: actualizarMuestra()).place(x=190, y=265)
    tk.Button(menu, text="Guardar archivo", width=20, anchor="c", bg="orange", fg="Black", font=("Arial Black", 10), command=lambda: actualizarMuestra()).place(x=190, y=310)
    tk.Button(menu, text="Inicialización", width=20, anchor="c", bg="orange", fg="Black", font=("Arial Black", 10), command=lambda: actualizarMuestra()).place(x=190, y=355)
    tk.Button(menu, text="Salir", width=20, anchor="c", bg="orange", fg="Black", font=("Arial Black", 10), command=lambda: salir()).place(x=190, y=400)

    menu.mainloop() # Permite mostrar la ventana 
"""
cargar archivo -> Ya está hecha
seleccionar muestra -> colocar algun organismo de la muestra -> validar la forma en que cambia la muestra e indicar cuando la muestra ya no puede ser modificada
actualizar-> informacion de la muestra 
crear -> muestra con los cambios introducidos
guardar archivo ->con las muestras actualizadas con la misma estructura del archivo de entrada
Inicializacion -> cargar un archivo desde 0, si se carga y existen datos cargados anteriormente deben continuar existiendo y debe aumentar la informacion en el sistema
"""