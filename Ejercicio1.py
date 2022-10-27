import string
import sys

def mayus_minus(var_1):
    var_1=string.ascii_letters
    print(len(var_1))

    longitud=len(var_1)/7
    longitud_decimales="{:06.04f}".format(longitud)
    return longitud_decimales

def funcion1():
    operacion=12 - (4*2) - (2+2)
    return operacion

def funcion2():
    operacion=12 - 4 * (2 - 2) + 2
    return operacion

def funcion3():
    try:
        edad=int(input("Introduzca su edad\n"))
        while edad<=0:
            edad=int(input("Introduzca su edad\n"))
    except:
        pass
    else:
        if edad>=18:
            return True
        else:
            return False
        


def main():
    cadena="Módulo 1 de Python"
    cadena_final=mayus_minus(cadena)
    
    resultado_funcion1=funcion1()
    resultado_funcion2=funcion2()

    print(cadena_final)
    print(resultado_funcion1)
    print(resultado_funcion2)

    resultado_funcion3=funcion3()
    if resultado_funcion3==1:
        print("Es mayor de edad\n")
    else:
        print("No es mayor de edad\n")
main()