"""Ejercicio 5: 
Se está realizando una obra de teatro para recaudar fondos, se quiere 
recaudar un total de 1.000.000$. 

Para la obra hay 3 valores de entradas: 
   * Entrada básica de 20.000$
   * Entrada premium de 40.000$ 
   * Entrada VIP de 100.000$

Realice un programa en el que: 
   a. Se pregunte al usuario por el tipo entrada que quiere comprar, 
   b. después de ingresar el tipo de entrada el programa saca en pantalla 
   “Disfrute la función”, esto se repetirá para el siguiente usuario. 
   c. El programa se detendrá cuando el dinero acumulado por las entradas 
   sea mayor a 1.000.000$, cuando esto pase, mostrar en pantalla el total 
   de usuarios que ingresaron a la obra."""


totalUsuarios=0
totalValorEntradas=0

while totalValorEntradas < 1000000:
    
    entrada=input("Elige tu entrada:\nBásica: $20.000\nPremium: $40.000\nVIP: $100.000")
    totalUsuarios += 1
    
    if entrada.lower() == "basica":
        totalValorEntradas += 20000
        print("Disfrute la función")
    elif entrada.lower() == "premium":
        totalValorEntradas += 40000 
        print("Disfrute la función")
    elif entrada.lower() == "vip":
        totalValorEntradas += 100000
    else:
        print("No se reconoce la entrada, intente de nuevo")
    
    print("Total de usuarios:",totalUsuarios," y valor total de entradas:",totalValorEntradas)
        
print("En esta función tuvimos:",totalUsuarios," usuarios.")