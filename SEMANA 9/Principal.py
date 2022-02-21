from listas import Lista
from Menu import principal
from pilas import Pilas
from colas import Colas
import time
import os
os.system("cls")
var = principal()
lis = ["1)Listas","2)Pilas","3)Colas","4)Salir"]
opcion = ""
while opcion != "4":
    os.system("cls")
    opcion = var.menu(lis)
    if opcion == "1":
        opc1= ""
        lista = Lista()
        while opc1 != "8":
            os.system("cls")
            opc1 = var.menu (["1.agregar", "2.eliminar", "3.mostrar", "4.Eliminarla posicion" , "5.insertar", "6.buscar", "7.vaciarla lista", "8. salir"])
            if opc1 == "1":
                for x in range(4):
                    valor=input("Inserte elementos para completar la lista :")
                    lista.agregar(valor)
               
            elif opc1 == "2":
                    lista.eliminar()
                    
            elif opc1 == "3":
                    lista.mostrar()
                   
            elif opc1 == "4":
                    while True:
                            indice= int(input("ingrese el valor de la posicion para poder eliminar: "))
                            os.system("cls")        
                            a = lista.eleminarElemento(indice)
                            if a == True:
                                break
                            else:
                                print("posicion invalida")
                               
                                os.system("cls")      
            elif opc1 == "5":
                    pos=int(input("ingrese una posición: "))
                    dato = input("ingrese un nombre: ")
                    lista.InsertarElemento(pos,dato)
                   
            elif opc1 == "6":
                    while True:
                            dato=input("ingrese el valor de la posicion que desea: ")
                            os.system("cls")        
                            a = lista.buscar(dato)
                            if a == True:
                                break
                            else:
                                print(" posicion invalida")
                               
                                os.system("cls")         
            elif opc1 == "7":
                    lista.clear()
                   
            elif opc1 == "8":
                    print("retorno al menu")
                    
                    os.system("cls")
    if opcion == "2":
        opc1 = ""
        tam = int(input("defina la extension de la pila: "))        
        pila = Pilas(tam)
        while opc1 != "6":
            os.system("cls")
            opc1 = var.menu (["1)Push", "2)Pop", "3)Show", "4)Buscar" , "5)Longitud", "6)Salir"])
            if opc1 == "1":
                valor=input("Inserte elementos para completar la pila: ")
                pila.push(valor)
                
            elif opc1 == "2":
                print(pila.pop())
               
            elif opc1 == "3":
                pila.show()
                
            elif opc1 == "4":
                while True:
                    buscado=input("ingrese el valor de la posicion que desea: ")
                    os.system("cls")        
                    a = pila.buscar(buscado)
                    if a == True:
                        break
                    else:
                        print("posicion invalida")
                       
                        os.system("cls") 
              
            elif opc1 == "5":
                pila.longitud()
              
            elif opc1 == "6":
                    print("retorno al menu")
                   
                    os.system("cls")
    if opcion == "3":
        opc1 = ""
        tam = int(input("defina la extension de la cola: "))        
        cola = Colas(tam)
        while opc1 != "6":
            os.system("cls")
            opc1 = var.menu (["1)Push", "2)Pop", "3)Show", "4)Buscar" , "5)Longitud", "6)Salir"])
            if opc1 == "1":
                valor=input("Inserta elemento para completar la cola: ")
                cola.push(valor)
               
            elif opc1 == "2":
                print(cola.pop())
               
            elif opc1 == "3":
                cola.show()
              
            elif opc1 == "4":
                while True:
                    buscado=input("Ingrese el valor de la posicion que desea: ")
                    os.system("cls")        
                    a = cola.buscar(buscado)
                    if a == True:
                        break
                    else:
                        print("posicion invalida")
                     
                        os.system("cls") 
            
            elif opc1 == "5":
                cola.longitud()
             
            elif opc1 == "6":
                    print("Retorno al menu")
                   
                    os.system("cls")
    if opcion == "4":
           os.system("cls")
print("Final del programa")
