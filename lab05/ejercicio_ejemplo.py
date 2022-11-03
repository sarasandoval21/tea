try:
    file2read = input ("Ingrese el nombre del archivo: ")
    fhandle = open(file2read, "r")
    for linea in fhandle:
     print(linea.upper())
except:
    print("Error, archivo no existente") 