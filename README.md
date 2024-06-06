## Guía de Ejecución del Proyecto

Este repositorio incluye un proyecto sencillo para demostrar los conceptos de pruebas unitarias, pruebas de servicio o de API y pruebas E2E o de GUI. El objetivo es que el alumno entienda estos conceptos, por lo que el código y la estructura del proyecto son especialmente sencillos.

### Prerrequisitos
- Docker instalado en tu sistema operativo.
- Conexión a Internet para descargar las imágenes necesarias.

### Pasos para Ejecutar el Proyecto

1. **Clonar el Repositorio**

- git clone https://github.com/martincuevast/unir-test.git
   
2. **Navegar al Directorio del Proyecto**

- cd /unir-test
   
3. **Construir la Imagen de Docker**
   
- make build

4. **Ejecutar la Aplicación**

- make run
   
5. **Realizar Pruebas Unitarias**

- make test-unit
   
6. **Realizar Pruebas de Servicio o API**

- make test-api
   
7. **Realizar Pruebas E2E o de GUI**

- make test-e2e
   
8. **Detener la Aplicación**

- make stop-web
   
9. **Limpiar los Recursos**

- make clean
