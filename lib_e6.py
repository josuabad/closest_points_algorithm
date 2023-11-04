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


def fuerza_bruta(plano: list[int]) -> list:
    """
    Pares de puntos mas cercanos en un plano

    Args:
        plano (list): puntos

    Return:
        list: puntos mas cercanos y distancia entre ellos
    """
    punto1 = []
    punto2 = []
    dist = float('inf')
    count = 0

    if len(plano) < 2:
        return TypeError # No permite que en el plano no haya mas de 1 punto

    for puntoA in plano:
        for puntoB in plano:
            if puntoB == plano[count]:
                continue # No se compara a si mismo
            dist_temp = distancia(puntoA, puntoB)
            if dist_temp < dist:
                dist = dist_temp
                punto1 = puntoA
                punto2 = puntoB
        count += 1 # Evita errores de redundancia

    return [punto1, punto2, dist]


def divide_conquer(plano: list[int]) -> list:
    """
    Pares de puntos mas cercanos en un plano

    Args:
        plano (list): puntos

    Return:
        list: puntos mas cercanos y distancia entre ellos
    """
    long_plano = len(plano)

    if long_plano <=3: #Este es el caso base
        return fuerza_bruta(plano)

    # Ordena los puntos por coordenada x
    puntos_ordenados_x = sorted(plano, key=lambda punto: punto[0])  # Timsort

    # Divide el conjunto en dos mitades
    mitad = long_plano // 2
    izquierda = puntos_ordenados_x[:mitad]
    derecha = puntos_ordenados_x[mitad:]

    distancia_izquierda = divide_conquer(izquierda)
    distancia_derecha = divide_conquer(derecha)

    # Encontrar la distancia mínima entre las dos mitades
    distancia_minima_entre_mitades = min(distancia_izquierda, distancia_derecha, key = lambda x: x[2])

    # Encontrar la franja con los puntos cercanos a la mitad de la division
    pto_medio = puntos_ordenados_x[mitad][0]
    franja = []
    distancia_minima_temporal = distancia_minima_entre_mitades[2] # [type -> float] comparacion distancias + evita TypeError
    for punto in puntos_ordenados_x:
        if abs(punto[0] - pto_medio) < distancia_minima_temporal:
            franja.append(punto)

    # Compara las distancias por una posible menor
    distancia_franja = [None, None, float('inf')]
    for puntoA in range(len(franja)):
        for puntoB in range(puntoA + 1, len(franja)):
            distancia_actual = [franja[puntoA], franja[puntoB], distancia(franja[puntoA], franja[puntoB])]
            distancia_franja = min(distancia_franja, distancia_actual, key = lambda x : x[2]) #Con el key lambda x : x[2] se comprueba el segundo valor de la lista y se mira cual es el minimo

    return min(distancia_minima_entre_mitades, distancia_franja, key = lambda x:x[2])
