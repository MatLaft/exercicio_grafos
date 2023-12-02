from Graph import Grafo


class HopcroftKarp(Grafo):
    def __init__(self, vertices: dict[int, str] = None, arestas: list[list[int, int, float]] = None,
                 arquivo: str = None):
        dirigido = False
        super().__init__(vertices, arestas, arquivo=arquivo, dirigido=dirigido)

        # Olhando os exemplos, considerei que a primeira metade dos vertices declados pertencem a X e a segunda a Y

        self.X = list(self.vertices.keys())[:len(self.vertices) // 2]
        self.Y = list(self.vertices.keys())[len(self.vertices) // 2:]


    def get_emparelhamento(self):
        D = {vertice: float('inf') for vertice in self.vertices.keys()}
        mate = {vertice: None for vertice in self.vertices.keys()}
        m = 0

        while self.bfs(mate, D):
            for x in self.X:
                if mate[x] is None:
                    if self.dfs(mate, x, D):
                        m += 1
        pares = [[verticeX, mate[verticeX]] for verticeX in self.X if mate[verticeX] is not None]
        print("Emparelhamento maximo:", m)
        print("Arestas do emparelhamento:", pares)
        return m, mate


    def bfs(self,mate, D):
        Q = []
        for x in self. X:
            if mate[x] is None:
                D[x] = 0
                Q.append(x)
            else:
                D[x] = float('inf')

        D[None] = float('inf')

        while len(Q) > 0:
            x = Q.pop(0)
            if D[x] < D[None]:
                for y in self.vizinhos(x):
                    if D[mate[y]] == float('inf'):
                        D[mate[y]] = D[x] + 1
                        Q.append(mate[y])

        return D[None] != float('inf')

    def dfs(self, mate, x, D):
        if x is not None:
            for y in self.vizinhos(x):
                if D[mate[y]] == (D[x] + 1):
                    if self.dfs(mate, mate[y], D):
                        mate[y] = x
                        mate[x] = y
                        return True
            D[x] = float('inf')
            return False
        return True



a = HopcroftKarp(arquivo="emparelhamento_max/gr128_10.net")
print(a.get_emparelhamento())