class Grafo:
  def __init__(self, n):
    self.n = n
    self.vizinhancas = [[] for i in range(n)]
