# algoritmo que implemente un menu de opciones
# Tienda de ropa básica
# Usuario ingrese su presupuesto, y seleccione una prenda
# Camiseta:40 Pantalon:130 Falda:80 Zapatos:200

"""
Ejercicio 7: 
En el archivo Tienda_While.py se encuentra un algoritmo que realiza la operación de 
una tienda de ropa. Modifique el algoritmo de manera que: 
1. Termine su operación si se acaba el presupuesto. 
2. No permita ingresar datos erróneos en el presupuesto como por ejemplo 
caracteres, si esto ocurre vuelva a pedir el presupuesto."""

def compra():
    
    try:
        Presupuesto=float(input("Ingrese su presupuesto"))
        
        while Presupuesto<40:
            #Decision=input("No le alcanza para ninguna prenda, ingrese sí para ingresar nuevamente el presupuesto")
            #if Decision.lower()!="sí":
            
            #    break
            print("Ingrese su presupuesto nuevamente")
            Presupuesto=float(input("Ingrese su presupuesto"))
            
    except ValueError:
        print("Ingrese un valor numérico")
        compra()
        
    else:
        print("Elija su prenda:\nCamiseta:40\nPantalon:130\nFalda:80\nZapatos:200")
        
        while True:
            
            try:
                Eleccion=input("Elija su prenda,  ingrese salir para terminar la compra:")
                Costo=0
                if Eleccion.lower()=="camiseta":#==   !=
                    Costo=40
                elif Eleccion.lower()=="pantalon":
                    Costo=130
                    #FALda->"falda"=="falda"
                    
                elif Eleccion.lower()=="falda":
                    Costo=80
                elif Eleccion.lower()=="zapatos":
                    Costo=200
                elif Eleccion.lower()=="salir":
                    print("Gracias por comprar")
                    break
                else:
                    print(Eleccion,"No está en el catalogo")
                    
                print("Su prenda costó:",Costo)

                #Presupuesto=Presupuesto-Costo
                Presupuesto-=Costo
                
                if Presupuesto>=0:
                    print("Su compra ha sido exitosa, le sobró:",Presupuesto)
                else:
                    print("No te alcanzó para la compra :(")
                    break
            except IndexError:
                print("Ingrese un dato válido")

compra()


