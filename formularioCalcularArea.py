class calcularArea():

    def __init__(self):
        self.figuraGeometrica = ''
        self.ladoFiguraCuadrado = 0;

    def elegirFigura(self, figuraGeometrica):
        self.figuraGeometrica = figuraGeometrica

    def darLongitudCuadrado(self, ladoFigura):
        self.ladoFiguraCuadrado = ladoFigura;

    def verAreaCuadrado(self):
        area = self.ladoFiguraCuadrado*self.ladoFiguraCuadrado
        return  'El area de la figura '+self.figuraGeometrica+' es: '+str(area)+' cm'