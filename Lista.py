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
            #newNodo.before = self.final #el apuntador anterior apunta al nodo anterior  <---
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
                #listaTemporal.BubbleSort()
                #listaTemporal.BubbleSortC()
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
    
    #OBTENER DATOS DE LISTA DE cOLORES
    def getDatoNOCO(self):
        almacenar = ""
        nodoTemporal = Nodo("")
        nodoTemporal = self.first
        while nodoTemporal != None:
            almacenar = almacenar + '''<TR>
                <TD BGCOLOR="''' +nodoTemporal.dato.getNommbreColor()+'''" width= "35" height = "35"></TD>
                <TD width= "35" height = "35">'''+nodoTemporal.dato.getNombreORGANISMO()+ '''</TD>
            </TR>
            '''
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
                            tmp = j.after #SIGUIENTE SE GUARDA EN TEMPORAL
                            i.after = j  # 
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
    #INSERTANDO EN ORDEN
    def insertarOrden(self, dato):
        newNodo = Nodo(dato) # se crea un nuevo nodo
        #si la lista está vacia
        self.size += 1
        if self.first == None: #si la lista no tiene ningun dato
            self.first = newNodo #el apuntador primero apunta al nuevo nodo
            #self.final = newNodo #el apuntador ultimo apunta al nuevo nodo
        #si el dato de entrada es menor al dato anterior    
        elif (newNodo.dato.getFilaCeldaViva() < self.first.dato.getFilaCeldaViva()): 
            newNodo.after = self.first
            self.first = newNodo
        else:
            anterior1 = Nodo("")
            p = Nodo("")
            anterior1 = self.first
            p = self.first
            while (p.after != None) and (newNodo.dato.getFilaCeldaViva() > p.dato.getFilaCeldaViva()):
                anterior1 = p
                p = p.after
            if (newNodo.dato.getFilaCeldaViva()> p.dato.getFilaCeldaViva()):
                anterior1 = p
            newNodo.after = anterior1.after
            anterior1.after = newNodo
        return self

    #METODOS PARA VALIDACIONES DE PROSPERAR
    def validandoHorizontal(self, totalFilas, totalColumnas, lcv):
        nodoTemporal = Nodo("")
        nodoTemporal = self.first
        while nodoTemporal != None:
            # mantiene la lista para seguirla recorriendo como auxiliar
            listaAuxiliar = lcv 
            #enviando a la lista auxiliar la posición actual que se está recorriendo 
            listaAuxiliar.validandoRepetidos(nodoTemporal.dato.getFilaCeldaViva(),nodoTemporal.dato.getColumnaCeldaViva(), nodoTemporal.dato.getCodigoCeldaOrganismoVivo())

            nodoTemporal = nodoTemporal.after #pasa al siguiente nodo de la lista

    def validandoRepetidos(self, filaActual, columnaActual, codigoCVActual):
        nodoTemporal = Nodo("")
        nodoTemporal = self.first
        while nodoTemporal != None:
            #valida que si es la posición actual la que se está recorriendo entonces pasa al siguiente dato de la lista
            if (int(nodoTemporal.dato.getFilaCeldaViva()) == int(filaActual)) and (int(nodoTemporal.dato.getColumnaCeldaViva()) == int(columnaActual) and (nodoTemporal.dato.getCodigoCeldaOrganismoVivo() == codigoCVActual)):
                #pasa al siguiente dato de la lista
                nodoTemporal = nodoTemporal.after
            # valida que si el siguiente esta en la misma fila pero en diferente columna y si el codigo es el mismo
            if (int(nodoTemporal.dato.getFilaCeldaViva()) == int(filaActual)) and (int(nodoTemporal.dato.getColumnaCeldaViva()) != int(columnaActual)and ((nodoTemporal.dato.getCodigoCeldaOrganismoVivo() == codigoCVActual))):
                #valida que el codigo sea el mismo, 
                #cuando sea la misma fila, pero diferente columna validar si el codigo es el mismo y almacenarlo en una lista de iguales
                listaIguales = Lista()
                #enviar un objeto donde se almacene las posiciones de las columnas, actual y el siguiente
                #si la resta entre la columna siguiente y la actual es mayor que 1 entonces almacenar la ultima coincidencia
                resta = int(columnaActual)- int(nodoTemporal.dato.getColumnaCeldaViva())
                if resta > 1:
                    listaIguales.addFinalNode(int(nodoTemporal.dato.getColumnaCeldaViva()))
                elif resta == 1:
                    #el dato muere ya que no hay otro dato dentro del rango
                    datoVive = "Muere"
            # valida que si el siguiente esta en la misma fila pero en diferente columna y si el codigo es diferente
            if (int(nodoTemporal.dato.getFilaCeldaViva()) == int(filaActual)) and (int(nodoTemporal.dato.getColumnaCeldaViva()) != int(columnaActual)and ((nodoTemporal.dato.getCodigoCeldaOrganismoVivo() != codigoCVActual))):
                #si la posición de este codigo se encuentra entre la posición del los otros codigos entonces convertir este dato en el otro codigo

                pass
            '''
            revisar bien todo el codigo anterior ya que algo no funciona
            primero se esta validando que todos los datos sean iguales, entonces los omita
            si fila permanece y columna no es igual y codigo es el mismo se tiene el mismo organismo entonces almacenar en una lista con datos iguales
            si fila permanece y columna no es igual y codigo no es el mismo y recorriendo la lista de datos iguales se verifica que este dato se encuentre entre la primera coincidencia y la segunda coincidencia de los datos que son iguales, entonces este dato se convierte igual a los otros. 
            '''  
            
            nodoTemporal = nodoTemporal.after #pasa al siguiente nodo de la lista
    #METODO PARA DEJAR VACÍA LA LISTA
    def vaciarLista(self):
        self.first = None
        self.final = None
    def ValidarListaVacia(self):
        #si la lista No está vacía devuelve True
        if self.first != None:
            return True
        #Si la lista está Vacia devuelve False
        if self.first == None:
            return False

    #METODO PARA AGREGAR DATOS A LA ESCRITURA DEL XML
    def agregarEscrituraOrganismo(self,contadorOr, boleanoOrganismo):
        count = 0
        nodoTemporal = Nodo("")
        nodoTemporal = self.first
        boleanoOrganismo = False
        while nodoTemporal != None:
            count +=1
            if count == contadorOr:
                return nodoTemporal.dato
            nodoTemporal = nodoTemporal.after #pasa al siguiente nodo de la lista
        return boleanoOrganismo
    #METODOS PARA LA ACTUALIZACIÓN DE DATOS VALIDACIONES
    def actualizandoLCeldasVivas(self, fil, col):
        nodoTemporal = Nodo("")
        nodoTemporal = self.first
        val = False
        while nodoTemporal != None:
            if (int(nodoTemporal.dato.getFilaCeldaViva()) == fil) and (int(nodoTemporal.dato.getColumnaCeldaViva()) == col) :
                val = True
            nodoTemporal = nodoTemporal.after #pasa al siguiente nodo de la lista
        return val
    
    #METODOS PARA EL INGRESO DE DATOS VALIDACIONES
    def ingresandoLCeldasVivas(self, fil, col):
        nodoTemporal = Nodo("")
        nodoTemporal = self.first
        val = False
        while nodoTemporal != None:
            if (int(nodoTemporal.dato.getFilaCeldaViva()) == fil) and (int(nodoTemporal.dato.getColumnaCeldaViva()) == col):
                val = True
            nodoTemporal = nodoTemporal.after #pasa al siguiente nodo de la lista
        return val
    def validandoCodigoIgual(self, recibiendoCodigo):
        nodoTemporal = Nodo("")
        nodoTemporal = self.first
        val1 = False
        while nodoTemporal != None:
            if (str(nodoTemporal.dato.getCodigoCeldaOrganismoVivo()) == str(recibiendoCodigo)):
                val1 = True
            nodoTemporal = nodoTemporal.after #pasa al siguiente nodo de la lista
        return val1
    
    def recorrListaCViva1(self):
        print("No. | Fila | Columna | Codigo Organismo"  )
        count1 = 0
        nodoTemporal1 = Nodo("")
        nodoTemporal1 = self.first
        while nodoTemporal1 != None:
            count1 +=1
            print(str(count1)+ "   | "+str(nodoTemporal1.dato.getFilaCeldaViva())+ "   | "+str(nodoTemporal1.dato.getColumnaCeldaViva())+ "      | "+str(nodoTemporal1.dato.getCodigoCeldaOrganismoVivo()))
            nodoTemporal1 = nodoTemporal1.after

    def actualizandoCodigoCV(self, codigoA):
        nodoTemporal = Nodo("")
        nodoTemporal = self.first
        val = False
        while nodoTemporal != None:
            if (str(nodoTemporal.dato.getCodigoOrganismo().lower()) == codigoA.lower()) :
                val = True
            nodoTemporal = nodoTemporal.after #pasa al siguiente nodo de la lista
        return val