import sys

def modificar(lista):
    lista2=[]
    lista1=list(set(lista))
    print(lista1)

    lista1=sorted(lista1, reverse=True)
    for i in range (len(lista1)):
        if lista1[i]%2==0:
            lista2.append(lista1[i])

    suma=sum(lista2)
    lista2.insert(0,suma)
    print(lista2) 
    return lista2

def main():
    lista=[2,1,2,3,4,5,7,8,6,9,9,7,6,5,6,9]
    lista_final=modificar(lista)
    print(sum(lista_final[1:])==lista_final[0])
main()