import Lista
import os
clear = lambda: os.system('cls')
if __name__ == "__main__":
    print("Bienvenido a mi implementación de Lista Enlazada en Python")
    lista = Lista.List()
    lista.insertar_inicio(1)
    lista.insertar_inicio("arroz")
    lista.insertar_inicio(3.14153213)
    lista.insertar_inicio("implementado")
    #Agrege un menu funcional para que pueda ser usado por consola.
    #Ademas, inicialize algunos datos en la list para poder visualizarlos al ejecutar
    running = True
    while running:
        print("\n############ MENU ############\n")
        print("1. Ver la Lista")
        print("2. Agregar elemento al inicio de la lista")
        print("3. Agregar elemento al final de la lista")
        print("4. Agregar elemento a una posicion objetivo de la lista")
        print("5. Eliminar elemento al inicio de la lista")
        print("6. Eliminar elemento al final de la lista")
        print("7. Eliminar elemento a una posicion objetivo de la lista")
        print("8. Salir del programa")
        try:
            opc = int(input())
            if opc == 1:
                clear()
                lista.mostrar()
            elif opc == 2:
                clear()
                lista.insertar_inicio(input("Insertar al inicio de la lista: "))
            elif opc == 3:
                clear()
                lista.insertar_final(input("Insertar al final de la lista: "))
            elif opc == 4:
                clear()
                lista.mostrar()
                lista.insertar_posicion(input("Insertar la lista: "),int(input("Insertar en posicion objetivo de la lista: ")))
            elif opc == 5:
                clear()
                lista.eliminar_inicio()
            elif opc == 6:
                clear()
                lista.eliminar_final()
            elif opc == 7:
                clear()
                lista.mostrar()
                lista.eliminar_posicion(int(input("Insertar posicion objetivo de la lista: ")))
            elif opc == 8:
                running = False
            else:
                print("Opcion no valida, ingrese otra")
        except ValueError:
            print("El numero ingresado no es valido")