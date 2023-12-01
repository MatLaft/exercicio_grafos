from A3.Graph import Grafo

class CicloEuleriano(Grafo):
    def __init__(self, arquivo: str = None, dirigido: bool = False, vertices: dict[int, str] = [],
                 arestas: list[list[int, int, float]] = []):
        super().__init__(arquivo, dirigido, vertices, arestas)

    def is_euleriano(self):
        for vertice in self.vertices_arestas.keys():
            if len(self.vertices_arestas[vertice].keys()) % 2 != 0:
                return False
        return True

    def get_ciclo_euleriano(self):
        if self.is_euleriano():
            print(1)

            pilha_vertices = []
            pilha_pontas = []
            arestas_visitadas = []
            vertice_atual = list(self.vertices.keys())[0]
            pilha_vertices.append(vertice_atual)

            while len(pilha_vertices) > 0:
                for vertice_destino in self.vertices_arestas[vertice_atual].keys():
                    if f'{vertice_atual},{vertice_destino}' not in arestas_visitadas or  \
                       f'{vertice_destino},{vertice_atual}' not in arestas_visitadas:
                        arestas_visitadas.append(f'{vertice_atual},{vertice_destino}')
                        arestas_visitadas.append(f'{vertice_destino},{vertice_atual}')
                        pilha_vertices.append(vertice_destino)
                        vertice_atual = vertice_destino
                        break
                else:
                    pilha_pontas.append(pilha_vertices[-1])
                    vertice_atual = pilha_vertices.pop(-1)
            print(str(pilha_pontas)[1:-1])

        else:
            print(0)
