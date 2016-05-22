# CLASE 3
# Autor: Abdel G. Martinez L.
#
# Instrucciones: Calcular el monto final que debe pagar Analida
# por comprar tres articulos con tasas de impuestos distintas.
# Los articulos que compro son: vestido ($75, 3.5%), celular ($525,
# 2.25%) y zapatos ($25, 15%).

vestido = 75
vestido_i = 0.035
celular = 525
celular_i = 0.0225
zapatos = 25
zapatos_i = 0.15

print("PROBLEMA DE EJEMPLO")

subtotal = vestido + celular + zapatos
impuesto = (vestido_i*vestido) + (celular_i*celular) + (zapatos_i*zapatos)
total = subtotal + impuesto

print("El total es $" + str(total))
