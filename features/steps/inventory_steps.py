import os
import sys

# Permite importar inventory.py (esta en la raiz del proyecto) desde los steps.
sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")),
)

from behave import given, when, then  # noqa: E402
from inventory import add_product, find_product, list_products, remove_product  # noqa: E402  # noqa: E402


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
    
# Feature 4: Eliminar un producto (Miembro 4)

@given('the inventory is empty')
def step_impl(context):
    context.inventory = []


@when('the user removes the product "{product}"')
def step_impl(context, product):
    ok, mensaje = remove_product(context.inventory, product)
    context.ok = ok
    context.output = mensaje


@then('the inventory should not contain "{product}"')
def step_impl(context, product):
    assert find_product(context.inventory, product) is None, \
        f'El producto "{product}" todavia esta en el inventario'


@then('the output should be "{message}"')
def step_impl(context, message):
    assert context.output == message, \
        f'Expected "{message}" but got "{context.output}"'