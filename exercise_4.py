from exercise_1 import Grafo

class BellmanFord(Grafo):
    def __init__(self, arquivo: str = None, vertices: dict[int, str] = [], arestas: list[list[int, int, float]] = []):
        super().__init__(arquivo, vertices, arestas)

    def bellman_ford_search(self, origem):
        #Como meu grafo nao é orientado, caso houver alguma aresta com peso negativo, já existe um ciclo negativo logo:
        for aresta in self.arestas:
            if aresta[2] < 0:
                print('há ciclo negativos pois o grafo é não dirigido com aresta negativa')
                return False

        vertice_distancia: dict[int, list] = {}

        for vertice in self.vertices:
            vertice_distancia[vertice] = [float('inf'), None]
        vertice_distancia[origem] = [0, -1]  # (-1) representa que ele é a origem

        for iteracao in range(len(self.vertices) - 1):
            for vertice in self.vertices:
                if vertice_distancia[vertice][0] != float('inf'):
                    for aresta in self.vertices_arestas[vertice]:
                        if vertice_distancia[aresta][0] > vertice_distancia[vertice][0] + self.vertices_arestas[vertice][aresta]:
                            vertice_distancia[aresta][0] = vertice_distancia[vertice][0] + self.vertices_arestas[vertice][aresta]
                            vertice_distancia[aresta][1] = vertice
        for vertice in vertice_distancia:
            string = str(vertice)
            pivot = vertice
            while str(origem) not in string:
                string = str(vertice_distancia[pivot][1]) + ',' + string
                pivot = vertice_distancia[pivot][1]
            print(f'{vertice}: {string}; d={vertice_distancia[vertice][0]}')


# a = BellmanFord(vertices={0:0,1:1,2:2,3:3,4:4,5:5}, arestas=[[0,1,5],[0,3,1],[1,5,1],[1,4,1],[1,2,3],[2,3,1],[2,4,1],[5,2,1]])
# print(a.vertices_arestas)
# a.bellman_ford_search(0)