class Grafo:
    def __init__(self, arquivo: str = None, vertices: dict[int, str] = [], arestas: list[list[int, int, float]] = []):
        if arquivo:
            vertices = {}
            arestas = []
            with open(arquivo, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    if line.strip().startswith('*vertices'):
                        continue  # Skip the line starting with '*vertices'
                    if line.strip().startswith('*edges'):
                        continue  # Skip the line starting with '*vertices'
                    values = line.strip().split()

                    if len(values) == 2:
                        vertices[int(values[0])] = int(values[1])

                    if len(values) == 3:
                        aresta = [int(values[0]), int(values[1]), float(values[2])]
                        arestas.append(aresta)

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
        peso = self.vertices_arestas[aresta[0]]. get(aresta[1])
        return peso if peso else float('inf')


# a = Grafo('polbooks.net')
# print(a.vertices_arestas)
# print(a.qtdVertices())
# print(a.qtdArestas())
# print(a.grau(2))
# print(a.rotulo(1))
# print(a.vizinhos(1))
# print(a.haAresta([2,3]))
# print(a.peso([20,2]))