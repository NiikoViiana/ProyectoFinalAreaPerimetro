Feature: Calcular el área de una figura geométrica

  Scenario: Área de un cuadrado
    Given Accedo al formulario de Calcular Áreas
    And Elijo la figura geométrica Cuadrado
    When Añado la longitud en cm de cualquier lado de la figura
    Then Ver el área del cuadrado