from collections import defaultdict


class Vertice:
    def __init__(self, nome: int):
        self.nome = nome
        self.cor = None
        self.vizinhanca = list()

    def __str__(self):
        return f"Vértice {self.nome} - Cor: {self.cor}"


class Grafo:
    def __init__(self, qtd_vertices: int):
        self.n = qtd_vertices
        self.vertices = {v: Vertice(v) for v in range(1, qtd_vertices+1)}
        self.arestas = defaultdict(list)

    def add_aresta(self, v1: int, v2: int):
        self.vertices[v1].vizinhanca.append(v2)
        self.vertices[v2].vizinhanca.append(v1)
        self.arestas[v1].append(v2)
        self.arestas[v2].append(v1)

    def mostrar_grafo(self):
        print("\n--- GRAFO ---")
        for v in self.vertices.values():
            vizinhos = ', '.join(str(viz) for viz in v.vizinhanca)
            print(f"Vértice {v.nome} -> Vizinhos: [{vizinhos}] | Cor: {v.cor}")

    def resetar_cores(self):
        for v in self.vertices.values():
            v.cor = None

    def greedy_coloring(self):
        print("[Greedy] Coloração iniciada...")
        return

    def dsatur_coloring(self):
        print("[DSatur] Coloração iniciada...")
        return
