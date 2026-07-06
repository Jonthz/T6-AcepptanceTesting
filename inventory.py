"""
Inventory Manager - Aplicacion de consola
Software Engineering II - Acceptance Testing Workshop (I Term 2026)

Base del proyecto y funcionalidad "Agregar producto" (Miembro 1).
La estructura de datos definida aqui es la que usaran las demas features.

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


# ---------------------------------------------------------------------------
# Operaciones de las demas features (a cargo de otros miembros del equipo).
# Se dejan como stubs para que el programa corra sin errores.
# ---------------------------------------------------------------------------

def list_products(inventory):
    """Feature 2 - Listar productos (otro miembro)."""
    # TODO: implementar
    print("[Pendiente] Listar productos")


def update_quantity(inventory, nombre, nueva_cantidad):
    """Feature 3 - Actualizar cantidad (otro miembro)."""
    # TODO: implementar
    print("[Pendiente] Actualizar cantidad")


def remove_product(inventory, nombre):
    """Feature 4 - Eliminar producto (otro miembro)."""
    # TODO: implementar
    print("[Pendiente] Eliminar producto")


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
        "5. (Feature extra)\n"
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
            update_quantity(inventory, nombre, nueva)
        elif opcion == "4":
            nombre = input("Nombre del producto: ").strip()
            remove_product(inventory, nombre)
        elif opcion == "5":
            print("[Pendiente] Feature extra")
        elif opcion == "0":
            print("Hasta luego.")
            break
        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    menu()