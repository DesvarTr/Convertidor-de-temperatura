#Realizado por Gonzalo Montezuma

bule = True

def CelaFar():

    bf = True

    while bf:

        gradoscel = float(input("Ingrese los grados CELSIUS: "))

        if 100 >= gradoscel >= -273.15:
            
            bf = False
            return gradoscel,((gradoscel*9)/5)+32
        

        else:
            print("Ingrese una cantidad de grados CELSUIS MAYOR o igual a -273.15 °C y MENOR o igual a 100°C\n")
            bf = True

def FaraCel():

    bf = True

    while bf:

        gradosfar = float(input("Ingrese los grados FARENHEIT: "))

        if -459.67 <= gradosfar <= 212:

            bf = False
            return gradosfar , ((gradosfar-32)*5)/9

        else:
            print("Ingrese una cantidad de grados CELSUIS MAYOR o igual a -459.67 °C y MENOR a 212°C\n")
            bf = True

def menu():
    print("""Elija una opción
1. Convertir grados Celsius a Farenheit
2. Convertir grados Farenheit a Celcius
3. Salir del programa""")
    
    opcion = int(input("Ingrese la opción deseada: "))
    print()

    if opcion == 1:

        Results = CelaFar()
        print(f"La cantidad de {Results[0]} grados Celsius es:",Results[1],"grados Farenheit")

    elif opcion == 2:

        Results = FaraCel()
        print(f"La cantidad de {Results[0]} grados Farenheit es:",Results[1],"grados Celsius")
    
    elif opcion == 3:

        print("Programa cerrado")
        return False
    
    else:
        print("Ingrese una opción de menú válida (1,2 o 3)")
    
    return True
    
while bule:

    bule = menu()
    print()