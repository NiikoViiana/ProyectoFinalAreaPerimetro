Feature: Calcular el perímetro de una figura geométrica

  Scenario: Perímetro de un cuadrado
    Given Accedo al formulario de Calcular Perímetro
    And Elijo la figura geométrica Cuadrado para el perímetro
    When Añado la longitud del cuadrado para el perímetro
    Then Ver el perímetro del cuadrado


  Scenario: Perímetro de un triangulo
    Given Accedo al formulario de Calcular Perímetro triangulo
    And Elijo la figura geométrica Triangulo para el perímetro
    When Añado los tres lados del triangulo para el perímetro
    Then Ver el perímetro del triangulo


  Scenario: Perímetro de un circulo
    Given Accedo al formulario de Calcular Perímetro circulo
    And Elijo la figura geométrica circulo para el perímetro
    When Añado diametro del circulo para el perímetro
    Then Ver el perímetro del circulo