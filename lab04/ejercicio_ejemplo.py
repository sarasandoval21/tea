
while True:
  vegetal = input("Ingrese el tipo del vegetal: ")
  if (vegetal == "salir"):
    break
  else:
    if (vegetal == "hortaliza"):
      print ("Ejemplo: Maiz")
    elif (vegetal == "frutal"):
      print ("Ejemplo: Mango")
    elif (vegetal == "ornamental"):
      print ("Ejemplo: Rosal")
    else:
      print ("no definido")