# Sistema de Gestión de Vacaciones - Chatbot por Consola

## Descripción

Este proyecto simula un chatbot administrativo para gestionar vacaciones de empleados dentro de una organización.

El sistema permite consultar días disponibles, agregar empleados, mostrar empleados cargados y solicitar licencias por vacaciones. La lógica representa un proceso administrativo de Recursos Humanos automatizado mediante Python.

## Objetivo del proyecto

Automatizar el proceso de gestión de vacaciones utilizando un chatbot funcional por consola, aplicando reglas de negocio, validaciones, persistencia de datos y manejo del camino infeliz.

## Tecnologías utilizadas

- Python 3
- Archivo CSV como base de datos persistente
- Consola / terminal
- BPMN 2.0 para modelado del proceso

## Estructura del proyecto

```text
Proyecto Chatbot Gestión de vacaciones/
│
├── Chatbot gestión de vacaciones.py
├── empleados_vacaciones.csv
├── README.md
└── Diagramas BPMN 2.0/
    ├── BPMN_01_AS_IS_Gestion_Manual.png
    ├── BPMN_02_TO_BE_Chatbot_CSV.png
    ├── BPMN_03_Consultar_Dias_CSV.png
    ├── BPMN_04_Solicitar_Vacaciones_CSV.png
```

## Persistencia de datos

La persistencia se realiza mediante el archivo:

```text
empleados_vacaciones.csv
```

El archivo contiene dos columnas:

```text
nombre,dias_disponibles
```

Cada vez que se agrega un empleado o se aprueba una solicitud de vacaciones, el sistema actualiza el archivo CSV para conservar los cambios.

## Base de respaldo

El programa incluye una base de datos de respaldo dentro del código:

```python
EMPLEADOS_RESPALDO = {...}
```

Esta base se utiliza solamente si el archivo CSV no existe. En ese caso, el sistema crea automáticamente el archivo `empleados_vacaciones.csv` con los datos iniciales.

## Funcionalidades

1. Agregar un nuevo empleado.
2. Mostrar empleados cargados.
3. Consultar días disponibles.
4. Solicitar licencia por vacaciones.
5. Salir del sistema.

## Validaciones

El sistema controla los siguientes errores:

- Nombre vacío.
- Nombre con números o caracteres inválidos.
- Empleado inexistente.
- Empleado duplicado.
- Días ingresados con texto.
- Días menores o iguales a cero.
- Solicitud de vacaciones superior al saldo disponible.
- Opción de menú inválida.

## Ejecución del programa

1. Descargar o clonar el repositorio.
2. Verificar que Python 3 esté instalado.
3. Abrir una terminal en la carpeta del proyecto.
4. Ejecutar:

```bash
python Chatbot Gestión de Vacaciones.py
```

## Repositorio

Agregar aquí el enlace al repositorio público de GitHub:

```text
[PEGAR LINK DEL REPOSITORIO AQUÍ]
```

## Autor

CORNAGLIA Pablo
