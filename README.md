Encuestas de Salud y Consumo de Alcohol
Este proyecto es una aplicación de escritorio desarrollada en Python con Tkinter para la interfaz gráfica y MySQL como base de datos relacional. La aplicación permite gestionar encuestas relacionadas con el consumo de alcohol y los indicadores de salud, realizar consultas avanzadas y visualizar resultados gráficamente.

Características Principales
1. Interfaz Gráfica de Usuario
Implementada con Tkinter, diseñada para ser intuitiva y profesional.
Elementos como menús, botones y campos de entrada para realizar operaciones CRUD, consultas y filtros.
Visualización clara de los datos.

2. Conexión a Base de Datos MySQL
Manejo completo de operaciones CRUD (Crear, Leer, Actualizar, Eliminar).
Integración con una base de datos proporcionada mediante un script SQL.

3. Consultas y Ordenación
Filtros avanzados y ordenación de registros según edad, sexo, consumo de alcohol, problemas de salud, etc.
Exportación de resultados a archivos Excel para análisis externo.

4. Visualización Gráfica
Gráficos dinámicos (barras, pastel, líneas) para representar los resultados de las consultas.
Personalización de gráficos según las necesidades del cliente.

Requisitos del Sistema
Python 3.10 o superior
Tkinter (preinstalado con Python)
MySQL Server 8.0 o superior
Biblioteca adicional:
pymysql (conector Python-MySQL)
matplotlib (para gráficos)
pandas (para exportar datos a Excel)

Instalación
Clonar el Repositorio
git clone https://github.com/tuusuario/encuestas-salud.git
cd encuestas-salud

Instalar Dependencias
pip install pymysql matplotlib pandas

Configurar la Base de Datos
Asegúrate de tener MySQL Server instalado y configurado.
Ejecuta el script ENCUESTAS.txt para crear la base de datos:
mysql -u tu_usuario -p < ENCUESTAS.txt
Configura las credenciales de acceso a MySQL en el archivo config.py.

Ejecución
Abre una terminal en la carpeta del proyecto.
Ejecuta la aplicación:
python main.py

Explora las funcionalidades:
Gestión de Encuestas: Añadir, visualizar, actualizar o eliminar registros.
Consultas Avanzadas: Ordenar y filtrar datos según diferentes criterios.
Exportación a Excel: Guardar los resultados para análisis externo.
Gráficos: Visualiza datos de manera gráfica con opciones de personalización.


Estructura del Proyecto
main.py: Archivo principal de la aplicación.
config.py: Configuración de conexión a MySQL.
models/: Módulos relacionados con la lógica CRUD y consultas.
views/: Código relacionado con la interfaz gráfica.
ENCUESTAS.txt: Script SQL para crear la base de datos.

Documentación Adicional
El proyecto está completamente documentado en el archivo PDF disponible en el repositorio, que incluye:
Descripción técnica y funcional.
Justificación de decisiones de diseño.
Ejemplos de consultas y gráficos.

Autor
Este proyecto fue desarrollado como parte de un hito académico. Para cualquier consulta o mejora, puedes contactar a través de GitHub.
