# Diccionario donde se almacenan los datos de la factura
factura = {"numero": "23", "proveedor": "aseos", "fecha": "23-10-2026", "total": 2000}

print(f"Numero de factura: {factura ['numero']}")
print(f"proveedor de factura: {factura ['proveedor']}")
print(f"fecha de factura: {factura ['fecha']}")
print(f"total de factura: {factura ['total']}")
# # imprimir individualmente cada dato

# # cambiar el valor de la clave: proveedor
factura["proveedor"] = "Vimash"
print(factura["proveedor"])
# # llamar una clave llamada moneda
factura["moneda"] = "COP"
print(factura)
# situacion cuando una clave no existe
"""print(factura["descuento"]) 
envia error porque la clave no esta determinada en el diccionario"""
print(factura.get("NIT", "No hay NIT registrado"))

factura["total"] = 5000
print(factura["total"])

facturas = [
    {"numero": "10", "proveedor": "QuimiEscencias", "total": "60000"},
    {"numero": "11", "proveedor": "Fuller", "total": "100000"},
    {"numero": "12", "proveedor": "colplast", "total": "30000"},
]

total_facturas = 0

print("--- REPORTE DE FACTURAS ---")
for factura in facturas:
    total_facturas += int(factura["total"])
    print(f"Numero: {factura['numero']} | Proveedor: {factura['proveedor']}")

# Mostramos el total fuera del bucle
print(f"\nTotal general de todas las facturas: {total_facturas}")

# Calcular el promedio (Total dividido entre la cantidad de facturas)
total_medio = total_facturas / len(facturas)
print(f"Total medio (promedio): {total_medio}")

# Encontrar la factura con el importe más alto
factura_mayor = max(facturas, key=lambda f: int(f["total"]))
print(f"La factura mas alta es del proveedor {factura_mayor['proveedor']} por un valor de {factura_mayor['total']}")

# Comprobar que existan las claves obligatorias: Que la factura tenga número, proveedor, fecha y total.
if "numero" not in factura or "proveedor" not in factura or "fecha" not in factura or "total" not in factura:
    print("Error: Faltan datos en factura")
else:
    print("Claves presentes")
# Detectar proveedores vacíos: Si un proveedor es un texto vacío (""), el programa debe detectarlo como un error.
if factura["proveedor"]== "":
    print("Error el proveedor esta vacio")
else:
    print("Proveedor valido")
# Rechazar importes negativos: Una factura no puede costar -5000.
if int(factura['total'])<0:
    print("Error el total no puede ser negativo")
else:
    print("Valor total Valido")
