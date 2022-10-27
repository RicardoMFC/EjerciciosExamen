import sys
def inrtoducir_lista():
    try:
        lista=[]
        longitud = int (input("Introduzca el numero de elementos que quiere introducir en la lista\n"))
        for i in range (longitud):
            lista.append(input("Introduzca el elemento {}\n".format(i)))
        print (lista)

    except:
        pass
    else:
        return lista, longitud

def reverse_lista(lista, longitud):
    
    for i in range (int(longitud/2)):
        aux=lista[longitud-i-1]
        lista[longitud-i-1]=lista[i]
        lista[i]=aux

    return lista

def main():
    lista, longitud=inrtoducir_lista()
    lista_invertida=reverse_lista(lista, longitud)
    print(lista_invertida)
main()
    
