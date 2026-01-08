# Task Manager API

API para la gestión de tareas y categorías usando **Django 5 + Django REST Framework**.

Permite:

-   Crear y listar tareas filtradas por estado (`pending` o `done`).
-   Crear y listar categorías.
-   Marcar tareas como completadas.
-   Eliminar tareas (soft delete).
-   Paginación de tareas (6 por página).
-   Control de acceso por usuario autenticado.

---

## Requisitos

-   Python 3.11
-   pip
-   virtualenv (opcional, recomendado)
-   Git

---

## Instalación

1. **Clonar el repositorio**

````bash
git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio

## Init

2. **Creación de entorno virtual**

```bash

python -m venv venv
# Windows
venv\Scripts\activate
# Linux / Mac
source venv/bin/activate

pip install -r requirements.txt

3. **Configurar variables de entorno**

```bash

cp .env.example .env

4. **Migrar la base de datos**

```bash

python manage.py migrate

5. **Crear un usuario administrador**

```bash

python manage.py createsuperuser

6. **Ejecutar el servidor**

```bash

python manage.py runserver


## Autenticación

Todos los endpoints requieren usuario autenticado.

Se puede usar token del usuario para pruebas con Postman o cualquier HTTP client.


## Tests

```bash

pytest


````
