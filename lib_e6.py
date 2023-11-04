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


def divide_conquer(plano: list[int]) -> tuple:
    """
    Pares de puntos mas cercanos en un plano

    Args:
        plano (list): puntos

    Return:
        tuple: puntos mas cercanos y distancia entre ellos
    """
    long_plano = len(plano)

    if long_plano <= 1:
        return float('inf')  # Si hay menos de 2 puntos, no se puede calcular distancia
    
    if long_plano == 2:
        return distancia(plano[0], plano[1]) # Caso base
    
    # Ordena los puntos por coordenada x
    puntos_ordenados_x = sorted(plano, key=lambda punto: punto[0]) # Timsort
    
    # Divide el conjunto en dos mitades
    mitad = long_plano // 2
    izquierda = puntos_ordenados_x[:mitad]
    derecha = puntos_ordenados_x[mitad:]
    
    distancia_izquierda = divide_conquer(izquierda)
    distancia_derecha = divide_conquer(derecha)
    
    # Encontrar la distancia mínima entre las dos mitades
    distancia_minima_entre_mitades = min(distancia_izquierda, distancia_derecha)
    
    # Encontrar la franja con los puntos cercanos a la mitad de la division
    pto_medio = puntos_ordenados_x[mitad][0]
    franja = []
    for punto in puntos_ordenados_x:
        if abs(punto[0] - pto_medio) < distancia_minima_entre_mitades:
            franja.append(punto)

    # Compara las distancias por una posible menor
    distancia_franja = float('inf')
    for puntoA in range(len(franja)):
        for puntoB in range(puntoA + 1, len(franja)):
            distancia_actual = distancia(franja[puntoA], franja[puntoB])
            distancia_franja = min(distancia_franja, distancia_actual)
    
    # Encontrar la distancia mínima entre las tres posibilidades
    return min(distancia_minima_entre_mitades, distancia_franja)
