from nodo import Nodo
class Lista:
    def __init__(self):
        self.first = None
        self.final = None

    def addFinalNode(self, dato):
        newNodo = Nodo(dato) # se crea un nuevo nodo
        #si la lista está vacia
        if self.first == None: #si la lista no tiene ningun dato
            self.first = newNodo #el apuntador primero apunta al nuevo nodo
            self.final = newNodo #el apuntador ultimo apunta al nuevo nodo
        else: #si la lista ya tiene uno o mas datos se agrega el nuevo nodo
            self.final.after = newNodo #el apuntador siguiente apunta al nuevo nodo --->
            newNodo.before = self.final #el apuntador anterior apunta al nodo anterior  <---
            self.final = newNodo #el apuntador ultimo apunta al nuevo nodo

    def printListMuestra(self):
        print("No. | Filas | Columnas | Codigo | Descripción"  )
        count = 0
        nodoTemporal = Nodo("")
        nodoTemporal = self.first
        while nodoTemporal != None:
            count +=1
            print(str(count) + "  | "+str(nodoTemporal.dato.getFilasMuestra()) + "  | "+ str(nodoTemporal.dato.getColumnasMuestra())+ "  | "+ str(nodoTemporal.dato.getCodigoMuestra())+ "  | "+ str(nodoTemporal.dato.getDescripcionMuestra()))
            nodoTemporal = nodoTemporal.after #pasa al siguiente nodo de la lista
            
    def recorrListMuestra(self, rec):
        print("No. | Fila | Columna | Codigo Organismo"  )
        count = 0
        nodoTemporal = Nodo("")
        nodoTemporal = self.first
        while nodoTemporal != None:
            count +=1
            if count == rec:
                listaTemporal = nodoTemporal.dato.listado_CVivas
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

    #OBTENER DATOS DE MUESTRAS
    def getDatoC(self, rec):
        count = 0
        nodoTemporal = Nodo("")
        nodoTemporal = self.first
        while nodoTemporal != None:
            count +=1
            if count == rec:
                return nodoTemporal.dato
            nodoTemporal = nodoTemporal.after #pasa al siguiente nodo de la lista
    
    def getListaCViva(self):
        nodoTemporal1 = Nodo("") 
        nodoTemporal1 = self.first
        while nodoTemporal1 != None:
            # ingresar la cadena y agregar a la cadena el nombre del organismo y luego retornar la cadena para ingresarla al .dot
            print("   | "+str(nodoTemporal1.dato.getFilaCeldaViva())+ "   | "+str(nodoTemporal1.dato.getColumnaCeldaViva())+ "      | "+str(nodoTemporal1.dato.getCodigoCeldaOrganismoVivo()))
            #borrar el print
            nodoTemporal1 = nodoTemporal1.after

    #OBTENER DATOS DE MUESTRAS
    def getDatoC(self, rec):
        count = 0
        nodoTemporal = Nodo("")
        nodoTemporal = self.first
        while nodoTemporal != None:
            count +=1
            if count == rec:
                return nodoTemporal.dato
            nodoTemporal = nodoTemporal.after #pasa al siguiente nodo de la lista
    
    def getListaCViva(self):
        nodoTemporal1 = Nodo("") 
        nodoTemporal1 = self.first
        while nodoTemporal1 != None:
            # ingresar la cadena y agregar a la cadena el nombre del organismo y luego retornar la cadena para ingresarla al .dot
            print("   | "+str(nodoTemporal1.dato.getFilaCeldaViva())+ "   | "+str(nodoTemporal1.dato.getColumnaCeldaViva())+ "      | "+str(nodoTemporal1.dato.getCodigoCeldaOrganismoVivo()))
            #borrar el print
            nodoTemporal1 = nodoTemporal1.after

    