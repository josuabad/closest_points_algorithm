def distancia(pto1: list, pto2: list):
    """
    Distacia entre 2 puntos -> formula euclidea

    Args:
        pto1 (list): coordenadas x1 - y1
        pto2 (list): coordenadas x2 - y2

    Return:
        num: distancia entre los puntos
    """
    return ((pto2[0] - pto1[0]) ** 2 + (pto2[1] - pto1[1]) ** 2) ** 0.5


def fuerza_bruta(plano: list):
    """
    Pares de puntos mas cercanos en un plano

    Args:
        plano (list): puntos

    Return:
        tuple: puntos mas cercanos y distancia entre ellos
        boolean: input no es un plano (lista con puntos)
    """
    punto1 = []
    punto2 = []
    dist = 0
    cont = 0

    if len(plano) < 2:
        return False

    for puntoA in plano:
        for puntoB in plano:
            if puntoB == puntoA:
                continue
            dist_temp = distancia(puntoA, puntoB)
            if cont == 0:
                dist = dist_temp
                punto1 = puntoA
                punto2 = puntoB
                cont += 1
            else:
                if dist_temp < dist:
                    dist = dist_temp
                    punto1 = puntoA
                    punto2 = puntoB

    return punto1, punto2, dist
