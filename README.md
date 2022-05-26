# ProyectoFinalAreaPerimetro
Proyecto final para la clase de Metodologia que involucra al BDD Behave que permita calcular el area y perimetro de las figuras cuadrado, triangulo y circulo

## Integrantes
- Natalia Paez
- Nicolas Viana
- William Sanabria

## Datos de la aplicación
- Python 3.10.4
- BDD Behave 1.2.6
- Pip 22.0.0
- Uso de lenguaje Gherkin

## Instrucciones para usar el proyecto
- Clonar el proyecto `git clone https://github.com/NiikoViiana/ProyectoFinalAreaPerimetro.git`
- Ejecutar Features
  - - Para calcular el area: `behave .\features\calcularArea.feature`
  - - Para calcular el perimtero: `behave .\features\calcularPerimetro.feature` 


# Historias de usuario
## Estudiante

  ✅ Como estudiante quiero calcular el área de un cuadrado, para obtener el área de la figura.  
  ✅ Como estudiante quiero calcular el área de un triángulo, para obtener el área de la figura.  
  ✅ Como estudiante quiero calcular el área de un círculo, para obtener el área de la figura.  
  ✅ Como estudiante quiero calcular el perímetro de un cuadrado, para obtener el perímetro de la figura.  
  ✅ Como estudiante quiero calcular el perímetro de un triángulo, para obtener el perímetro de la figura.  
  ✅ Como estudiante quiero calcular el perímetro de un círculo, para obtener el perímetro de la figura.
 
## Reglas o normas de trabajo:
  - Los datos ingresados se toman en centímetros

# Lenguaje Gherkin
![Image text](https://github.com/NiikoViiana/ProyectoFinalAreaPerimetro/blob/main/imagenes/areaFeature.png)
![Image text](https://github.com/NiikoViiana/ProyectoFinalAreaPerimetro/blob/main/imagenes/periodoFeature.png)

# Código
## Steps Feature Area
![Image text](https://github.com/NiikoViiana/ProyectoFinalAreaPerimetro/blob/main/imagenes/AreaStep.png)
![Image text](https://github.com/NiikoViiana/ProyectoFinalAreaPerimetro/blob/main/imagenes/areaStepTriangulo.png)
![Image text](https://github.com/NiikoViiana/ProyectoFinalAreaPerimetro/blob/main/imagenes/AreaStepCirculo.png)

## Steps Feature Perimetro
![Image text](https://github.com/NiikoViiana/ProyectoFinalAreaPerimetro/blob/main/imagenes/perimetroStepCuadrado.png)
![Image text](https://github.com/NiikoViiana/ProyectoFinalAreaPerimetro/blob/main/imagenes/PerimetroStepTriangulo.png)
![Image text](https://github.com/NiikoViiana/ProyectoFinalAreaPerimetro/blob/main/imagenes/perimetroStepCirculo.png)

## Clases
### Cuadrado
![Image text](https://github.com/NiikoViiana/ProyectoFinalAreaPerimetro/blob/main/imagenes/CuadradoClass.png)
### Triangulo
![Image text](https://github.com/NiikoViiana/ProyectoFinalAreaPerimetro/blob/main/imagenes/TrianguloClass.png)
### Circulo
![Image text](https://github.com/NiikoViiana/ProyectoFinalAreaPerimetro/blob/main/imagenes/CirculoClass.png)


# Pruebas de aceptación
## Estudiante
### Feature: Calcular el área de una figura geométrica
![Image text](https://raw.githubusercontent.com/NiikoViiana/ProyectoFinalAreaPerimetro/main/imagenes/area.jpeg)

### Feature: Calcular el perímetro de una figura geométrica
![Image text](https://raw.githubusercontent.com/NiikoViiana/ProyectoFinalAreaPerimetro/main/imagenes/perimetro.jpeg)


