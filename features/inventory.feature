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
    
  Scenario: Remove a product from the inventory
    Given the inventory contains products:
      | Product |
      | Coffee  |
      | Sugar   |
    When the user removes the product "Coffee"
    Then the inventory should not contain "Coffee"

  Scenario: Remove a product that does not exist
    Given the inventory is empty
    When the user removes the product "Coffee"
    Then the output should be "Product Coffee was not found"

# ===========================================================================
# Espacio para las demas features del equipo (5 features / 5 scenarios total)
# ---------------------------------------------------------------------------
# Feature 4: Eliminar producto       -> Miembro 4
# Feature 5: (feature extra)         -> Miembro 5
# ===========================================================================