# SoftMarket: propuesta de buenas prácticas

Repositorio académico con el informe y un ejemplo de gestión de clientes. Incluye código fuente, pruebas y el flujo de trabajo propuesto.

## Contenido

- `docs/Informe_SoftMarket.pdf`: informe final.
- `docs/Informe_SoftMarket_editable.docx`: versión editable del informe.
- `docs/flujo-git.md`: pasos para trabajar con ramas y revisar cambios.
- `src/clientes/registro.py`: ejemplo de registro de clientes con principios SOLID.
- `tests/test_registro.py`: pruebas del registro.
- `.github/PULL_REQUEST_TEMPLATE.md`: plantilla para describir y revisar cambios.

## Ejecutar las pruebas

Requiere Python 3.10 o posterior. Desde la carpeta principal:

```bash
python -m unittest discover -s tests -v
```

## Ramas de ejemplo

- `main`: versión estable del proyecto.
- `feature/1-gestion-clientes`: trabajo de gestión de clientes.
- `fix/2-guia-revision`: corrección de la guía de revisión.

Repositorio público: [softmarket-buenas-practicas](https://github.com/santiago1515m-del/softmarket-buenas-practicas)
