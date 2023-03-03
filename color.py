class Color:
    def __init__(self, coColor_Organismo, nombre_Color):
        self.coColor_Organismo = coColor_Organismo
        self.nombre_Color = nombre_Color

    def setCoColorOrganismo(self, coColor_Organismo):
        self.coColor_Organismo = coColor_Organismo

    def getCoColorOrganismo(self):
        return self.coColor_Organismo

    def setNombreColor(self, nombre_Color):
        self.nombre_Color = nombre_Color

    def getNommbreColor(self):
        return self.nombre_Color
