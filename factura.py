# Diccionario donde se almacenan los datos de la factura   
factura = {"numero": "23",
         "proveedor": "aseos",
         "fecha": "23-10-2026",
         "total": 2000}

print(f"Numero de factura: {factura ['numero']}")
print(f"proveedor de factura: {factura ['proveedor']}")
print(f"fecha de factura: {factura ['fecha']}")
print(f"total de factura: {factura ['total']}")
# # imprimir individualmente cada dato
# # para imprimir valores se pone nom_var.valuees()
# for valor in factura.values():
#     print(valor)

# # cambiar el valor de la clave: proveedor
# factura["proveedor"] = "Vimash"
# print(factura["proveedor"])
# # llamar una clave llamada moneda
# factura["moneda"] = "COP"
# print(factura)
# # situacion cuando una clave no existe
# """print(factura["descuento"]) 
# envia error porque la clave no esta determinada en el diccionario"""
# factura.get("descuento")
