def modificar1(lista):
    lista2=[]
    lista2.append(lista[-1:0:-2])
    return lista2
    
def modificar2(lista):
    aux=lista[0]
    lista[0]=lista[-1]
    lista[-1]=aux
    return lista

def eliminar_elemento(lista):
    lista.pop(-1)
    return lista

def guardar_en_lista(lista):
    lista_3=[]
    for i in range(len(lista)):
        lista_3.append(lista[i])
    return lista_3
     
def main():
    lista=[1,1.83,'q',-1]
    lista2=modificar1(lista)
    lista3=modificar2(lista)
    lista4=eliminar_elemento(lista3)
    print(lista2)
    

main()