calificacion = 0

while True:
  try:
        calificacion = float(input ("Introduzca puntuación: "))
        if (calificacion == "fin"):
            break
        else:
            if (calificacion == 10.0 ):
                print ("Puntuacion incorrecta")
            if (calificacion > 0.9):
                print ("Perfecto")
            if (calificacion >= 0.9):
                print ("Sobresaliente")
            if (calificacion > 0.8):
                print ("Notable")
            if (calificacion > 0.7):
                print ("Bien")
            if (calificacion > 0.6):
                print ("Suficiente")
            if (calificacion <= 0.6):
                print ("insuficiente")
  except:
    print ("Puntuacion incorrecta")
    
    
