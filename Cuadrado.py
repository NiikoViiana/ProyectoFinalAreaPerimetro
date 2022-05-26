class Cuadrado():

    def __init__(self):
        self.lados = 0

    def establecerLongitud(self, ladoFigura):
        self.lados = ladoFigura

    def calcularArea(self):
        area = self.lados*self.lados
        return  'El área del cuadrado es: '+str(area)+' cm'