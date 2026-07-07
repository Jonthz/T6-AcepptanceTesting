# Reporte de Practica: Taller de Pruebas de Aceptacion BDD

## Portada

**Asignatura:** Ingenieria de Software II  
**Practica:** Taller de Pruebas de Aceptacion con BDD  
**Proyecto:** Sistema de gestion de inventario  
**Repositorio:** https://github.com/Jonthz/T6-AcepptanceTesting  
**Equipo:** 6 integrantes  
**Responsable de integracion y documentacion:** Miembro 6  
**Fecha de preparacion:** 7 de julio de 2026

## Introduccion

El presente reporte documenta la integracion, verificacion y evidencia de pruebas de aceptacion para un sistema de inventario desarrollado en Python. La practica aplica BDD usando Gherkin y Behave para describir comportamientos esperados desde la perspectiva del usuario y automatizar su validacion.

El sistema permite gestionar productos mediante operaciones basicas de inventario: agregar productos, listar productos existentes, actualizar cantidades, eliminar productos y buscar productos por nombre. Cada producto se maneja como un diccionario con al menos cuatro atributos: nombre, cantidad, precio y categoria.

## Objetivo

Comprobar que las funcionalidades del inventario cumplen los escenarios de aceptacion definidos por el equipo, integrar los steps de Behave con la logica de Python, ejecutar las pruebas automatizadas y entregar evidencia verificable del resultado.

## Herramientas Utilizadas

- Python 3.
- Behave para pruebas BDD.
- Gherkin para redaccion de escenarios.
- Git y GitHub para control de versiones.
- Entorno virtual `.venv` para aislar dependencias.

## Alcance del Proyecto

El proyecto incluye cinco funcionalidades principales:

| Feature | Funcionalidad | Estado |
| --- | --- | --- |
| Feature 1 | Agregar producto al inventario | Implementada y validada |
| Feature 2 | Listar productos del inventario | Implementada y validada |
| Feature 3 | Actualizar cantidad de un producto | Implementada y validada |
| Feature 4 | Eliminar producto del inventario | Implementada y validada |
| Feature 5 | Buscar producto por nombre | Implementada y validada |

Adicionalmente, se validan interacciones fallidas, como intentar eliminar un producto inexistente o buscar un producto que no tiene coincidencias.

## Distribucion del Trabajo

| Miembro | Rol | Responsabilidad |
| --- | --- | --- |
| Miembro 1 | Lider tecnico / Dev | Base del proyecto y feature para agregar producto |
| Miembro 2 | Desarrollador BDD | Feature para listar productos |
| Miembro 3 | Desarrollador BDD | Feature para actualizar cantidad |
| Miembro 4 | Especialista QA | Feature para eliminar producto y escenario fallido |
| Miembro 5 | Desarrollador BDD | Feature adicional para buscar producto |
| Miembro 6 | Release Manager | Integracion, ejecucion de pruebas, evidencia y reporte |

## Estructura del Repositorio

```text
T6-AcepptanceTesting/
├── features/
│   ├── inventory.feature
│   └── steps/
│       └── inventory_steps.py
├── README.md
├── inventory.py
├── requirements.txt
└── docs/
    ├── evidencia_behave.txt
    ├── reporte_practica.md
    └── reporte_practica.docx
```

## Desarrollo de las Funcionalidades

### Feature 1: Agregar Producto

Permite registrar un producto dentro del inventario. El escenario de aceptacion valida que, partiendo de un inventario vacio, al agregar el producto `Coffee`, el inventario lo contenga.

### Feature 2: Listar Productos

Permite visualizar los productos existentes. El escenario utiliza una tabla de datos Gherkin para cargar un inventario inicial con productos y luego verifica que la salida de consola contenga la lista esperada.

### Feature 3: Actualizar Cantidad

Permite modificar la cantidad de un producto existente. La prueba valida que el producto `Coffee` cambie su cantidad de `10` a `25` en la estructura del inventario.

### Feature 4: Eliminar Producto

Permite remover un producto del inventario. Se validan dos comportamientos: la eliminacion exitosa de un producto existente y el mensaje esperado cuando se intenta eliminar un producto inexistente.

### Feature 5: Buscar Producto

Permite filtrar productos por una palabra clave incluida en el nombre. Se valida una busqueda exitosa con dos coincidencias y una busqueda fallida sin resultados.

## Integracion Realizada por el Miembro 6

Durante la integracion se realizaron las siguientes actividades:

1. Se preparo un entorno virtual local con las dependencias del archivo `requirements.txt`.
2. Se ejecuto Behave para comprobar el estado inicial del proyecto.
3. Se reviso la conexion entre `inventory.py`, `features/inventory.feature` y `features/steps/inventory_steps.py`.
4. Se ajusto la carga de tablas Gherkin para soportar columnas opcionales de `Quantity`, `Price` y `Category`.
5. Se corrigio la interfaz de consola para mostrar el mensaje devuelto al eliminar productos.
6. Se genero evidencia de ejecucion en `docs/evidencia_behave.txt`.

## Evidencia de Pruebas

Comando ejecutado:

```bash
behave
```

Resultado obtenido:

```text
1 feature passed, 0 failed, 0 skipped
7 scenarios passed, 0 failed, 0 skipped
23 steps passed, 0 failed, 0 skipped
```

La evidencia completa se encuentra en el archivo `docs/evidencia_behave.txt`.

## Correcciones y Hallazgos

- Se comprobo que las pruebas BDD pasan correctamente con Behave.
- Se fortalecio el step `Given the inventory contains products:` para que pueda cargar productos con cuatro atributos cuando la tabla Gherkin los provee.
- Se mantuvo compatibilidad con escenarios que solo declaran la columna `Product`.
- Se ajusto el menu de consola para imprimir el resultado de la operacion de eliminacion.
- No se agrego coautoria en commits ni documentacion.

## Conclusiones

El proyecto cumple con los objetivos del taller de pruebas de aceptacion. Las funcionalidades principales del inventario estan implementadas y cubiertas por escenarios BDD ejecutables. La integracion entre Gherkin, Behave y Python funciona correctamente, y el resultado final muestra una suite de pruebas estable con todos los escenarios aprobados.

## Recomendaciones

- Mantener cada feature en archivos separados si el proyecto crece.
- Agregar pruebas negativas para cantidades invalidas y productos duplicados.
- Estandarizar el idioma de los escenarios para evitar mezclar pasos en ingles y espanol.
- Usar mensajes de consola consistentes entre la aplicacion y los escenarios de prueba.
- Ejecutar `behave` antes de cada entrega o pull request.

## Referencias

- Behave Documentation: https://behave.readthedocs.io/
- Gherkin Reference: https://cucumber.io/docs/gherkin/
- Python Documentation: https://docs.python.org/3/
- Repositorio del proyecto: https://github.com/Jonthz/T6-AcepptanceTesting
