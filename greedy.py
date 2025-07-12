
def coloring(grafo):
    print("[Greedy] Coloração iniciada...")

    disponibilidadeCor = [-1 for i in range(0, grafo.n + 1)]

    grafo.vertices[1].cor = 0
    for i in range(2, grafo.n + 1):

        for v in grafo.vertices[i].vizinhanca:
            if (grafo.vertices[v].cor is not None):
                disponibilidadeCor[grafo.vertices[v].cor] = 1

        cor = 0

        while cor < grafo.n:
            if (disponibilidadeCor[cor] == -1):
                break
            cor += 1

        grafo.vertices[v].cor = cor

        for v in grafo.vertices[i].vizinhanca:
            if (grafo.vertices[v].cor is not None):
                disponibilidadeCor[grafo.vertices[v].cor] = -1

    print("[Greedy] Coloração finalizada.")
