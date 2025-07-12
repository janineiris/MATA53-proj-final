def coloring(grafo):
    def atualiza_vizinhos(grafo, vertice: int, cor: int) -> None:
        for vizinho in grafo.vertices[vertice].vizinhanca:
            cores_usadas[vizinho].add(cor)
            saturacao[vizinho] = len(cores_usadas[vizinho])

    def menor_cor_possivel(grafo, vertice: int) -> int:
        vizinhos = grafo.vertices[vertice].vizinhanca
        cores_vizinhos = {
            grafo.vertices[v].cor for v in vizinhos if grafo.vertices[v].cor is not None
        }
        cor = 0
        while cor in cores_vizinhos:
            cor += 1
        return cor

    print("\n[DSATUR] Coloração iniciada...")
    grafo.resetar_cores()

    # Inicializa saturação de todos os vértices como 0
    saturacao = {v: 0 for v in grafo.vertices}
    cores_usadas = {v: set() for v in grafo.vertices}
    nao_coloridos = set(grafo.vertices.keys())

    # Começa pelo vértice de maior grau
    inicial = max(nao_coloridos, key=lambda v: len(grafo.vertices[v].vizinhanca))
    grafo.vertices[inicial].cor = 0
    nao_coloridos.remove(inicial)

    # Atualiza saturação dos vizinhos
    atualiza_vizinhos(grafo, inicial, 0)

    # Continua enquanto houver vértices não coloridos
    while nao_coloridos:
        # Escolhe o vértice com maior saturação (desempata pelo grau)
        proximo = max(
            nao_coloridos,
            key=lambda v: (saturacao[v], len(grafo.vertices[v].vizinhanca))
        )

        # Determina a menor cor possível que os vizinhos ainda não usam
        cor = menor_cor_possivel(grafo, proximo)

        # Atribui cor
        grafo.vertices[proximo].cor = cor
        nao_coloridos.remove(proximo)

        # Atualiza saturação dos vizinhos do vértice recém-colorido
        atualiza_vizinhos(grafo, proximo, cor)

    print("[DSATUR] Coloração finalizada.")
