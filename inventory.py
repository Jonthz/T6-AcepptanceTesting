"""
Inventory Manager - Aplicacion de consola
Software Engineering II - Acceptance Testing Workshop (I Term 2026)

Base del proyecto y funcionalidades integradas.
Modelo de datos:
    El inventario es una lista de diccionarios.
    Cada producto tiene 4 atributos:
        nombre    (str)   -> identificador del producto
        cantidad  (int)   -> unidades en stock
        precio    (float) -> precio unitario
        categoria (str)   -> categoria a la que pertenece
"""


# ---------------------------------------------------------------------------
# Funciones del dominio (usadas por el CLI y por los acceptance tests)
# ---------------------------------------------------------------------------

def add_product(inventory, nombre, cantidad=0, precio=0.0, categoria="General"):
    """Agrega un producto al inventario.

    No permite nombres duplicados (compara sin distinguir mayusculas).
    Retorna una tupla (ok: bool, mensaje: str).
    """
    if not nombre or not nombre.strip():
        return False, "El nombre del producto no puede estar vacio"

    if find_product(inventory, nombre) is not None:
        return False, f'El producto "{nombre}" ya existe en el inventario'

    inventory.append({
        "nombre": nombre,
        "cantidad": int(cantidad),
        "precio": float(precio),
        "categoria": categoria,
    })
    return True, f'Producto "{nombre}" agregado al inventario'


def find_product(inventory, nombre):
    """Busca un producto por nombre (sin distinguir mayusculas).

    Retorna el diccionario del producto o None si no existe.
    """
    for producto in inventory:
        if producto["nombre"].lower() == nombre.lower():
            return producto
    return None


def list_products(inventory):
    """Feature 2 - Lista todos los productos del inventario."""
    if not inventory:
        print("El inventario esta vacio")
        return

    print("Products:")
    for producto in inventory:
        print(f'- {producto["nombre"]}')


def update_quantity(inventory, nombre, nueva_cantidad):
    """Feature 3 - Actualiza la cantidad de un producto existente."""
    producto = find_product(inventory, nombre)

    if not producto:
        return False, f'El producto "{nombre}" no existe en el inventario'

    try:
        nueva_cantidad_int = int(nueva_cantidad)
    except ValueError:
        return False, "La cantidad debe ser un numero entero"

    producto["cantidad"] = nueva_cantidad_int
    return True, f'Cantidad de "{nombre}" actualizada a {nueva_cantidad_int}'


def remove_product(inventory, nombre):
    """Feature 4 - Elimina un producto del inventario.

    Retorna (ok, mensaje). El mensaje va en ingles para coincidir con el
    escenario de interaccion fallida del enunciado ("Product Coffee was not found").
    """
    producto = find_product(inventory, nombre)
    if producto is None:
        return False, f"Product {nombre} was not found"
    inventory.remove(producto)
    return True, f"Product {nombre} was removed"


def search_products(inventory, keyword):
    """Feature 5 - Busca productos que contengan la palabra clave en su nombre."""
    # Filtra usando una comprension de listas y comparando en minusculas
    resultados = [p for p in inventory if keyword.lower() in p["nombre"].lower()]

    if not resultados:
        print(f"No se encontraron productos que coincidan con '{keyword}'")
    else:
        print(f"{len(resultados)} productos coinciden:")
        for p in resultados:
            print(f"- {p['nombre']} (Stock: {p['cantidad']}, Precio: ${p['precio']}, Categoria: {p['categoria']})")

    return resultados


# ---------------------------------------------------------------------------
# Interfaz de linea de comandos
# ---------------------------------------------------------------------------

def _leer_int(mensaje, por_defecto=0):
    valor = input(mensaje).strip()
    if valor == "":
        return por_defecto
    try:
        return int(valor)
    except ValueError:
        print("  Valor invalido, se usara 0.")
        return 0


def _leer_float(mensaje, por_defecto=0.0):
    valor = input(mensaje).strip()
    if valor == "":
        return por_defecto
    try:
        return float(valor)
    except ValueError:
        print("  Valor invalido, se usara 0.0.")
        return 0.0


def menu():
    inventory = []

    opciones = (
        "\n===== INVENTORY MANAGER =====\n"
        "1. Agregar producto\n"
        "2. Listar productos\n"
        "3. Actualizar cantidad\n"
        "4. Eliminar producto\n"
        "5. Buscar producto\n"
        "0. Salir\n"
    )

    while True:
        print(opciones)
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            nombre = input("Nombre del producto: ").strip()
            cantidad = _leer_int("Cantidad: ")
            precio = _leer_float("Precio: ")
            categoria = input("Categoria: ").strip() or "General"
            ok, mensaje = add_product(inventory, nombre, cantidad, precio, categoria)
            print(mensaje)
        elif opcion == "2":
            list_products(inventory)
        elif opcion == "3":
            nombre = input("Nombre del producto: ").strip()
            nueva = _leer_int("Nueva cantidad: ")
            ok, mensaje = update_quantity(inventory, nombre, nueva)
            print(mensaje)
        elif opcion == "4":
            nombre = input("Nombre del producto: ").strip()
            ok, mensaje = remove_product(inventory, nombre)
            print(mensaje)
        elif opcion == "5":
            keyword = input("Ingrese el nombre o palabra clave a buscar: ").strip()
            search_products(inventory, keyword)
        elif opcion == "0":
            print("Hasta luego.")
            break
        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    menu()
