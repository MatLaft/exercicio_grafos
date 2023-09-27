from exercise_1 import Grafo

class FloydWarshall(Grafo):
    def __init__(self, arquivo: str = None, dirigido: bool = False, vertices: dict[int, str] = [], arestas: list[list[int, int, float]] = []):
        super().__init__(arquivo, dirigido, vertices, arestas)

    def floyd_warshall(self):
        matriz = [[float('inf')]*len(self.vertices) for _ in range(len(self.vertices))]

        for index_origem, origem in enumerate(self.vertices.keys()):
            for index_destino, destino in enumerate(self.vertices.keys()):
                if index_origem == index_destino:
                    matriz[index_origem][index_destino] = 0
                else:
                    matriz[index_origem][index_destino] = self.vertices_arestas.get(origem).get(destino, float('inf'))

        for iteracao in range(len(self.vertices)):
            for origem in range(len(self.vertices)):
                for destino in range(len(self.vertices)):
                    if matriz[origem][destino] > matriz[origem][iteracao] + matriz[iteracao][destino]:
                        matriz[origem][destino] = matriz[origem][iteracao] + matriz[iteracao][destino]

        for index, distancias in enumerate(matriz):
            # index(rotulo): Distancias
            print(f"{list(self.vertices.keys())[index]}({self.vertices[list(self.vertices.keys())[index]]}): {str(distancias)[1:-1].replace(' ','')}")



# a = FloydWarshall(dirigido=True, vertices={0:0,1:1,2:2,3:3,4:4,5:5}, arestas=[[0,1,5],[0,3,1],[1,5,1],[1,4,1],[1,2,3],[2,3,1],[2,4,1],[5,2,1]])
# a = FloydWarshall(dirigido=True, arquivo='polbooks.net')
# a.floyd_warshall()
