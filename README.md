# Projeto de Coloração de Grafos

Este projeto implementa algoritmos de coloração de grafos, com funcionalidades para criar grafos, adicionar arestas e executar diferentes heurísticas de coloração.

--- 

## Equipe
Este projeto foi feito para a disciplina Teoria dos Grafos.
Os membros da equipe são:
- Ian Ramos Santos Reis
- Iris Janine dos Santos Nogueira
- Rafael Correa Nagy
- Raphael Matos Costa

---

## Requisitos

- Python 3.12 ou superior
- Bibliotecas usadas:  
  - `matplotlib`  
  - `networkx`

Instale as bibliotecas que não vierem com o Python com o comando:

```bash
pip install matplotlib networkx
```

---

## Como usar

### CLI interativo

Você pode usar o CLI para criar grafos, adicionar arestas e rodar os algoritmos de coloração.

Execute:

```bash
    python cli.py
```


No menu, escolha as opções para:

1. Criar grafo
2. Adicionar arestas
3. Mostrar o grafo (visualização gráfica se o grafo tiver até 1000 vértices)
4. Executar a coloração: GREEDY
5. Executar a coloração: DSATUR
6. Executar a coloração: WELSH-POWELL
0. Sair do programa

---

### Testes com medição de tempo

O arquivo `test.py` permite rodar os algoritmos automaticamente em grafos gerados aleatoriamente ou carregados de arquivo.

**Parâmetros:**

* `--mostrar true` : exibe visualização do grafo
* `--arquivo <caminho>` : arquivo contendo grafo (primeira linha: número de vértices; linhas seguintes: pares de vértices das arestas)
* `--vertices <n>` : número de vértices para grafo aleatório
* `--arestas <m>` : número de arestas para grafo aleatório

Exemplo para carregar grafo de arquivo e rodar os testes:

```bash
python test.py --arquivo entrada/petersen.txt --mostrar true
```
Adicionamos alguns grafos na pasta `entrada/`

Exemplo para gerar grafo aleatório e rodar os testes:

```bash
python test.py --vertices 50 --arestas 100 --mostrar true
```
