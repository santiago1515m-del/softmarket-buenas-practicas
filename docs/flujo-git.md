# Flujo de Git propuesto

1. Abrir una tarea en GitHub Issues.
2. Actualizar `main` y crear una rama breve: `git switch -c feature/1-gestion-clientes`.
3. Hacer un cambio pequeño, guardar el trabajo y subir la rama.
4. Abrir un pull request hacia `main`, explicar el cambio y pedir una revisión.
5. Revisar el código y las verificaciones automáticas; corregir lo que falle.
6. Integrar con **Squash and merge** y borrar la rama cuando se apruebe.
7. Para publicar, crear una etiqueta de versión y desplegar después de verificar el cambio.

## Publicar este repositorio en GitHub

Primero crea en GitHub un repositorio vacío llamado `softmarket-buenas-practicas`. Desde la carpeta local del proyecto, usa:

```bash
git remote add origin https://github.com/TU_USUARIO/softmarket-buenas-practicas.git
git push -u origin main
git push -u origin feature/1-gestion-clientes
git push -u origin fix/2-guia-revision
```

Reemplaza `TU_USUARIO` por tu usuario. En GitHub, abre un pull request desde `feature/1-gestion-clientes` hacia `main` para mostrar la revisión.

La revisión debe ser realizada por otra persona; el autor de la propuesta no aprueba su propio cambio.
