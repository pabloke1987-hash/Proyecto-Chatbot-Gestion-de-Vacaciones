# ============================================================
# SISTEMA DE GESTIÓN DE VACACIONES - CHATBOT POR CONSOLA
# VERSIÓN CORREGIDA CON PERSISTENCIA EN CSV
# ============================================================
# Corrección importante:
# El archivo CSV se busca y se modifica en la MISMA CARPETA donde
# está guardado este archivo .py.
#
# De esta forma, el programa no depende de desde qué carpeta se
# ejecute la terminal.
# ============================================================

import csv
import os


# ============================================================
# RUTA DEL ARCHIVO CSV
# ============================================================
# os.path.dirname(__file__) obtiene la carpeta donde está este .py.
# Así evitamos que Python cree o modifique otro CSV en otra ubicación.
# ============================================================

CARPETA_PROGRAMA = os.path.dirname(os.path.abspath(__file__))
ARCHIVO_CSV = os.path.join(CARPETA_PROGRAMA, "empleados_vacaciones.csv")


# ============================================================
# BASE DE DATOS DE RESPALDO
# ============================================================
# Se usa solamente si el archivo CSV no existe.
# ============================================================

EMPLEADOS_RESPALDO = {
    "juan perez": 10,
    "ana gomez": 5,
    "luis lopez": 8,
    "maria diaz": 12,
    "carlos ruiz": 7,
    "sofia martinez": 9,
    "diego fernandez": 6,
    "lucia gonzalez": 11,
    "pablo sosa": 4,
    "camila romero": 10,
    "martin diaz": 8,
    "julieta alvarez": 7,
    "nicolas pereyra": 9,
    "valentina ramos": 6,
    "franco castro": 5,
    "agustina silva": 12,
    "leandro torres": 10,
    "micaela luna": 8,
    "federico vera": 6,
    "carla nuñez": 7
}


# ============================================================
# FUNCIONES DE VALIDACIÓN
# ============================================================

def normalizar(texto):
    return texto.strip().lower()


def nombre_valido(nombre):
    nombre = nombre.strip()

    if len(nombre) == 0:
        return False

    if not any(c.isalpha() for c in nombre):
        return False

    for c in nombre:
        if not (c.isalpha() or c.isspace()):
            return False

    return True


def dias_validos(dias):
    if not dias.isdigit():
        return False

    if int(dias) <= 0:
        return False

    return True


# ============================================================
# FUNCIONES PARA CSV
# ============================================================

def crear_csv_desde_respaldo():
    """Crea el CSV con los empleados iniciales si el archivo no existe."""
    try:
        with open(ARCHIVO_CSV, "w", newline="", encoding="utf-8-sig") as archivo:
            escritor = csv.writer(archivo, delimiter=";")
            escritor.writerow(["nombre", "dias_disponibles"])

            for nombre, saldo in EMPLEADOS_RESPALDO.items():
                escritor.writerow([nombre, saldo])

    except PermissionError:
        print("\n🤖 ❌ No se pudo crear el archivo CSV.")
        print("🤖 Cerrá el archivo si está abierto en Excel e intentá nuevamente.")


def cargar_empleados():
    """Lee el CSV y devuelve un diccionario con los empleados."""
    if not os.path.exists(ARCHIVO_CSV):
        crear_csv_desde_respaldo()

    empleados = {}

    try:
        with open(ARCHIVO_CSV, "r", newline="", encoding="utf-8-sig") as archivo:
            lector = csv.DictReader(archivo, delimiter=";")

            for fila in lector:
                nombre = normalizar(fila["nombre"])
                saldo = int(fila["dias_disponibles"])
                empleados[nombre] = saldo

    except FileNotFoundError:
        print("\n🤖 ❌ No se encontró el archivo CSV.")
        print("🤖 Se creará nuevamente con la base de respaldo.")
        crear_csv_desde_respaldo()
        return cargar_empleados()

    except PermissionError:
        print("\n🤖 ❌ No se puede leer el archivo CSV.")
        print("🤖 Cerrá el archivo si está abierto en Excel e intentá nuevamente.")

    except (ValueError, KeyError):
        print("\n🤖 ❌ El archivo CSV tiene datos incorrectos.")
        print("🤖 Verificá que tenga las columnas: nombre;dias_disponibles")

    return empleados


def guardar_empleados(empleados):
    """Guarda el diccionario actualizado dentro del CSV."""
    try:
        with open(ARCHIVO_CSV, "w", newline="", encoding="utf-8-sig") as archivo:
            escritor = csv.writer(archivo, delimiter=";")
            escritor.writerow(["nombre", "dias_disponibles"])

            for nombre, saldo in empleados.items():
                escritor.writerow([nombre, saldo])

        return True

    except PermissionError:
        print("\n🤖 ❌ No se pudo modificar el archivo CSV.")
        print("🤖 Cerrá el archivo si está abierto en Excel e intentá nuevamente.")
        return False


# ============================================================
# FUNCIONES DEL SISTEMA
# ============================================================

def agregar_empleado():
    empleados = cargar_empleados()

    print("\n🤖 Seleccionaste la opción para cargar un empleado al sistema de gestión de vacaciones.")
    print("🤖 Por favor, necesitamos que nos digas algunos datos importantes para agregarlo de manera correcta.\n")

    nombre = input("👤 Ingresá el nombre y apellido del empleado que necesitás agregar al sistema: ")

    if not nombre_valido(nombre):
        print("\n🤖 ❌ El nombre de empleado que ingresaste no está permitido.")
        print("🤖 Por favor, ingresá solo letras y espacios.")
        return

    nombre = normalizar(nombre)

    if nombre in empleados:
        print("\n🤖 ⚠️  El nombre del empleado que necesitás agregar ya existe.")
        print("🤖 Por favor, verificá la lista de empleados agregados al sistema o intentá nuevamente con otro nombre.")
        return

    saldo = input("👤 Ingrese la cantidad de días de vacaciones disponibles que tiene el empleado: ")

    if not dias_validos(saldo):
        print("\n🤖 ❌ Error en la carga de los días de vacaciones.")
        print("🤖 Por favor ingresá una cantidad en números mayor que cero.")
        return

    empleados[nombre] = int(saldo)

    if guardar_empleados(empleados):
        print("\n🤖 ✅ Información del empleado cargada correctamente en el sistema.")
        print("🤖 💾 Los datos fueron guardados en el archivo CSV.")


def mostrar_empleados():
    empleados = cargar_empleados()

    print("\n🤖 📋 LISTA DE EMPLEADOS AGREGADOS AL SISTEMA DE GESTIÓN DE VACACIONES\n")

    if len(empleados) == 0:
        print("🤖 No hay empleados cargados en el sistema.")
        return

    for nombre, saldo in empleados.items():
        print(f"👤 {nombre.title()}  🗓️  {saldo} días de vacaciones disponibles")


def consultar_saldo():
    empleados = cargar_empleados()

    print("\n🤖 🔎 Seleccionaste la opción para consultar las vacaciones disponibles que tiene un empleado.")
    print("🤖 Por favor, necesitamos que nos digas algunos datos importantes para buscarlo en el sistema.\n")

    nombre = input("👤 Ingrese el nombre y apellido del empleado: ")

    if not nombre_valido(nombre):
        print("\n🤖 ❌ El nombre de empleado que ingresaste no está permitido.")
        print("🤖 Por favor, ingresá solo letras y espacios.")
        return

    nombre = normalizar(nombre)

    if nombre not in empleados:
        print("\n🤖 ❌ Empleado no encontrado.")
        print("🤖 Por favor, verificá la lista de empleados agregados al sistema.")
        print("🤖 Si no está en el sistema, podés agregarlo usando la opción 1 del menú principal.")
        return

    print(f"\n🤖 📊 Días de vacaciones disponibles: {empleados[nombre]}")


def solicitar_vacaciones():
    empleados = cargar_empleados()

    print("\n🤖 🗓️  Seleccionaste la opción para solicitar una licencia por vacaciones.")
    print("🤖 Por favor, necesitamos que nos digas algunos datos importantes para buscar en el sistema los días de vacaciones que tenés disponibles.\n")

    nombre = input("👤 Ingrese nombre y apellido del empleado que desea tomarse vacaciones: ")

    if not nombre_valido(nombre):
        print("\n🤖 ❌ El nombre de empleado que ingresaste no está permitido.")
        print("🤖 Por favor, ingresá solo letras y espacios.")
        return

    nombre = normalizar(nombre)

    if nombre not in empleados:
        print("\n🤖 ❌ Empleado no encontrado.")
        print("🤖 Por favor, verificá la lista de empleados agregados al sistema.")
        print("🤖 Si no está en el sistema, podés agregarlo usando la opción 1 del menú principal.")
        return

    print(f"\n🤖 📊 Días disponibles de vacaciones: {empleados[nombre]}\n")

    dias = input("👤 Ingresá la cantidad de días de vacaciones que necesitás pedir: ")

    if not dias_validos(dias):
        print("\n🤖 ❌ Error en la carga de los días de vacaciones.")
        print("🤖 Por favor ingresá una cantidad en números mayor que cero.")
        return

    dias = int(dias)

    if dias <= empleados[nombre]:
        empleados[nombre] -= dias

        if guardar_empleados(empleados):
            print("\n🤖 ✅ Tu solicitud de vacaciones fue APROBADA.")
            print(f"🤖 📉 Días de vacaciones restantes: {empleados[nombre]} días")
            print("🤖 💾 El nuevo saldo fue guardado en el archivo CSV.")

    else:
        print("\n🤖 ❌ Tu solicitud de vacaciones fue RECHAZADA.")
        print("🤖 No contás con la cantidad de días disponibles que pediste.")
        print("🤖 Por favor, volvé a solicitar tus vacaciones ingresando otra cantidad de días.")


# ============================================================
# MENÚ PRINCIPAL
# ============================================================

def menu():
    while True:
        print("\n=================================================")
        print("   SISTEMA DE GESTIÓN DE VACACIONES - CHATBOT")
        print("=================================================\n")

        print("🤖 Bienvenido al sistema de gestión de vacaciones.")
        print("🤖 ¿Qué necesitás hacer?")
        print("🤖 Por favor, elegí una de las opciones del menú principal.\n")

        print("1️⃣   🧾 Agregar un nuevo empleado a la base de datos del sistema")
        print("2️⃣   📋 Mostrar lista de empleados cargados en la base de datos")
        print("3️⃣   🔎 Consultar días de vacaciones disponibles que tiene un empleado")
        print("4️⃣   🗓️  Solicitar licencia por vacaciones")
        print("5️⃣   🚪 Salir del sistema")

        opcion = input("\n👤 Seleccioná una opción: ")

        if opcion == "1":
            agregar_empleado()

        elif opcion == "2":
            print("\n🤖 Cargando lista de empleados, aguardá un momento por favor...")
            mostrar_empleados()

        elif opcion == "3":
            consultar_saldo()

        elif opcion == "4":
            solicitar_vacaciones()

        elif opcion == "5":
            print("\n🤖 👋 Gracias por usar el sistema de gestión de vacaciones. ¡Hasta luego!\n")
            break

        else:
            print("\n🤖 ⚠️  La opción que elegiste no está permitida.")
            print("🤖 Por favor ingresá una de las opciones disponibles del menú principal.")


# ============================================================
# EJECUCIÓN DEL PROGRAMA
# ============================================================

menu()
