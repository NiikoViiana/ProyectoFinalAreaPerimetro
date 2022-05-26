from behave import *
from Cuadrado import *
from Triangulo import *
from Circulo import *
from selenium import webdriver

@given('Accedo al formulario de Calcular Áreas')
def ejecutarFormulario(context):
    context.cuadrado = Cuadrado()


@given('Elijo la figura geométrica Cuadrado para el area')
def elegirFiguraCuadrado(context):
    context.cuadrado = Cuadrado()


@when('Añado la longitud del cuadrado para el area')
def darLongitudCuadrado(context):
    context.cuadrado.establecerLongitud(4)


@then('Ver el área del cuadrado')
def calcularArea(context):
    context.cuadrado.calcularArea()

### triangulo
@given('Accedo al formulario de Calcular Áreas Triangulo')
def ejecutarFormularioTriangulo(context):
    context.triangulo = Triangulo()


@given('Elijo la figura geométrica Triangulo para el area')
def elegirFiguraTriangulo(context):
    context.triangulo = Triangulo()


@when('Añado la base y la altura del triangulo para el area')
def ingresarDatosTriangulo(context):
    context.triangulo.establecerParametros(10, 15, 12, 16.16, 16.16)


@then('Ver el área del triangulo')
def calcularAreaTriangulo(context):
    context.triangulo.calcularArea()

### Circulo
@given('Accedo al formulario de Calcular Áreas Circulo')
def ejecutarFormularioCirculo(context):
    context.circulo = Circulo()


@given('Elijo la figura geométrica Circulo para el area')
def elegirFiguraCirculo(context):
    context.circulo = Circulo()


@when('Añado el diametro del circulo para el area')
def ingresarDatosCirculo(context):
    context.circulo.establecerParametros(10)


@then('Ver el área del circulo')
def calcularAreaCirculo(context):
    context.circulo.calcularArea()