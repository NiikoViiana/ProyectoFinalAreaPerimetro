class Triangulo():

    def __init__(self):
        self.base = 0
        self.altura = 0
        self.ladoUno = 0
        self.ladoDos = 0
        self.ladoTres = 0

    def establecerParametros(self, baseFigura, alturaFigura, ladoUnoFigura, ladoDosFigura, ladoTresFigura):
        self.base = baseFigura
        self.altura = alturaFigura
        self.ladoUno = ladoUnoFigura
        self.ladoDos = ladoDosFigura
        self.ladoTres = ladoTresFigura

    def calcularArea(self):
        area = self.base * self.altura
        return 'El área de un triangulo es: ' + str(area) + ' cm'

    def calcularPerimetro(self):
        perimetro = self.ladoUno + self.ladoDos + self.ladoTres
        return 'El área del triangulo es: ' + str(perimetro) + ' cm'
