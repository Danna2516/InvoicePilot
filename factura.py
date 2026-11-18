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

# Iteramos sobre cada diccionario (factura) en la lista 'facturas' 
for factura in facturas:
    print(factura)
    #Sumar el total de cada factura al acumulador (usamos int() porque el total es un texto)
    total_facturas =+ int(factura["total"]) #se calcula el total de las facturas juntas
    print(f"Numero: {factura['numero']}| Proveedor: {factura['proveedor']}") # y usamos las claves ['numero'] y ['proveedor'] para extraer esos datos específicos.
print (f"Total: ",{total_facturas}) #se imprime el valor total de las facturas

#Calcular el total de las facturas

total_facturas = total_facturas + int(factura["total"])