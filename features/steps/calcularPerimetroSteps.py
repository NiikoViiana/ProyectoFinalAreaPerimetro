from behave import *
from Cuadrado import *
from Triangulo import *
from Circulo import *

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


##Triangulo
@given('Accedo al formulario de Calcular Perímetro triangulo')
def ejecutarFormularioTriangulo(context):
    context.triangulo = Triangulo()


@given('Elijo la figura geométrica Triangulo para el perímetro')
def elegirFiguraTriangulo(context):
    context.triangulo = Triangulo()


@when('Añado los tres lados del triangulo para el perímetro')
def ingresarDatosTriangulo(context):
    context.triangulo.establecerParametros(10, 15, 12, 16.16, 16.16)


@then('Ver el perímetro del triangulo')
def calcularPerimetroTriangulo(context):
    context.triangulo.calcularPerimetro()

##circulo
@given('Accedo al formulario de Calcular Perímetro circulo')
def ejecutarFormularioCirculo(context):
    context.circulo = Circulo()


@given('Elijo la figura geométrica circulo para el perímetro')
def elegirFiguraCriculo(context):
    context.circulo = Circulo()


@when('Añado diametro del circulo para el perímetro')
def ingresarDatosCirculo(context):
    context.circulo.establecerParametros(10)


@then('Ver el perímetro del circulo')
def calcularPerimetroCircuo(context):
    context.circulo.calcularPerimetro()
