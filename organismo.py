class Organismo:
    def __init__(self, codigo_Organismo, nombre_Organismo):
        self.codigo_Organismo = codigo_Organismo
        self.nombre_Organismo = nombre_Organismo

    def setCodigoOrganismo(self, codigo):
        self.codigo_Organismo = codigo

    def getCodigoOrganismo(self):
        return self.codigo_Organismo

    def setNombreOrganismo(self, nombre):
        self.nombre_Organismo = nombre

    def getNommbreOrganismo(self):
        return self.nombre_Organismo
