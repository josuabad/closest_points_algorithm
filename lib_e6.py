def distancia(pto1: list[int], pto2: list[int]) -> float:
    """
    Distacia entre 2 puntos -> formula euclidea

    Args:
        pto1 (list): coordenadas x1 - y1
        pto2 (list): coordenadas x2 - y2

    Return:
        num: distancia entre los puntos
    """
    return ((pto2[0] - pto1[0]) ** 2 + (pto2[1] - pto1[1]) ** 2) ** 0.5


def fuerza_bruta(plano: list[int]) -> tuple:
    """
    Pares de puntos mas cercanos en un plano

    Args:
        plano (list): puntos

    Return:
        tuple: puntos mas cercanos y distancia entre ellos
    """
    punto1 = []
    punto2 = []
    dist = 0
    count = 0

    if len(plano) < 2:
        return TypeError # No permite que en el plano no haya mas de 1 punto

    for puntoA in plano:
        for puntoB in plano:
            if puntoB == plano[count]:
                continue # No se compara a si mismo
            dist_temp = distancia(puntoA, puntoB)
            if count == 0: # Primer cambio de las variables iniciadas
                dist = dist_temp
                punto1 = puntoA
                punto2 = puntoB
            else:
                if dist_temp < dist:
                    dist = dist_temp
                    punto1 = puntoA
                    punto2 = puntoB
        count += 1 # Evita errores de redundancia

    return punto1, punto2, dist
