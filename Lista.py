import Nodo

class List:
    def __init__(self):
        self.inicio = None

    #Instacia un nuevo nodo al inicio de la lista
    def insertar_inicio(self, item):
        nuevo_nodo = Nodo.Nodo(item)
        nuevo_nodo.next = self.inicio
        self.inicio = nuevo_nodo

    #Busca el final de la lista mediante un puntero, y luego agrega el nodo en esta posicion.
    def insertar_final(self, item):
        nuevo_nodo = Nodo.Nodo(item) #Este es el nuevo nodo
        if self.inicio is None:
            self.inicio = nuevo_nodo #En caso de estar vacia directamente se inserta al inicio
        else:
            puntero = self.inicio #De otro modo, buscara el final de la lista viendo si tiene un nodo
            while puntero.next is not None:
                puntero = puntero.next
            puntero.next = nuevo_nodo #Luego inserta el nodo en el puntero donde se encuentra el final

    def insertar_posicion(self, item, pos):
        nuevo_nodo = Nodo.Nodo(item) #Crea el nodo
        if self.inicio is None or pos == 1:
            #Para no tener que buscar durante toda la lista, lo mismo si la posicion
            # es la primera directamente se inserta en esta posicion
            nuevo_nodo.next = self.inicio
            self.inicio = nuevo_nodo
        else: #De otro modo se busca de igual forma donde esta la posicion
            puntero = self.inicio
            for _ in range(pos - 2):
                if puntero.next is None:
                    break
                puntero = puntero.next
            nuevo_nodo.next = puntero.next #Y se agrega el nuevo nodo
            puntero.next = nuevo_nodo

    def eliminar_inicio(self): #Se elimina el nodo que se encuentra al inicio de la lista
        if self.inicio is None:
            print("La lista esta vacia!")
        elif self.inicio.next is None: #En este caso, si solo hay un elemento simplemente elimina el unico nodo presente
            self.inicio = None
        else: #De otra forma, busco el primer nodo
            puntero_ant = self.inicio
            puntero_sig = self.inicio.next
            while puntero_sig.next is not None:
                puntero_ant = puntero_sig
                puntero_sig = puntero_sig.next
            puntero_ant.next = None

    def eliminar_final(self): #Se elimina el nodo que se encuentra al final de la lista xd
        if self.inicio is None:
            print("La lista está vacía!")
        elif self.inicio.next is None: #Misma metodologia que el anterior
            self.inicio = None
        else:
            puntero_ant = self.inicio
            puntero_sig = self.inicio.next
            while puntero_sig.next is not None:
                puntero_ant = puntero_sig
                puntero_sig = puntero_sig.next
            puntero_ant.next = None

    def eliminar_posicion(self, pos): #Buscamos en una posicion dentro de la lista y lo elimina
        if self.inicio is None:
            print("La lista está vacía!")
            return
        if pos == 1:
            self.inicio = self.inicio.next
            return
        puntero = self.inicio
        for _ in range(pos - 2):
            if puntero.next is None:
                print("Posición fuera de rango")
                return
            puntero = puntero.next
        if puntero.next is None:
            print("Posición fuera de rango")
        else:
            puntero.next = puntero.next.next

    def mostrar(self):
        #Lista todos los elementos dentro de la lista, y el final es un null, como se define
        # en este tipo de listas
        if self.inicio is None:
            print("La lista está vacía")
        else:
            puntero = self.inicio
            while puntero is not None:
                print(f"{puntero.dato} -> ", end="")
                puntero = puntero.next
            print("None")

    #Variables usadas:
    #Siempre instanciaba un nuevo nodo en cada metodo.
    #Las variables como puntero son para buscar dentro de la lista, puntero anterior y siguiente
    #es para mantener esa data a la hora de eliminar en una posicion especifica
    #En general, es una implementacion sencilla de las listas simplemente enlazadas