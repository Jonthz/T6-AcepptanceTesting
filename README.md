# T6 - Acceptance Testing BDD

Proyecto de practica para pruebas de aceptacion usando Python, Behave y Gherkin.

## Funcionalidades

- Agregar un nuevo producto al inventario.
- Listar todos los productos.
- Actualizar la cantidad de un producto.
- Eliminar un producto del inventario.
- Buscar productos por nombre.

Cada producto se maneja con al menos cuatro atributos:

- `nombre`
- `cantidad`
- `precio`
- `categoria`

## Estructura

```text
features/
  inventory.feature
  steps/
    inventory_steps.py
inventory.py
requirements.txt
docs/
  evidencia_behave.txt
  reporte_practica.md
  reporte_practica.docx
```

## Preparar el entorno

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Ejecutar la aplicacion

```bash
python inventory.py
```

## Ejecutar pruebas BDD

```bash
behave
```

Resultado validado:

```text
1 feature passed, 0 failed, 0 skipped
7 scenarios passed, 0 failed, 0 skipped
23 steps passed, 0 failed, 0 skipped
```

La evidencia completa de ejecucion esta en `docs/evidencia_behave.txt`.

## Reporte

El reporte final de la practica esta disponible en:

- `docs/reporte_practica.md`
- `docs/reporte_practica.docx`
