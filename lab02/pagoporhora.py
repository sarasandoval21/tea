# Tendencias e Innovación en Tecnologia Agricola (TE)
# display numero de horas que trabaja
from sys import float_repr_style


horas= input("Ingrese el numero de horas trabajadas: ")
valor= input("Ingrese el valor de cada hora trabajada: ")

# El total del valor de pago
total= int(horas) * float(valor)

print("Su pago es de: ", total)



