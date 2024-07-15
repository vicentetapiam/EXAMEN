from os import system
from random import randint
from statistics import geometric_mean
system("cls")


trabajadores=["Juan Perez","Maria Garcia","Carlos Lopez","Ana Martinez","Pedro Rodriguez","Laura Hernandez","Miguel Sanches","Isabel Gomez","Fancisco Dias","Elena Fernandez"]
lista_sueldos=[]
sueldo_menor_800000=[]
a=0


#arreglar generar nuevos sueldos
def asignar_sueldos():
    system("cls")
    print("Asignar sueldos aleatorios:")
    for i in range(10):
        sueldo_aleatorio=randint(300000,2500000)
        lista_sueldos.append(sueldo_aleatorio)
    print(lista_sueldos)


def clasificar_sueldos():
    system("cls")
    print("Clasificar Sueldos:")
    while True:
        if a!=0:
            if lista_sueldos[0] < 800000:
                sueldo_menor_800000.append(trabajadores[0])
                sueldo_menor_800000.append(lista_sueldos[0])
            elif lista_sueldos[1] < 800000:
                sueldo_menor_800000.append(trabajadores[1])
                sueldo_menor_800000.append(lista_sueldos[1])
            elif lista_sueldos[2] < 800000:
                sueldo_menor_800000.append(trabajadores[2])
                sueldo_menor_800000.append(lista_sueldos[2])
            elif lista_sueldos[3] < 800000:
                sueldo_menor_800000.append(trabajadores[3])
                sueldo_menor_800000.append(lista_sueldos[3])
            elif lista_sueldos[4] < 800000:
                sueldo_menor_800000.append(trabajadores[4])
                sueldo_menor_800000.append(lista_sueldos[4])
            elif lista_sueldos[5] < 800000:
                sueldo_menor_800000.append(trabajadores[5])
                sueldo_menor_800000.append(lista_sueldos[5])
            elif lista_sueldos[6] < 800000:
                sueldo_menor_800000.append(trabajadores[6])
                sueldo_menor_800000.append(lista_sueldos[6])
            elif lista_sueldos[7] < 800000:
                sueldo_menor_800000.append(trabajadores[7])
                sueldo_menor_800000.append(lista_sueldos[7])
            elif lista_sueldos[8] < 800000:
                sueldo_menor_800000.append(trabajadores[8])
                sueldo_menor_800000.append(lista_sueldos[8])
            elif lista_sueldos[9] < 800000:
                sueldo_menor_800000.append(trabajadores[9])
                sueldo_menor_800000.append(lista_sueldos[9])
            elif lista_sueldos[10] < 800000:
                sueldo_menor_800000.append(trabajadores[10])
                sueldo_menor_800000.append(lista_sueldos[10])
            print("*************************************************")
            print(f"Sueldos menores a $800.000 TOTAL: ")
            print("Nombre empleado/Sueldo")
            print(sueldo_menor_800000)
            break
        else:
            print("No hay datos...")
            break
            

def ver_estadisticas():
    system("cls")
    print("Ver estadisticas:")
    while True:
        if a!=0:
            print(f"Lista de sueldos: {lista_sueldos}")
            break
        else:
            print("No hay datos...")
            break


def reporte_sueldos():
    system("cls")
    print("Reporte de sueldo")
    while True:
        if a!=0:
            archivo=open("Trabajadores.csv","w")

            break
        else:print("No hay datos disponibles...")
        break

#menu
while True:
    print('''
1. Asignar sueldos aleatorios
2. Clasificar sueldos
3. Ver estadisticas
4. Reporte de sueldos
5. Salir del programa
''')
    op=input("Ingrese una opcion: ")
    match op:
        case "1":
            a=1
            asignar_sueldos()
        case "2":
            clasificar_sueldos()    
        case "3":
            ver_estadisticas()
        case "4":
            reporte_sueldos()
        case "5":
            system("cls")
            print("Finalizando programa...")
            print("Desarrollado por Vicente Tapia")
            print("RUT 21.694.997-8")
            break
        case other:
            system("cls")
            print("Ingrese opcion valida...")