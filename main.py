import lib_e6
import random


def generador_ptos(num: int, min_x: int, min_y: int) -> list:
    """
    Genera una cantidad 'num' de puntos (x, y)

    Args:
        num (list): numero
        min_x (int): rango minimo de coordenadas x que puede optar un punto
        min_y (int): rango minimo de coordenadas y que puede optar un punto

    Return:
        list: plano con 'num' puntos
    """
    plano = []

    for n in range(num):
        punto = []
        punto.append(random.randint(min_x, min_y))
        punto.append(random.randint(min_x, min_y))
        plano.append(punto)

    return plano


# Pruebas aleatorias de lib_e6
plano = [(1, 2), (3, 5), (11, 0), (11, 17), (4, 2)]
fb = lib_e6.fuerza_bruta(plano)
dc = lib_e6.divide_conquer(plano)
print(type(fb), fb)
print(type(dc), dc)
