"""
Ejercicio 6: 

Realice un programa que permita realizar la división de 2 variables ingresadas por el 
usuario y muestre su resultado en pantalla. 

El programa debe mostrar:
  1. El mensaje “Los datos ingresados no son numéricos” si se ingresa algún dato que no se pueda 
  convertir a número. 
  2. Mostrar el mensaje “No fue posible realizar la división” si se ingresa 0 en el segundo termino 
  (Esto es por la división de x/0 no está definida) """
  
valor=input("Deseas ingresar tus números? (S/N)")

while valor == "S":
    
    try:
        x=float(input("Ingrese el primer número"))
        y=float(input("Ingrese el segundo número"))
        print(x/y)
    except ValueError:
        print("El dato ingresado no es válido")
    except ZeroDivisionError:
        print("No se puede dividir por 0")
    else:
        valor=input("Deseas ingresar tus números? (S/N)")
    