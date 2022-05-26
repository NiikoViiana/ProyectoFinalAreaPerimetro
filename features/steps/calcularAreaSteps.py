from behave import *
from Cuadrado import *
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