import os
import sys
from contextlib import redirect_stdout
from io import StringIO

# Permite importar inventory.py (esta en la raiz del proyecto) desde los steps.
sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")),
)

from behave import given, when, then  # noqa: E402
from inventory import add_product, find_product, list_products, update_quantity 


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


# ---------------------------------------------------------------------------
# Feature 2: Listar todos los productos (Miembro 2)
# ---------------------------------------------------------------------------

@given('the inventory contains products:')
def step_impl(context):
    context.inventory = []

    for row in context.table:
        ok, mensaje = add_product(
            context.inventory,
            row["Product"],
        )
        assert ok, mensaje


@when('the user lists all products')
def step_impl(context):
    output = StringIO()
    with redirect_stdout(output):
        list_products(context.inventory)
    context.output = output.getvalue()


@then('the output should contain:')
def step_impl(context):
    expected_output = context.text.strip()
    actual_output = context.output.strip()

    assert expected_output in actual_output, \
        f'Expected output to contain "{expected_output}" but got "{actual_output}"'


# ---------------------------------------------------------------------------
# Feature 3: Actualizar cantidad (Miembro 3)
# ---------------------------------------------------------------------------

@when('the user updates product "{product}" to quantity "{quantity}"')
def step_impl(context, product, quantity):
    ok, mensaje = update_quantity(context.inventory, product, quantity)
    context.ok = ok
    context.mensaje = mensaje


@then('the inventory should show product "{product}" with quantity "{quantity}"')
def step_impl(context, product, quantity):
    producto = find_product(context.inventory, product)
    
    assert producto is not None, f'El producto "{product}" no se encontro'
    
    assert str(producto["cantidad"]) == str(quantity), \
        f'Se esperaba cantidad {quantity} pero se obtuvo {producto["cantidad"]}'