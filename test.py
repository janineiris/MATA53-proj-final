import argparse
import random
from time import time

from grafo import Grafo
from utils import visualizar_grafo_com_cores, visualizar_grafo_pequeno


def gerar_grafo_gigante(n_vertices: int, n_arestas: int) -> Grafo:
    grafo = Grafo(n_vertices)
    arestas_adicionadas = set()

    while len(arestas_adicionadas) < n_arestas:
        u = random.randint(1, n_vertices)
        v = random.randint(1, n_vertices)

        if u == v:
            continue

        aresta = tuple(sorted((u, v)))

        if aresta in arestas_adicionadas:
            continue

        grafo.add_aresta(u, v)
        arestas_adicionadas.add(aresta)

    return grafo


def main():
    parser = argparse.ArgumentParser(description="Geração de grafos gigantes.")
    parser.add_argument("--vertices", type=int, help="Número de vértices")
    parser.add_argument("--arestas", type=int, help="Número de arestas")
    args = parser.parse_args()

    run_test(args.vertices, args.arestas)


def run_test(n_vertices, n_arestas):
    print(f"Gerando grafo com {n_vertices} vértices e {n_arestas} arestas...")

    inicio = time()
    grafo = gerar_grafo_gigante(n_vertices, n_arestas)
    fim = time()

    print(f"Grafo gerado em {fim - inicio:.5f} segundos.")

    if n_vertices <= 1000:
        visualizar_grafo_pequeno(grafo)

    print()

    print("Fazendo coloração por método Greedy Coloring.")

    inicio = time()
    grafo.greedy_coloring()
    fim = time()

    cores_utilizadas = set()

    for vertice in grafo.vertices.values():
        assert vertice.cor is not None
        assert not any(
            vertice.cor == grafo.vertices[vizinho].cor for vizinho in vertice.vizinhanca
        )
        cores_utilizadas.add(vertice.cor)

    print(f"Tempo utilizado: {fim - inicio:.5f} segundos")
    print(f"Cores utilizadas: {len(cores_utilizadas)} -> {cores_utilizadas}")

    if n_vertices <= 1000:
        visualizar_grafo_com_cores(grafo)

    print()

    print("Fazendo coloração por método DSatur Coloring.")

    inicio = time()
    grafo.dsatur_coloring()
    fim = time()

    cores_utilizadas = set()

    for vertice in grafo.vertices.values():
        assert vertice.cor is not None
        assert not any(
            vertice.cor == grafo.vertices[vizinho].cor for vizinho in vertice.vizinhanca
        )
        cores_utilizadas.add(vertice.cor)

    print(f"Tempo utilizado: {fim - inicio:.5f} segundos")
    print(f"Cores utilizadas: {len(cores_utilizadas)} -> {cores_utilizadas}")

    if n_vertices <= 1000:
        visualizar_grafo_com_cores(grafo)

    print()


if __name__ == "__main__":
    main()
