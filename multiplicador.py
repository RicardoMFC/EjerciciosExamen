import sys
def introducir_num():
    try:
        numero_usuario = int (input("Introduzca un número entre 1 y 9\n"))
        while numero_usuario<0 or numero_usuario>9:
            numero_usuario = int (input("Introduzca un número entre 1 y 9\n"))

    except:
        pass
    else:
        return numero_usuario

def algoritmo():
    numero_magico=12345679
    num_usu=introducir_num()
    num_usu=num_usu*9
    numero_magico=numero_magico*num_usu
    print (numero_magico)
algoritmo()
