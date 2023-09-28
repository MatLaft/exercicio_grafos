from Graph import Grafo

class BellmanFord(Grafo):
    def __init__(self, arquivo: str = None, dirigido: bool = False, vertices: dict[int, str] = [],
                 arestas: list[list[int, int, float]] = []):
        super().__init__(arquivo, dirigido, vertices, arestas)

    def bellman_ford_search(self, origem):
        vertice_distancia: dict[int, list] = {}

        for vertice in self.vertices:
            vertice_distancia[vertice] = [float('inf'), None]
        vertice_distancia[origem] = [0, -1]  # (-1) representa que ele é a origem

        for iteracao in range(len(self.vertices)+1):
            for vertice in self.vertices:
                if vertice_distancia[vertice][0] != float('inf'):
                    for aresta in self.vertices_arestas[vertice]:
                        if vertice_distancia[aresta][0] > vertice_distancia[vertice][0] + self.vertices_arestas[vertice][aresta]:
                            vertice_distancia[aresta][0] = vertice_distancia[vertice][0] + self.vertices_arestas[vertice][aresta]
                            vertice_distancia[aresta][1] = vertice
                            if iteracao == len(self.vertices):
                                print("Há ciclo negativo")
                                return 0

        for vertice in vertice_distancia:
            string = str(vertice)
            pivot = vertice
            while str(origem) not in string:
                string = str(vertice_distancia[pivot][1]) + ',' + string
                pivot = vertice_distancia[pivot][1]
                if pivot is None:
                    string = 'inf'
                    break
            print(f'{vertice}: {string}; d={vertice_distancia[vertice][0]}')
