import os
os.system("cls")

horas = int (input ("ausencia al trabajo: "))
tornillosD = int (input ("tornilllos defectuosos: "))
tornillosN = int (input ("tornilllos no defectuosos: "))

if horas > 1.5 and tornillosD > 300 and tornillosN < 10000:
    grado = 5
if horas < 1.5 and tornillosD > 300 and tornillosN < 10000:
    grado = 7
if horas > 1.5 and tornillosD < 300 and tornillosN < 10000:
    grado = 8
if horas > 1.5 and tornillosD > 300 and tornillosN > 10000:
    grado = 9
if horas < 1.5 and tornillosD < 300 and tornillosN > 10000:
    grado = 12
if horas < 1.5 and tornillosD > 300 and tornillosN < 10000:
    grado = 13
if horas > 1.5 and tornillosD < 300 and tornillosN < 10000:
    grado = 15
if horas < 1.5 and tornillosD < 300 and tornillosN < 10000:
    grado = 20

print (f"el grado de eficiencia es: {(grado)}")
print()