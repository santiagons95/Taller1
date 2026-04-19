import sys
from datetime import datetime

valor_cliente = {"Particular": 80000, "EPS": 5000, "Prepagada": 30000}
valor_atencion = {"Particular": {"Limpieza": 60000, "Calzas": 80000, "Extracción": 100000, "Diagnostico": 50000},
                   "EPS": {"Limpieza":0, "Calzas": 40000, "Extracción": 40000, "Diagnostico": 0},
                   "Prepagada": {"Limpieza": 0, "Calzas": 10000, "Extracción": 10000, "Diagnostico": 0}}
lista_clientes = []

def ingresar_info_cliente():
    while True:
        try:
            cedula = int(input("Ingrese el número de cédula del cliente:").strip())
            if cedula <= 0:
                print("La cédula debe ser un número positivo y no puede estar vacía. Intente nuevamente.")
                continue
            else:
                break
        except ValueError:
            print("Entrada no válida. Por favor ingrese un número de cédula válido.")
            continue
                
    while True:
        nombre = str(input("Ingrese el nombre del cliente:").strip())
        if not nombre:
            print("El nombre no puede estar vacío. Intente nuevamente.")
            continue
        elif not nombre.replace(" ", "").isalpha():
            print("El nombre solo puede contener letras y espacios. Intente nuevamente.")
            continue
        else:
            break

    while True:
        telefono = input("Ingrese el número de teléfono del cliente:").strip()
        if not telefono:
            print("El número de teléfono no puede estar vacío. Intente nuevamente.")
            continue
        elif not telefono.isdigit():
            print("El número de teléfono solo puede contener dígitos. Intente nuevamente.")
            continue
        else:    
            break

    while True:
        tipo_raw = input("Ingrese el tipo de cliente (Particular, EPS, Prepagada): ").strip()
        match = next((k for k in valor_cliente if k.lower() == tipo_raw.lower()), None)
        if match is None:
            print("Tipo de cliente no válido. Intente nuevamente.")
            continue
        else:
            tipo_cliente = match
            break
            
    while True:
        tipo_raw = input("Ingrese el tipo de atención (Limpieza, Calzas, Extracción, Diagnostico): ").strip()
        match = next((k for k in valor_atencion[tipo_cliente] if k.lower() == tipo_raw.lower()), None)
        if match is None:
            print("Tipo de atención no válido. Intente nuevamente.")
            continue
        else:
            tipo_atencion = match
            break
    if tipo_atencion in ("Limpieza", "Diagnostico"):
        cantidad = 1
    else:
        while True:
            try:
                cantidad = int(input("Ingrese la cantidad de " + tipo_atencion + ":").strip())
            except ValueError:
                print("Entrada no válida. Por favor ingrese un número entero.")
                continue
            else:
                if cantidad > 0:
                    break
                print("La cantidad debe ser mayor a cero. Intente nuevamente.")
                continue
    while True:
        tipo_raw = input("Ingrese el tipo de prioridad (Normal, Urgente): ").strip()
        match = next((k for k in ["Normal", "Urgente"] if k.lower() == tipo_raw.lower()), None)
        if match is None:
            print("Tipo de prioridad no válido. Intente nuevamente.")
            continue
        else:
            tipo_prioridad = match
            break
    while True:
        fecha_atencion = input("ingrese la fecha de atención (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(fecha_atencion, "%Y-%m-%d")
            break
        except ValueError:
            print("Formato de fecha no válido. Por favor ingrese la fecha en el formato YYYY-MM-DD, ejemplo: 2024-06-15. Intente nuevamente.")
            continue
    costo_atencion = valor_cliente[tipo_cliente] + valor_atencion[tipo_cliente][tipo_atencion] * cantidad

    cliente_info = {
    "Cédula": cedula,
    "Nombre": nombre,
    "Teléfono": telefono,
    "Tipo Cliente": tipo_cliente,
    "Tipo Atención": tipo_atencion,
    "Costo Atención": costo_atencion,
    "Prioridad": tipo_prioridad,
    "Fecha Atención": fecha_atencion,
    "Cantidad": cantidad
    }

    lista_clientes.append(cliente_info)
    print(f"\n✔ Cliente registrado exitosamente: {cliente_info}\n")

def agregar_cliente():
    while True:
        respuesta = input("¿Desea ingresar la información de un cliente? (si/no): ").strip().lower()
        if respuesta not in ['si', 'no']:
            print("Respuesta no válida. Por favor ingrese 'si' o 'no'.")
            continue
        if respuesta == 'no':
            print("No se ingresarán más clientes.\n")
            break
        ingresar_info_cliente()

def mostrar_estadisticas():                    
    total_clientes = len(lista_clientes)
    ingresos_totales = sum(cliente["Costo Atención"] for cliente in lista_clientes)
    clientes_por_extraccion = len([cliente for cliente in lista_clientes if cliente["Tipo Atención"] == "Extracción"])
    print("=" * 45)
    print("           ESTADÍSTICAS GENERALES")
    print("=" * 45)
    print(f"  Total de clientes registrados : {total_clientes}")
    print(f"  Ingresos totales              : ${ingresos_totales:,}")
    print(f"  Clientes con Extracciones     : {clientes_por_extraccion}")
    print("=" * 45 + "\n")

def mostrar_clientes_ordenados():
    lista_clientes.sort(key=lambda x: x["Costo Atención"], reverse=True)
    print("Clientes ordenados por costo de atención (de mayor a menor):")
    for cliente in lista_clientes:
            print(f"  - {cliente['Nombre']} (CC {cliente['Cédula']}): ${cliente['Costo Atención']:,}")
    print()

def buscar_cliente():
    while True:
        busqueda = input("Ingrese el número de cédula del cliente que desea buscar (o escriba 'salir' para terminar): ").strip()
        if busqueda.lower() == 'salir':
            print("Saliendo del programa.")
            break   
        try:
            cedula_buscar= int(busqueda)
        except ValueError:
            print("Entrada no válida. Por favor ingrese un número de cédula válido.")
            continue
        cliente_encontrado = next((cliente for cliente in lista_clientes if cliente["Cédula"] == cedula_buscar), None)
        if cliente_encontrado:
            print(f"Información del cliente encontrado: {cliente_encontrado}\n")
        else:
            print("Cliente no encontrado. Intente nuevamente.\n")
            
def main():
    agregar_cliente()
    if lista_clientes:
        mostrar_estadisticas()
        mostrar_clientes_ordenados()
        buscar_cliente()
    else:
        print("No se registraron clientes. No se mostrarán estadísticas ni se realizará búsqueda. Fin del programa.")
if __name__ == "__main__":
    main()