# StayKeeper API

## 🏨 Descripción

StayKeeper API es un **gestor de reservas de hotel** desarrollado con **Django REST Framework**.
Permite administrar clientes y sus reservas mediante **endpoints REST**, con funcionalidades de CRUD, búsqueda y relación entre entidades.

**Desarrollado por:** Yamile Ochoa Marín – Tecsup  
**Video de validación:** [YouTube](https://youtu.be/Os6Y2DB7ZKM)

---

## 💻 Tecnologías usadas

* Python 3.13
* Django 5.2.7
* Django REST Framework
* drf-spectacular (Swagger UI)
* SQLite (base de datos por defecto)

---

## ⚙️ Instrucciones para ejecutar el servidor

1. Clonar el repositorio:

```bash
git clone https://github.com/YamileOchoa/django-reservas-api.git
cd staykeeper_api
```

2. Crear entorno virtual y activar:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. Instalar dependencias:

```bash
pip install -r requirements.txt
```

4. Ejecutar migraciones:

```bash
python manage.py migrate
```

5. Ejecutar el servidor:

```bash
python manage.py runserver
```

6. Acceder a **Swagger UI** para probar los endpoints:

```
http://127.0.0.1:8000/api/docs/
```

---

## 📂 Endpoints disponibles

### Clientes

| Método | URL                   | Descripción               |
| ------ | --------------------- | ------------------------- |
| GET    | `/api/clientes/`      | Listar todos los clientes |
| POST   | `/api/clientes/`      | Crear un cliente          |
| GET    | `/api/clientes/{id}/` | Obtener un cliente por ID |
| PUT    | `/api/clientes/{id}/` | Actualizar un cliente     |
| PATCH  | `/api/clientes/{id}/` | Actualización parcial     |
| DELETE | `/api/clientes/{id}/` | Eliminar un cliente       |

**Ejemplo POST cliente:**

```json
POST /api/clientes/
{
  "nombre": "Carlos Pérez",
  "documento": "87654321"
}
```

### Reservas

| Método | URL                   | Descripción                |
| ------ | --------------------- | -------------------------- |
| GET    | `/api/reservas/`      | Listar todas las reservas  |
| POST   | `/api/reservas/`      | Crear una reserva          |
| GET    | `/api/reservas/{id}/` | Obtener una reserva por ID |
| PUT    | `/api/reservas/{id}/` | Actualizar una reserva     |
| PATCH  | `/api/reservas/{id}/` | Actualización parcial      |
| DELETE | `/api/reservas/{id}/` | Eliminar una reserva       |

**Ejemplo POST reserva:**

```json
POST /api/reservas/
{
  "fecha_ingreso": "2025-11-01",
  "fecha_salida": "2025-11-05",
  "numero_habitacion": "202",
  "cliente": 1
}
```

**Campos personalizados en reservas:**

* `cliente_nombre`: nombre del cliente asociado
* `cliente_documento`: documento del cliente asociado

### Búsqueda (Search Filter)

* Filtrar clientes por nombre o documento:

```
GET /api/clientes/?search=Carlos
```

* Filtrar reservas por número de habitación o nombre de cliente:

```
GET /api/reservas/?search=202
```

---

## 🎨 Documentación

La API está documentada con **Swagger UI**:

```
http://127.0.0.1:8000/api/docs/
```

---

## 🎥 Validación

El proyecto se valida mediante video mostrando:

* Creación, listado, edición, eliminación y búsqueda de clientes y reservas.
* La relación entre reservas y clientes (`cliente_nombre`, `cliente_documento`).
