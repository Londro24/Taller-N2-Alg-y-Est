import time
from random import randint


def generar_datos(cantidad_de_datos):
    list_datos = []
    extremo_izquierdo = randint(int(cantidad_de_datos/4), int(cantidad_de_datos/2))
    extremo_derecho = randint(int(cantidad_de_datos*2), int(cantidad_de_datos*4))
    for _i in range(cantidad_de_datos):
        list_datos.append(randint(extremo_izquierdo, extremo_derecho))
    return list_datos


def histograma(list_datos, cant_intervalo, list_histograma):
    dato_mayor = 0
    dato_menor = list_datos[0]
    for dato in list_datos:
        if dato > dato_mayor:
            dato_mayor = dato
        elif dato < dato_menor:
            dato_menor = dato
    extencion_intervalo = ((dato_mayor - dato_menor)/cant_intervalo)
    if extencion_intervalo % int(extencion_intervalo) < 0.5:
        extencion_intervalo = int(extencion_intervalo)
    else:
        extencion_intervalo = int(extencion_intervalo) + 1
    for dato in list_datos:
        dato = dato - dato_menor
        if int(dato/extencion_intervalo) == cant_intervalo:
            indice = int(dato/extencion_intervalo) - 1
        else:
            indice = int(dato/extencion_intervalo)
        list_histograma[indice].append(dato + dato_menor)
    for indice in range(cant_intervalo):
        list_histograma[indice] = len(list_histograma[indice])
    return list_histograma


if __name__ == "__main__":
    # max = 100000000
    for _i in range(10):
        cantidad_de_datos = 1000
        inicio = time.time()
        list_datos = generar_datos(cantidad_de_datos)
        fin = time.time()
        cant_intervalo = int(len(list_datos) ** 0.5)
        list_histograma = []
        for _i in range(cant_intervalo):
            list_histograma.append([])
        print(cant_intervalo)
        print(len(list_histograma))
        inicio = time.time()
        list_histograma = histograma(list_datos, cant_intervalo, list_histograma)
        fin = time.time()
        print(fin-inicio)
