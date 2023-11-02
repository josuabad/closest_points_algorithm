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
