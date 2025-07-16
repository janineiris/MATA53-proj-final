import heapq


def coloring(grafo):
    def menor_cor_possivel(grafo, vertice: int) -> int:
        for vizinho in grafo.vertices[vertice].vizinhanca:
            cor_vizinho = grafo.vertices[vizinho].cor
            if cor_vizinho is not None:
                cores_usadas[cor_vizinho] = True

        cor = 1
        while cor < grafo.n + 1:
            if (cores_usadas[cor] == False):
                break
            cor += 1

        for vizinho in grafo.vertices[vertice].vizinhanca:
            cor_vizinho = grafo.vertices[vizinho].cor
            if cor_vizinho is not None:
                cores_usadas[cor_vizinho] = False

        return cor

    print("\n[DSATUR] Coloração iniciada...")
    grafo.resetar_cores()

    # Inicializa saturação de todos os vértices como 0
    saturacao = {v: 0 for v in grafo.vertices.keys()}
    grau = {index: len(vertice.vizinhanca) for index, vertice in grafo.vertices.items()}

    cores_usadas = [False for i in range(0, grafo.n + 1)]

    fila_prioridade = []
    for vertice in grafo.vertices:
        heapq.heappush(fila_prioridade,  ((-saturacao[vertice], -grau[vertice], vertice), vertice))

    while fila_prioridade:
        _, proximo = heapq.heappop(fila_prioridade)

        # Se o próximo da fila tiver saturação igual (desatualizada), recalcula e reempilha com valor atualizado
        while fila_prioridade and _ == fila_prioridade[0][0]:
            _, vertice = heapq.heappop(fila_prioridade)
            heapq.heappush(fila_prioridade,  ((-saturacao[vertice], -grau[vertice], vertice), vertice))

        # Determina a menor cor possível que os vizinhos ainda não usam
        cor = menor_cor_possivel(grafo, proximo)

        # Atribui cor
        grafo.vertices[proximo].cor = cor

        for vizinho in grafo.vertices[proximo].vizinhanca:
            # Adiciona vizinhos na fila de prioridade
            if grafo.vertices[vizinho].cor is None:
                heapq.heappush(fila_prioridade, ((-saturacao[vizinho], -grau[vizinho], vizinho), vizinho))
                grau[vizinho] -= 1

    print("[DSATUR] Coloração finalizada.")
