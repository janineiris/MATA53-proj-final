from grafo import Grafo


def menu():
    grafo = None

    while True:
        print("\n--- MENU ---")
        print("1. Criar novo grafo")
        print("2. Adicionar aresta")
        print("3. Mostrar grafo")
        print("4. Rodar coloração GREEDY")
        print("5. Rodar coloração DSATUR")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            n = int(input("Quantidade de vértices: "))
            grafo = Grafo(n)
            print(f"Grafo com {n} vértices criado.")
        elif opcao == '2':
            if grafo is None:
                print("Crie um grafo primeiro.")
                continue
            v1 = int(input("Vértice 1: "))
            v2 = int(input("Vértice 2: "))
            if valida_arestas(grafo, v1, v2):
                grafo.add_aresta(v1, v2)
                print(f"Aresta {v1}-{v2} inserida com sucesso")
        elif opcao == '3':
            if grafo is None:
                print("Crie um grafo primeiro.")
                continue
            grafo.mostrar_grafo()
        elif opcao == '4':
            if grafo is None:
                print("Crie um grafo primeiro.")
                continue
            grafo.greedy_coloring()
        elif opcao == '5':
            if grafo is None:
                print("Crie um grafo primeiro.")
                continue
            grafo.dsatur_coloring()
        elif opcao == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


def valida_arestas(grafo, v1, v2):
    if v1 > grafo.n or v1 <= 0:
        print("ERRO: Primeiro vértice informado é inválido")
        return False
    if v2 > grafo.n or v2 <= 0:
        print("ERRO: Segundo vértice informado é inválido")
        return False
    if v1 == v2:
        print("ERRO: Aresta inválida")
        return False
    if v2 in grafo.vertices[v1].vizinhanca:
        print("ERRO: Aresta já existe")
        return False

    return True


if __name__ == "__main__":
    menu()
