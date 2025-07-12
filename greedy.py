
def coloring(grafo):
    print("[Greedy] Coloração iniciada...")
    grafo.resetar_cores()

    disponibilidadeCor = [-1 for i in range(1, grafo.n + 1)]

    grafo.vertices[1].cor = 1
    for i in range(2, grafo.n + 1):

        for v in grafo.vertices[i].vizinhanca:
            if (grafo.vertices[v].cor is not None):
                disponibilidadeCor[grafo.vertices[v].cor] = 1

        cor = 1

        while cor < grafo.n + 1:
            if (disponibilidadeCor[cor] == -1):
                break
            cor += 1

        grafo.vertices[i].cor = cor

        for v in grafo.vertices[i].vizinhanca:
            if (grafo.vertices[v].cor is not None):
                disponibilidadeCor[grafo.vertices[v].cor] = -1

    print("[Greedy] Coloração finalizada.")
