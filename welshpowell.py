def coloring(grafo):
    print("[Welsh-Powell] Coloração iniciada...")
    grafo.resetar_cores()

    verticesOrdGraus = sorted(range(1, grafo.n + 1), key=lambda v: -len(grafo.vertices[v].vizinhanca))

    cor = 1
    qtd_vertices_coloridos = 0
    while qtd_vertices_coloridos < grafo.n:
        for index, vertice in enumerate(verticesOrdGraus):
            if all([grafo.vertices[vizinho].cor != cor for vizinho in grafo.vertices[vertice].vizinhanca]):
                grafo.vertices[vertice].cor = cor
                verticesOrdGraus.pop(index)
                qtd_vertices_coloridos += 1
        cor += 1

    print("[Welsh-Powell] Coloração finalizada.")
