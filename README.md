# Choose Your Story

Proyecto **Choose Your Story**: una aventura narrativa interactiva donde el jugador toma decisiones que afectan al desarrollo de la historia.

## 📖 Descripción

Choose Your Story es un juego de aventura conversacional desarrollado en Python y respaldado por una base de datos MySQL. El usuario puede:

* Crear o iniciar sesión con un usuario
* Elegir un personaje y una aventura
* Tomar decisiones a lo largo de la historia
* Finalizar la aventura según sus elecciones
* Consultar estadísticas e informes
* Reproducir partidas ya jugadas (replay)

El proyecto forma parte de un trabajo académico modular (M01–M05), integrando programación, bases de datos, sistemas, lenguajes de marcas y control de versiones.

## 🛠️ Tecnologías utilizadas

* **Python 3**
* **MySQL**
* **PyMySQL** (conector Python–MySQL)
* **Node.js** (para la parte web)
* **HTML5 / CSS3**
* **Git & GitHub**

## 📂 Estructura del proyecto

```text
/
├── M2/            # Base de datos (scripts SQL, diagrama)
├── M3/            # Programación (juego en Python)
├── M4/            # Lenguaje de marcas (web)
├── README.md
```

## ⚙️ Requisitos previos

Antes de ejecutar el proyecto asegúrate de tener instalado:

* Python 3.9 o superior

### 📦 Dependencias Python

Es **obligatorio** instalar **PyMySQL** para que el proyecto funcione correctamente con la base de datos:

```bash
pip install pymysql
```

Opcionalmente, puedes usar un entorno virtual:

```bash
python -m venv venv
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate     # Windows
pip install pymysql
```

## 🗄️ Base de datos

1. Crear la base de datos en MySQL.
2. Ejecutar los scripts en el siguiente orden (ubicados en `M2/`):

* `create_db.sql`
* `alter_tables.sql`
* `insert_data.sql`

Estos scripts crean la estructura, relaciones y datos.

## ▶️ Ejecución del juego

Desde la carpeta `M3/`:

```bash
python main.py
```

El juego se ejecuta en consola y muestra menús interactivos para jugar, consultar informes o reproducir partidas.

## 📊 Funcionalidades principales

* Login y creación de usuarios
* Selección de personaje y aventura
* Sistema de decisiones por pasos
* Guardado de partidas y elecciones
* Informes estadísticos desde la BBDD
* Replay de aventuras jugadas

## 🌐 Página web

Puedes acceder a la pagina web del proyecto en el siguiente enlace:

[https://aleixgls.github.io/Projecte1-2026-MP03/](https://aleixgls.github.io/Projecte1-2026-MP03/)

---

## 👥 Autores

Proyecto desarrollado por estudiantes como parte de un trabajo académico.

*Aleix Linares Sousa*

*Marc Pino Reina*

## 📄 Licencia

Este proyecto se distribuye con fines educativos. Uso libre para aprendizaje y mejora personal.