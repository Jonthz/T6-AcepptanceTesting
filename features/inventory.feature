# language: en

Feature: Agregar un producto al inventario
  Como usuario del sistema de inventario
  Quiero agregar productos
  Para llevar el control de mi stock

  Scenario: Agregar un producto al inventario
    Given el inventario esta vacio
    When el usuario agrega un producto "Coffee"
    Then el inventario deberia contener "Coffee"


# ===========================================================================
# Espacio para las demas features del equipo (5 features / 5 scenarios total)
# ---------------------------------------------------------------------------
# Feature 2: Listar productos        -> Miembro 2
# Feature 3: Actualizar cantidad     -> Miembro 3
# Feature 4: Eliminar producto       -> Miembro 4
# Feature 5: (feature extra)         -> Miembro 5
# ===========================================================================
