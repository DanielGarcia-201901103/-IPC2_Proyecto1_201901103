class Muestra:

    def __init__(self, codigo_Muestra, descripcion_Muestra, filas_Muestra, columnas_Muestra, listado_CVivas):
        self.codigo_Muestra = codigo_Muestra
        self.descripcion_Muestra = descripcion_Muestra
        self.filas_Muestra = filas_Muestra
        self.columnas_Muestra = columnas_Muestra
        self.listado_CVivas = listado_CVivas
        
    def setCodigoMuestra(self, codigoM):
        self.codigo_Muestra = codigoM
    
    def getCodigoMuestra(self):
        return self.codigo_Muestra
    
    def setDescripcionMuestra(self, descripcionM):
        self.descripcion_Muestra = descripcionM
    
    def getDescripcionMuestra(self):
        return self.descripcion_Muestra
    
    def setFilasMuestra(self, filasM):
        self.filas_Muestra = filasM
    
    def getFilasMuestra(self):
        return self.filas_Muestra

    def setColumnasMuestra(self, columnasM):
        self.columnas_Muestra = columnasM
    
    def getColumnasMuestra(self):
        return self.columnas_Muestra