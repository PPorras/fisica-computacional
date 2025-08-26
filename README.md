# fisica-computacional
Este repositorio contiene todo el material del curso de Física Computacional, incluyendo apuntes, códigos, ejemplos y recursos complementarios.

## Estructura del Repositorio
- **`main`**: Rama principal con versiones estables y probadas (solo lectura para estudiantes)
- **`numeric-dev`**: Rama de desarrollo activo con el material del curso
- **Ramas personales**: Cada estudiante trabaja en su propia rama

##  Para Estudiantes

### Configuración Inicial
```bash
# Clonar el repositorio
git clone <repo-url>
cd fisica-computacional

# Configurar rama de desarrollo y crear rama personal
git checkout numeric-dev
git checkout -b PPorras-numeric-dev 
## El nombre de la rama debe ser primera inicial del nombre seguido del apellido seguido de numeric-dev

### Flujo de Trabajo Diario 
#### Al empezar a trabajar:
```bash
# Actualizar con los últimos cambios del profesor
git checkout numeric-dev
git pull origin numeric-dev
git checkout mi-rama-desarrollo

#### Durante el trabajo:
# Trabajar en ejercicios y prácticas
# Guardar cambios frecuentemente
```bash
git add .
git commit -m "Descripción clara de los cambios realizados"

#### Al terminar:
# Subir trabajo al repositorio (solo tu rama personal)
```bash
git push origin mi-rama-desarrollo
