Feature: Calcular el área de una figura geométrica

  Scenario: Área de un cuadrado
    Given Accedo al formulario de Calcular Áreas
    And Elijo la figura geométrica Cuadrado para el area
    When Añado la longitud del cuadrado para el area
    Then Ver el área del cuadrado


  Scenario: Área de un triangulo
    Given Accedo al formulario de Calcular Áreas Triangulo
    And Elijo la figura geométrica Triangulo para el area
    When Añado la base y la altura del triangulo para el area
    Then Ver el área del triangulo