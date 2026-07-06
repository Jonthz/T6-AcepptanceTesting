import os
import sys

# Permite importar inventory.py (esta en la raiz del proyecto) desde los steps.
sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")),
)

from behave import given, when, then  # noqa: E402
from inventory import add_product, find_product  # noqa: E402


# ---------------------------------------------------------------------------
# Feature 1: Agregar un producto (Miembro 1)
# ---------------------------------------------------------------------------

@given('el inventario esta vacio')
def step_impl(context):
    context.inventory = []


@when('el usuario agrega un producto "{nombre}"')
def step_impl(context, nombre):
    ok, mensaje = add_product(context.inventory, nombre)
    context.ok = ok
    context.mensaje = mensaje


@then('el inventario deberia contener "{nombre}"')
def step_impl(context, nombre):
    assert find_product(context.inventory, nombre) is not None, \
        f'El producto "{nombre}" no se encontro en el inventario'