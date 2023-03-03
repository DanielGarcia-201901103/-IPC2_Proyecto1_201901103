from nodo import Nodo
class Lista:
    def __init__(self):
        self.first = None
        self.final = None
        self.size = 0
    #Agrega el objeto al final de la lista
    def addFinalNode(self, dato):
        newNodo = Nodo(dato) # se crea un nuevo nodo
        #si la lista está vacia
        self.size += 1
        if self.first == None: #si la lista no tiene ningun dato
            self.first = newNodo #el apuntador primero apunta al nuevo nodo
            self.final = newNodo #el apuntador ultimo apunta al nuevo nodo
        else: #si la lista ya tiene uno o mas datos se agrega el nuevo nodo
            self.final.after = newNodo #el apuntador siguiente apunta al nuevo nodo --->
            newNodo.before = self.final #el apuntador anterior apunta al nodo anterior  <---
            self.final = newNodo #el apuntador ultimo apunta al nuevo nodo
    
    #Imprime la lista de muestras , no imprime las celdas vivas
    def printListMuestra(self):
        print("No. | Filas | Columnas | Codigo | Descripción"  )
        count = 0
        nodoTemporal = Nodo("")
        nodoTemporal = self.first
        while nodoTemporal != None:
            count +=1
            print(str(count) + "  | "+str(nodoTemporal.dato.getFilasMuestra()) + "  | "+ str(nodoTemporal.dato.getColumnasMuestra())+ "  | "+ str(nodoTemporal.dato.getCodigoMuestra())+ "  | "+ str(nodoTemporal.dato.getDescripcionMuestra()))
            nodoTemporal = nodoTemporal.after #pasa al siguiente nodo de la lista

    #Imprime la lista de celdas vivas ya ordenadas        
    def recorrListMuestra(self, rec):
        print("No. | Fila | Columna | Codigo Organismo"  )
        count = 0
        nodoTemporal = Nodo("")
        nodoTemporal = self.first
        while nodoTemporal != None:
            count +=1
            if count == rec:
                listaTemporal = nodoTemporal.dato.listado_CVivas
                listaTemporal.BubbleSort()
                listaTemporal.BubbleSortC()
                listaTemporal.recorrListaCViva()

            nodoTemporal = nodoTemporal.after #pasa al siguiente nodo de la lista
    def recorrListaCViva(self):
        count1 = 0
        nodoTemporal1 = Nodo("")
        nodoTemporal1 = self.first
        while nodoTemporal1 != None:
            count1 +=1
            print(str(count1)+ "   | "+str(nodoTemporal1.dato.getFilaCeldaViva())+ "   | "+str(nodoTemporal1.dato.getColumnaCeldaViva())+ "      | "+str(nodoTemporal1.dato.getCodigoCeldaOrganismoVivo()))
            nodoTemporal1 = nodoTemporal1.after

    #OBTENER DATOS DE MUESTRAS, cualquier dato
    def getDatoC(self, rec):
        count = 0
        nodoTemporal = Nodo("")
        nodoTemporal = self.first
        while nodoTemporal != None:
            count +=1
            if count == rec:
                return nodoTemporal.dato
            nodoTemporal = nodoTemporal.after #pasa al siguiente nodo de la lista
    #OBTENER DATOS de las celdas vivas, cualquier valor
    def getDatoCV(self, rec, rec2): 
        nodoTemporal = Nodo("")
        nodoTemporal = self.first
        while nodoTemporal != None:
            if (int(nodoTemporal.dato.getFilaCeldaViva()) == rec) and (int(nodoTemporal.dato.getColumnaCeldaViva()) == rec2 ):
                return nodoTemporal.dato
            nodoTemporal = nodoTemporal.after #pasa al siguiente nodo de la lista
        #OBTENER DATOS DE Organismos
    def getDatoOrga(self, rec):
        nodoTemporal = Nodo("")
        nodoTemporal = self.first
        while nodoTemporal != None:
            if nodoTemporal.dato.getCodigoOrganismo() == rec:
                return nodoTemporal.dato.getNommbreOrganismo()
            nodoTemporal = nodoTemporal.after #pasa al siguiente nodo de la lista
    
    #OBTENER DATOS DE LISTA DE ORGANISMOS
    def getDatoNO(self):
        almacenar = ""
        nodoTemporal = Nodo("")
        nodoTemporal = self.first
        while nodoTemporal != None:
            almacenar = almacenar + nodoTemporal.dato.getNommbreOrganismo()  + '\n'
            nodoTemporal = nodoTemporal.after #pasa al siguiente nodo de la lista
        return almacenar

    #Obtener colores para cada uno de los datos
    def getColorO(self, reC):
        nodoTemporal = Nodo("")
        nodoTemporal = self.first
        while nodoTemporal != None:
            if nodoTemporal.dato.getCoColorOrganismo() == reC:
                return nodoTemporal.dato.getNommbreColor()
            nodoTemporal = nodoTemporal.after #pasa al siguiente nodo de la lista
    
    #ordenamiento funcionando
    def BubbleSort(self):
        if self.size > 1:
            while True:
                actual = self.first
                i = None  # anterior
                j = self.first.after  # siguiente
                cambio = False
                while j != None:
                    if int(actual.dato.getFilaCeldaViva())> int(j.dato.getFilaCeldaViva()):
                        cambio = True
                        if i != None:
                            tmp = j.after
                            i.after = j
                            j.after = actual
                            actual.after = tmp
                        else:
                            tmp2 = j.after
                            self.first = j
                            j.after = actual
                            actual.after = tmp2
                        i = j
                        j = actual.after
                    else:
                        i = actual
                        actual = j
                        j = j.after
                if not cambio:
                    break
    #ordenamiento para las columnas pero manteniendo las filas intactas
    def BubbleSortC(self):
        if self.size > 1:
            while True:
                actual = self.first
                i = None  # anterior
                j = self.first.after  # siguiente
                cambio = False
                while j != None:
                    if (int(actual.dato.getColumnaCeldaViva())> int(j.dato.getColumnaCeldaViva())) and (int(actual.dato.getFilaCeldaViva())== int(j.dato.getFilaCeldaViva())):
                        cambio = True
                        if i != None:
                            tmp = j.after
                            i.after = j
                            j.after = actual
                            actual.after = tmp
                        else:
                            tmp2 = j.after
                            self.first = j
                            j.after = actual
                            actual.after = tmp2
                        i = j
                        j = actual.after
                    else:
                        i = actual
                        actual = j
                        j = j.after
                if not cambio:
                    break