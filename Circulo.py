class Circulo():

    def __init__(self):
        self.diametro = 0
        self.pi = 3.1416

    def establecerParametros(self, diametro):
        self.diametro = diametro

    def calcularArea(self):
        radio = self.diametro / 2
        area = self.pi * radio ** 2
        return 'El área de un circulo es: ' + str(area) + ' cm'

    def calcularPerimetro(self):
        radio = self.diametro / 2
        perimetro = 2 * self.pi * radio
        return 'El perimetro del circulo es: ' + str(perimetro) + ' cm'
