import networkx as nx
import matplotlib.pyplot as plt


def visualizar_grafo_pequeno(grafo_custom):
    G = nx.Graph()

    for v in grafo_custom.vertices:
        G.add_node(v)

    for v in grafo_custom.arestas:
        for u in grafo_custom.arestas[v]:
            G.add_edge(v, u)

    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_size=30, font_size=6)
    plt.show()


def visualizar_grafo_com_cores(grafo_custom):
    G = nx.Graph()

    # Adiciona nós e arestas
    for v in grafo_custom.vertices:
        G.add_node(v)

    for v, vizinhos in grafo_custom.arestas.items():
        for u in vizinhos:
            if v < u:
                G.add_edge(v, u)

    # Extrai cores dos vértices
    cores = []
    for v in G.nodes:
        cor = grafo_custom.vertices[v].cor
        cores.append(cor if cor is not None else -1)  # usa -1 para "sem cor"

    # Normaliza cores para matplotlib (ex: 0 = azul, 1 = laranja, etc)
    cmap = plt.cm.get_cmap('tab20')  # até 20 cores distintas
    norm_cores = [(c if c >= 0 else 0) for c in cores]  # evita erro com None

    # Layout automático
    pos = nx.spring_layout(G, seed=42)

    # Desenha
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color=norm_cores,
        node_size=100,
        cmap=cmap,
        font_size=6
    )
    plt.title("Grafo com coloração dos vértices")
    plt.show()
