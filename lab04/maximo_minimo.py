# Estableciendo parametros
from ast import While
contador = 0
suma = 0
minimo = 0
maximo = 0
primerNumero = True

while True:
 try:
   numero = input ("Introduzca un número: ")
   if (numero == "fin"):
      break
   else:
      contador = contador +1
      suma = suma + int(numero)
      if (primerNumero):
         minimo = int(numero)
         maximo = minimo
         primerNumero = False
      else:
          if (int(numero) > maximo):
             maximo = int(numero)
          if (int (numero) < minimo):
              minimo = int(numero)
 except:
      print("Entrada inválida")
      contador = contador -1
      continue
print ("Minimo:", minimo)
print ("Máximo:", maximo)



