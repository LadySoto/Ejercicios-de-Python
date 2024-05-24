"""Ejercicio 4: 

Realice una calculadora con el siguiente funcionamiento: 
 1. El usuario ingresa 2 números decimales,  
 2. Después puede elegir entre 4 operaciones: Suma, resta,
 multiplicación o división.  
 3. Mostrar en pantalla el resultado y preguntar si desea realizar 
 otra operación. 
 4. Si la respuesta es sí, volver a 1.  caso contrario, termina el código.
"""


def calculadora():
    
    decimal1=float(input("Ingresa un decimal"))
    decimal2=float(input("Ingresa otro decimal"))
    operacion=input("Elige el número correspondiente a la operación: \nSuma (1)\nResta (2)\nMultiplicación (3)\nDivisión (4)")

    while True:
        if operacion == "1":
            print(decimal1 + decimal2)
            break
        elif operacion == "2":
            print(decimal1 - decimal2)
            break
        elif operacion == "3":
            print(decimal1 * decimal2)
            break
        elif operacion == "4":
            print(decimal1 / decimal2)
            break
        else:
            print("Opción no válida")
            break
    

calculadora()

while True:
    
    continuar=input("¿Necesitas hacer otra operación? Si,No")
    
    if continuar.lower() == "si":
        calculadora()
    elif continuar.lower() == "no":
        break
    else:
        print("Opción no inválida")
        break