import os
import sys
from contextlib import redirect_stdout
from io import StringIO
from inventory import add_product, find_product, list_products, search_products 

# Permite importar inventory.py (esta en la raiz del proyecto) desde los steps.
sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")),
)

from behave import given, when, then  # noqa: E402
from inventory import add_product, find_product, list_products, update_quantity, remove_product


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


# ---------------------------------------------------------------------------
# Feature 5: Buscar producto (Miembro 5)
# ---------------------------------------------------------------------------

@when('el usuario busca la palabra "{keyword}"')
def step_impl(context, keyword):
    # Usamos StringIO para capturar lo que la funcion imprime en la consola
    # Esto es vital para poder evaluar el mensaje de error en el escenario fallido
    output = StringIO()
    with redirect_stdout(output):
        context.resultados = search_products(context.inventory, keyword)
    
    # Guardamos la salida impresa en el context para el ultimo 'Then'
    context.output = output.getvalue().strip()

@then('{cantidad} productos coincidiran')
def step_impl(context, cantidad):
    # Convertimos 'cantidad' a entero porque desde Gherkin llega como string
    cantidad_esperada = int(cantidad)
    cantidad_obtenida = len(context.resultados)
    
    assert cantidad_obtenida == cantidad_esperada, \
        f"Se esperaban {cantidad_esperada} resultados, pero se obtuvieron {cantidad_obtenida}"

@then('los nombres de los productos son:')
def step_impl(context):
    # Extraemos solo los nombres de los diccionarios encontrados
    nombres_encontrados = [p['nombre'] for p in context.resultados]
    
    # Comparamos cada fila de la tabla de Gherkin con nuestra lista
    for row in context.table:
        nombre_esperado = row['Product']
        assert nombre_esperado in nombres_encontrados, \
            f"Se esperaba encontrar '{nombre_esperado}' en los resultados de busqueda"

@then('el sistema muestra el mensaje "{mensaje}"')
def step_impl(context, mensaje):
    assert mensaje in context.output, \
        f"Se esperaba el mensaje '{mensaje}', pero la consola mostro: '{context.output}'"
