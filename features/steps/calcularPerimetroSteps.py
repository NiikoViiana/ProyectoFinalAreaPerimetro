from behave import *
from Cuadrado import *

@given('Accedo al formulario de Calcular Perímetro')
def ejecutarFormulario(context):
    context.cuadrado = Cuadrado()


@given('Elijo la figura geométrica Cuadrado para el perímetro')
def elegirFiguraCuadrado(context):
    context.cuadrado = Cuadrado()


@when('Añado la longitud del cuadrado para el perímetro')
def darLongitudCuadrado(context):
    context.cuadrado.establecerLongitud(4)


@then('Ver el perímetro del cuadrado')
def calcularPerimetro(context):
    context.cuadrado.calcularArea()