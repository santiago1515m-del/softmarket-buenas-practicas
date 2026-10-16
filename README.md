# SoftMarket: propuesta de buenas prácticas

Repositorio académico para acompañar el informe de refactorización de SoftMarket. Contiene una implementación sencilla del registro de clientes, una prueba unitaria de ejemplo y el informe en PDF y formato editable.

## Estructura

- `docs/Informe_SoftMarket.pdf`: informe final.
- `docs/Informe_SoftMarket_editable.docx`: editable en Word o importable en Google Docs.
- `docs/flujo-git.md`: pasos del flujo de ramas y revisión.
- `src/clientes/registro.py`: ejemplo SOLID de gestión de clientes.
- `tests/test_registro.py`: ejemplo de prueba unitaria.

## Ejecutar el ejemplo

Requiere Python 3.10 o posterior. Desde la raíz del repositorio:

```bash
python -m unittest discover -s tests -v
```

## Flujo ilustrado

`main` es la rama estable. La funcionalidad se trabaja en `feature/1-gestion-clientes`, se revisa mediante pull request y se integra a `main`. La rama `fix/2-guia-revision` muestra un cambio correctivo separado.

Este repositorio local es una simulación académica. Para publicarlo, crea un repositorio vacío en GitHub y sigue las instrucciones de `docs/flujo-git.md`.
