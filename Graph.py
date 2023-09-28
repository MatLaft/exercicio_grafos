import re

class Grafo:
    def __init__(self, arquivo: str = None, dirigido: bool = False, vertices: dict[int, str] = [],
                 arestas: list[list[int, int, float]] = []):
        if arquivo:
            vertices = {}
            arestas = []
            with open(arquivo, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    line = line.strip()

                    if line.startswith("*"):
                        current_section = line
                        continue

                    if "*vertices" in current_section:
                        parts = line.split(None, 1)
                        if len(parts) == 2:
                            vertice_index, vertice_name = parts
                            vertices[int(vertice_index)] = vertice_name.strip('""')

                    elif current_section == "*edges":
                        edge_info = line.split()
                        if len(edge_info) == 3:
                            aresta = [int(edge_info[0]), int(edge_info[1]), float(edge_info[2])]
                            arestas.append(aresta)

        self.dirigido = dirigido
        self.vertices_arestas: dict[int, dict] = {}
        self.arestas = arestas
        self.vertices = vertices

        for vertice in vertices.keys():
            self.vertices_arestas[vertice] = {}
        for aresta in arestas:
            self.vertices_arestas[aresta[0]][aresta[1]] = aresta[2]
            if not self.dirigido:
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