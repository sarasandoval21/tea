def calculoSalario(horas, tarifa):
    MAX_HORAS_SEMANALES = 40
    horas_extras = 0
    if(horas) > MAX_HORAS_SEMANALES:
        horas_extras = (horas) - MAX_HORAS_SEMANALES
        calculo = ( MAX_HORAS_SEMANALES * tarifa) + (horas_extras * (tarifa) *1.5)
    else:
        calculo = horas * tarifa
    return calculo

try:
    horas =  int(input("ingrese numero de horas: "))
    tarifa = float(int(input("ingrese tarifa por hora: ")))
    pago = calculoSalario(horas, tarifa)
    print(pago)
except:
    print("Error, ingresar un valor numerico")