class CeldaViva:
    def __init__(self, fila_CeldaViva, columna_CeldaViva, codigo_CeldaOrganismoVivo):
        self.fila_CeldaViva = fila_CeldaViva
        self.columna_CeldaViva = columna_CeldaViva
        self.codigo_CeldaOrganismoVivo = codigo_CeldaOrganismoVivo

    def setFilaCeldaViva(self, filaViva):
        self.fila_CeldaViva = filaViva

    def getFilaCeldaViva(self):
        return self.fila_CeldaViva

    def setColumnaCeldaViva(self, columnaViva):
        self.columna_CeldaViva = columnaViva

    def getColumnaCeldaViva(self):
        return self.columna_CeldaViva

    def setCodigoCeldaOrganismoVivo(self, codigoViva):
        self.codigo_CeldaOrganismoVivo = codigoViva

    def getCodigoCeldaOrganismoVivo(self):
        return self.codigo_CeldaOrganismoVivo