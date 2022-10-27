import math
import sys

def introducir_num():
    try:
        numero_usuario = int (input("Introduzca un número\n"))
        while numero_usuario<=0:
            numero_usuario = int (input("Introduzca un número\n"))

    except:
        pass
    else:
        return numero_usuario

def salida_ceros(numero):
    aux=numero
    cifras=0
    while aux!=0:
        aux=int(aux/10)
        cifras+=1

    exponente=0
    while numero!=0:
        x=(numero%10)*pow(10,exponente)
        print("{}\n".format(str(x).zfill(cifras)))
        numero=int(numero/10)
        exponente+=1

def main():
    numero=introducir_num()
    salida_ceros(numero)

if __name__=='__main__':
    main()
    
