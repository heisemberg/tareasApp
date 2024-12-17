# Gestión de Tareas

Una aplicación de escritorio para gestionar tareas, desarrollada con Python y Tkinter. Permite agregar, editar, eliminar, completar, importar y exportar tareas en formato JSON.

## Características

- **Agregar Tareas**: Añade nuevas tareas con un título y una descripción.
- **Editar Tareas**: Modifica el título y la descripción de las tareas existentes.
- **Eliminar Tareas**: Elimina tareas que han sido marcadas como completadas.
- **Completar Tareas**: Marca las tareas como completadas o no completadas.
- **Importar Tareas**: Importa tareas desde un archivo JSON.
- **Exportar Tareas**: Exporta tareas a un archivo JSON.
- **Interfaz Desplazable**: La lista de tareas es desplazable para manejar un gran número de tareas.

## Requisitos

- Python 3.x
- Tkinter (incluido con Python)
- SQLite3 (incluido con Python)

## Instalación

1. Clona este repositorio o descarga los archivos.
2. Navega al directorio del proyecto.

    ```sh
    git clone https://github.com/tu_usuario/gestion-tareas.git
    cd gestion-tareas
    ```

3. Instala las dependencias necesarias (si las hubiera).

    ```sh
    pip install -r requirements.txt
    ```

## Uso

### Ejecutar desde el código fuente

1. Ejecuta el script `gestionTareas.py`.

    ```sh
    python gestionTareas.py
    ```

2. Usa la interfaz gráfica para agregar, editar, eliminar, completar, importar y exportar tareas.

### Ejecutar el archivo ejecutable

1. Navega a la carpeta `dist` que se encuentra en el mismo directorio donde ejecutaste `PyInstaller`.
2. Dentro de la carpeta `dist`, encontrarás el archivo `gestionTareas.exe`.
3. Haz doble clic en `gestionTareas.exe` para ejecutar la aplicación.

## Estructura del Proyecto

- `gestionTareas.py`: El script principal que contiene la lógica de la aplicación y la interfaz gráfica.
- `tareas.db`: La base de datos SQLite que almacena las tareas (se crea automáticamente al ejecutar el script).
- `dist/gestionTareas.exe`: El archivo ejecutable de la aplicación.
- `README.md`: Este archivo.

## Funcionalidades

### Agregar Tareas

1. Ingresa el título de la tarea en el campo "Titulo de la tarea".
2. Ingresa la descripción de la tarea en el campo "Descripcion de la tarea".
3. Haz clic en el botón "Agregar tarea".

### Editar Tareas

1. Haz clic en el botón "Modificar" junto a la tarea que deseas editar.
2. Modifica el título y/o la descripción en los campos correspondientes.
3. Haz clic en el botón "Actualizar tarea".

### Eliminar Tareas

1. Marca la tarea como completada haciendo clic en el checkbox junto a la tarea.
2. Haz clic en el botón "Eliminar" junto a la tarea.

### Completar Tareas

1. Haz clic en el checkbox junto a la tarea para marcarla como completada o no completada.

### Importar Tareas

1. Haz clic en el botón "Importar tareas".
2. Selecciona un archivo JSON que contenga las tareas a importar.

### Exportar Tareas

1. Haz clic en el botón "Exportar tareas".
2. Selecciona la ubicación y el nombre del archivo JSON donde se exportarán las tareas.

