class Grafo:
    def __init__(self, arquivo: str = None, vertices: dict[int, str] = [], arestas: list[list[int, int, float]] = []):
        self.vertices_arestas: dict[int, dict] = {}
        self.arestas = arestas
        self.vertices = vertices

        for vertice in vertices.keys():
            self.vertices_arestas[vertice] = {}
        for aresta in arestas:
            self.vertices_arestas[aresta[0]][aresta[1]] = aresta[2]
            self.vertices_arestas[aresta[1]][aresta[0]] = aresta[2]

    def qtdVertices(self):
        return len(self.vertices)

    def qtdArestas(self):
        return len(self.arestas)

    def grau(self, vertice: int):
        return len(self.vertices_arestas[vertice].values())

    def rotulo(self, vertice):
        return self.vertices[vertice]

    def vizinhos(self, vertice):
        return list(self.vertices_arestas[vertice].keys())

    def haAresta(self, aresta: list[int, int]):
        return self.vertices_arestas[aresta[0]].get(aresta[1]) is not None

    def peso(self, aresta):
        return self.vertices_arestas[aresta[0]][aresta[1]]



a = Grafo({1: 'A',  2: 'B',  3: 'C'}, [[1, 2, 10], [3, 2, 20]])
print(a.qtdVertices())
print(a.qtdArestas())
print(a.grau(2))
print(a.rotulo(1))
print(a.vizinhos(1))
print(a.haAresta([2,3]))
print(a.peso([1,2]))