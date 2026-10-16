# Flujo de Git propuesto

1. Abrir una tarea y acordar qué cambio se necesita.
2. Actualizar `main` y crear una rama para trabajar, por ejemplo: `git switch -c feature/1-gestion-clientes`.
3. Hacer un cambio pequeño, ejecutar las pruebas y guardarlo con un mensaje claro, como `feat(clientes): agregar registro` o `fix(clientes): validar correo`.
4. Subir la rama a GitHub con `git push -u origin feature/1-gestion-clientes`.
5. Abrir un pull request dirigido a `main`, explicar el cambio y pedir una revisión.
6. Otra persona revisa el cambio y confirma que las pruebas pasen. Si hay observaciones, corregirlas en la misma rama y solicitar otra revisión.
7. Si aparece un conflicto con `main`, actualizar la rama, resolver las diferencias y ejecutar otra vez las pruebas.
8. Integrar el cambio aprobado con **Squash and merge** y cerrar la rama.

## Ramas de ejemplo

- `main`: versión estable del proyecto.
- `feature/1-gestion-clientes`: trabajo de gestión de clientes.
- `fix/2-guia-revision`: corrección de la guía de revisión.

La revisión debe hacerla otra persona; quien propone el cambio no lo aprueba por su cuenta.

Repositorio: https://github.com/santiago1515m-del/softmarket-buenas-practicas
