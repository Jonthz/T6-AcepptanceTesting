# language: en

Feature: Inventory Management
  Como usuario del sistema de inventario
  Quiero gestionar mis productos
  Para llevar el control de mi stock

  Scenario: Agregar un producto al inventario
    Given el inventario esta vacio
    When el usuario agrega un producto "Coffee"
    Then el inventario deberia contener "Coffee"

  Scenario: List all products in the inventory
    Given the inventory contains products:
      | Product |
      | Coffee  |
      | Sugar   |
    When the user lists all products
    Then the output should contain:
      """
      Products:
      - Coffee
      - Sugar
      """

  Scenario: Update the quantity of a product
    Given the inventory contains products:
      | Product | Quantity |
      | Coffee  | 10       |
    When the user updates product "Coffee" to quantity "25"
    Then the inventory should show product "Coffee" with quantity "25"





# ===========================================================================
# Funcionalidad 5: Buscar producto por nombre (Miembro 5)
# ===========================================================================

  Scenario: Filtrar productos que contienen una palabra especifica
    Given the inventory contains products:
      | Product      |
      | Black Coffee |
      | Sugar        |
      | Iced Coffee  |
    When el usuario busca la palabra "Coffee"
    Then 2 productos coincidiran
    And los nombres de los productos son:
      | Product      |
      | Black Coffee |
      | Iced Coffee  |

  Scenario: Buscar un producto que no existe (Interaccion fallida)
    Given the inventory contains products:
      | Product |
      | Coffee  |
      | Sugar   |
    When el usuario busca la palabra "Tea"
    Then 0 productos coincidiran
    And el sistema muestra el mensaje "No se encontraron productos que coincidan con 'Tea'"
    

# ===========================================================================
# Espacio para las demas features del equipo (5 features / 5 scenarios total)
# ---------------------------------------------------------------------------
# Feature 4: Eliminar producto       -> Miembro 4
# Feature 5: (feature extra)         -> Miembro 5
# ===========================================================================