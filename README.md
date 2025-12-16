# 🏋️‍♂️ SportsPro Inventory | Sistema de Gestión Deportivo

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.0-092E20?style=for-the-badge&logo=django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Status](https://img.shields.io/badge/Status-Finalizado-success?style=for-the-badge)

> **Evaluación Técnica Módulo 7:** Desarrollo de Aplicación Web con Django.

Plataforma integral para la administración de inventario enfocada en tiendas de deportes de alto rendimiento. Este proyecto implementa un sistema CRUD completo, gestión de multimedia y relaciones complejas de bases de datos, asegurando un código limpio y seguro.


---

## 🚀 Funcionalidades Clave

### 🛠️ Gestión de Datos (CRUD)
* **Crear:** Alta de productos con validación de formularios y carga de imágenes.
* **Leer:** Visualización en grilla (Cards) y vistas de detalle específicas.
* **Actualizar:** Edición de información existente y reemplazo de imágenes.
* **Eliminar:** Borrado seguro con página de confirmación "Zona de Peligro".

### 🔗 Relaciones de Base de Datos (ORM)
El sistema gestiona tres tipos de relaciones SQL a través del ORM de Django:
* **Uno a Muchos (1:N):** *Categoría (Disciplina)* -> *Productos*.
* **Muchos a Muchos (N:N):** *Productos* <-> *Etiquetas* (Ej: Oferta, Pro, Nuevo).
* **Uno a Uno (1:1):** *Producto* <-> *Detalles Técnicos* (Peso y Dimensiones).

### 🛡️ Seguridad y Buenas Prácticas
* **Variables de Entorno:** Uso de `python-dotenv` para ocultar la `SECRET_KEY` y configuración de `DEBUG`.
* **Protección CSRF:** Todos los formularios incluyen tokens de seguridad.
* **Manejo de Errores:** Uso de `get_object_or_404` para control de flujo.

---

## 💻 Stack Tecnológico

* **Backend:** Python 3, Django Framework.
* **Base de Datos:** SQLite3 (Configuración por defecto para desarrollo).
* **Frontend:** HTML5, CSS3, Bootstrap 5 (CDN), Jinja2 Templates.
* **Librerías Adicionales:**
    * `Pillow`: Procesamiento de imágenes.
    * `python-dotenv`: Gestión de seguridad.

---

## ⚙️ Guía de Instalación Local

Sigue estos pasos para desplegar el proyecto en tu máquina:

### 1. Clonar el repositorio
```bash
git clone [https://github.com/dg-nvrr/Evaluacion_M7](https://github.com/dg-nvrr/Evaluacion_M7)
cd Evaluacion_M7
