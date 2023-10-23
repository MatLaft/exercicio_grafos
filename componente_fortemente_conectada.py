from Graph import Grafo


class ComponenteFortementeConectada(Grafo):
    def __init__(self, arquivo: str = None, vertices: dict[int, str] = [],
                 arestas: list[list[int, int, float]] = []):
        dirigido = True
        super().__init__(arquivo, dirigido, vertices, arestas)
        self.tempo = 0

    def dfs(self):
        C = [False]*self.qtdVertices()
        T = [float('inf')]*self.qtdVertices()
        F = [float('inf')]*self.qtdVertices()
        A = [None]*self.qtdVertices()
        self.tempo = 0

        for vertice in self.vertices:
            if not C[list(self.vertices.keys()).index(vertice)]:
                self.__dfs_visit(vertice, C, T, A, F)
        # print(C, T, A, F)
        return C, T, A, F

    def __dfs_visit(self, vertice:int, C:list, T:list, A:list, F:list):
        C[list(self.vertices.keys()).index(vertice)] = True
        self.tempo = self.tempo + 1
        T[list(self.vertices.keys()).index(vertice)] = self.tempo

        for vertice_vizinho in self.vertices_arestas[vertice]:
            if not C[list(self.vertices.keys()).index(vertice_vizinho)]:
                A[list(self.vertices.keys()).index(vertice_vizinho)] = self.vertices[vertice]
                self.__dfs_visit(vertice_vizinho, C, T, A, F )
        self.tempo = self.tempo + 1
        F[list(self.vertices.keys()).index(vertice)] = self.tempo

    def dfs_modificado(self, F_origin):
        F_sorted = F_origin[:]
        F_sorted.sort(reverse=True)
        C = [False]*self.qtdVertices()
        T = [float('inf')]*self.qtdVertices()
        F = [float('inf')]*self.qtdVertices()
        A = [None]*self.qtdVertices()
        self.tempo = 0

        for tempo in F_sorted:
            index1 = F_origin.index(tempo)
            vertices = list(self.vertices.keys())
            vertice = vertices[(index1)]
            if not C[list(self.vertices.keys()).index(vertice)]:
                self.__dfs_visit(vertice, C, T, A, F)
        # print(C, T, A, F)
        return C, T, A, F

    def get_componentes_fortemente_conectadas(self):
        C, T, A, F = self.dfs()

        At = []
        for aresta in self.arestas:
            At.append([aresta[1], aresta[0], aresta[2]])

        grafo_transposto = ComponenteFortementeConectada(arestas=At, vertices=self.vertices)
        Ct, Tt, At, Ft = grafo_transposto.dfs_modificado(F)

        pilha = []
        componentes = []
        componente_aux = []
        for i in range(1, self.qtdVertices()*2+1):
            if i in Tt:
                pilha.append(self.vertices[list(self.vertices.keys())[Tt.index(i)]])
            elif i in Ft:
                pilha.remove(self.vertices[list(self.vertices.keys())[Ft.index(i)]])
                componente_aux. append(self.vertices[list(self.vertices.keys())[Ft.index(i)]])
            if len(pilha) == 0:
                componentes.append(componente_aux)
                componente_aux = []

        for componente in componentes:
            print(str(componente)[1:-1])




# #
# a = ComponenteFortementeConectada(vertices={0:'a', 1: 'b', 2:'c', 3:'d', 4:'e', 5:'f',6:'g', 7:'h'},
#                                   arestas=[[0,1,1],[1,2,1], [1,4,1], [1,5,1], [2,3,1], [2,6,1], [3,7,1], [3,2,1],
#                                            [4, 0, 1], [4,5,1], [5,6,1], [6,5,1],[6,7,1], [7,7,1]])
# a = ComponenteFortementeConectada(arquivo='fln_pequena.net')
# a = ComponenteFortementeConectada(vertices={1:'1', 2: '2', 3:'3', 4:'4', 5:'5', 6:'6'},
#                                   arestas=[[1,2,1],[2,4,1], [2,5,1], [5,4,1], [4,5,1], [4,1,1], [6,3,1]])
# a.get_componentes_fortemente_conectadas()
