from nodo import Nodo
class Lista:
    def __init__(self):
        self. first = None
        self. final = None

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

    def printList(self):
        count = 0
        nodoTemporal = Nodo("")
        nodoTemporal = self.first
        while nodoTemporal != None:
            count +=1
            print("Nodo no. "+ str(count)+" valor: "+ str(nodoTemporal.dato.getNommbreOrganismo()))
            nodoTemporal = nodoTemporal.after #pasa al siguiente nodo de la lista

'''
from NodoCurso import Curso

class ListaDoble():
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0

    def insertarCursoAlFinal(self, cod, nombre):
        nuevo_curso = Curso(cod, nombre) # primer paso
        self.size += 1
        if self.primero is None:
            self.primero = nuevo_curso
            self.ultimo = nuevo_curso 
        else: 
            self.ultimo.setSiguiente(nuevo_curso)
            nuevo_curso.setAnterior(self.ultimo)
            self.ultimo = nuevo_curso

    def mostrarCursos(self):
        tmp = self.primero
        for i in range(self.size):
            print('Cod', tmp.cod, 'Nombre:',tmp.nombre)
            tmp = tmp.getSiguiente()

Lista_doble = ListaDoble()
Lista_doble.insertarCursoAlFinal(6,"nombre1")
Lista_doble.insertarCursoAlFinal(8,"Nombre2")
Lista_doble.mostrarCursos()
'''