from exercise_1 import Grafo

class CicloEuleriano(Grafo):
    def __init__(self, arquivo: str = None, vertices: dict[int, str] = [], arestas: list[list[int, int, float]] = []):
        super().__init__(arquivo, vertices, arestas)

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

# a = CicloEuleriano('polbooks.net')
# a = CicloEuleriano(vertices={0:0,1:1,2:2,3:3,4:4,5:5}, arestas=[[0,1,1],[0,3,1],[1,5,1],[1,4,1],[1,2,1],[2,3,1],[2,4,1],[5,2,1]])
# print(a.vertices_arestas)
# a.get_ciclo_euleriano()