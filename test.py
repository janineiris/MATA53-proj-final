import argparse
import random
from time import time

from grafo import Grafo
from utils import visualizar_grafo_com_cores, visualizar_grafo_pequeno


def gerar_grafo_aleatorio(n_vertices: int, n_arestas: int) -> Grafo:
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


def gerar_k_grafo(n_vertices: int) -> Grafo:
    grafo = Grafo(n_vertices)

    for u in range(1, n_vertices):
        for v in range(u + 1, n_vertices + 1):
            grafo.add_aresta(u, v)

    return grafo


def gerar_grafo_arquivo(arquivo: str) -> Grafo:
    with open(arquivo, "r") as file:
        lines = file.readlines()
        n_vertices = int(lines[0])
        grafo = Grafo(n_vertices)

        for line in lines[1:]:
            u, v = [int(i) for i in line.split(" ")]
            grafo.add_aresta(u, v)

    return grafo


def conta_cores(grafo):
    cores_utilizadas = set()

    for vertice in grafo.vertices.values():
        assert vertice.cor is not None
        assert not any(
            vertice.cor == grafo.vertices[vizinho].cor for vizinho in vertice.vizinhanca
        )
        cores_utilizadas.add(vertice.cor)

    return cores_utilizadas


def cria_grafo(
    n_vertices: int, n_arestas: int, mostrar_grafo: bool, arquivo: str
) -> Grafo:
    inicio = time()

    if arquivo:
        print(f"Gerando grafo a partir de arquivo {arquivo}...")
        grafo = gerar_grafo_arquivo(arquivo)
    else:
        maximo_arestas = int(n_vertices * (n_vertices - 1) / 2)

        if n_arestas > maximo_arestas:
            print(
                f"A quantidade máxima de arestas para um grafo de {n_vertices} vértices é {maximo_arestas} arestas, iremos gerar um grafo com {maximo_arestas} arestas."
            )

        n_arestas = min(n_arestas, maximo_arestas)

        if n_arestas == maximo_arestas:
            print(f"Gerando k-grafo com {n_vertices} vértices e {n_arestas} arestas...")

            grafo = gerar_k_grafo(n_vertices)
        else:
            print(
                f"Gerando grafo com {n_vertices} vértices e {n_arestas} arestas aleatórias..."
            )

            grafo = gerar_grafo_aleatorio(n_vertices, n_arestas)
    fim = time()

    print(f"Grafo gerado em {fim - inicio:.10f} segundos.")

    if mostrar_grafo:
        visualizar_grafo_pequeno(grafo)

    print()
    return grafo


def run_test(grafo: Grafo, mostrar_grafo: bool):
    print("Fazendo coloração por método Greedy Coloring.")

    inicio = time()
    grafo.greedy_coloring()
    fim = time()

    cores_utilizadas = conta_cores(grafo)
    greedy = len(cores_utilizadas)
    print(f"Tempo utilizado: {fim - inicio:.10f} segundos")
    print(f"Cores utilizadas: {len(cores_utilizadas)} -> {cores_utilizadas}")

    if mostrar_grafo:
        visualizar_grafo_com_cores(grafo)

    print()

    print("Fazendo coloração por método DSatur Coloring.")

    inicio = time()
    grafo.dsatur_coloring()
    fim = time()

    cores_utilizadas = conta_cores(grafo)
    dsatur = len(cores_utilizadas)
    print(f"Tempo utilizado: {fim - inicio:.10f} segundos")
    print(f"Cores utilizadas: {len(cores_utilizadas)} -> {cores_utilizadas}")

    if mostrar_grafo:
        visualizar_grafo_com_cores(grafo)

    print()
    return greedy, dsatur, grafo


def main():
    parser = argparse.ArgumentParser(description="Geração de grafos gigantes.")
    parser.add_argument("--vertices", type=int, help="Número de vértices")
    parser.add_argument("--arestas", type=int, help="Número de arestas")
    parser.add_argument("--mostrar", type=bool, default=False, help="Mostrar grafo")
    parser.add_argument("--arquivo", type=str, default="", help="Arquivo com grafo")
    args = parser.parse_args()

    grafo = cria_grafo(args.vertices, args.arestas, args.mostrar, args.arquivo)
    run_test(grafo, args.mostrar)


if __name__ == "__main__":
    main()
