import sys

def reverse_lista(lista): 
    for i in range (int(len(lista)/2)):
        aux=lista[len(lista)-i-1]
        lista[len(lista)-i-1]=lista[i]
        lista[i]=aux

    return lista

def main():
    cadena = "zeréP nauJ,01"
    lista=list(cadena)
    lista_invertida=reverse_lista(lista)
    print(lista_invertida)
main()
    
