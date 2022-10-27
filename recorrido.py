def recorrido(lista):
    condicion_300=0
    for i in range (len(lista)):

        if lista[i]%10==0 and lista[i]<200:
            print("\n",lista[i])
        elif lista[i]>300:                
            condicion_300=1
            return condicion_300
        
    return condicion_300

def main():
    lista_1=[18,50,210,80,145,33,70,30]
    valor=recorrido(lista_1)
    if valor==1:
        print("Se ha encontrado un numero mayor de 300")
    elif valor==0:
        print("No hay ningún número mayor que 300")

main()