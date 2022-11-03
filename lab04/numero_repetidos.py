contador =0 
suma = 0
while True:
    try:
        numero = input ("Introduzca un número: ")
        if (numero == "fin"):
          break
        else:
            contador = contador + 1
            suma = suma + int(numero)
    except:
        print ("Entrada inválida")
        contador = contador - 1
        continue
print ("contador:", contador)
print ("suma:", suma)
print ("promedio:", suma/contador)

