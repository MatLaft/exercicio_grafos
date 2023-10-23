from componente_fortemente_conectada import ComponenteFortementeConectada


class OrdenacaoTopologica(ComponenteFortementeConectada):
    def __init__(self, arquivo: str = None, vertices: dict[int, str] = [],
                 arestas: list[list[int, int, float]] = []):
        super().__init__(arquivo, vertices, arestas)

    def ordenacao_topolica(self):
        C, T, A, F = self.dfs()
        F_sorted = F[:]
        F_sorted.sort(reverse=True)
        ordem = []
        for tempo in F_sorted:
            index1 = F.index(tempo)
            vertices = list(self.vertices.keys())
            vertice = vertices[(index1)]
            ordem.append(self.vertices[vertice])
        for vertice in ordem[:-1]:
            print(vertice, end='→')
        print(ordem[-1])


# a = OrdenacaoTopologica(vertices={0:'cueca', 1: 'calça', 2:'cinto', 3:'camisa', 4:'gravata', 5:'paleto',6:'meias',
#                                   7:'sapatos', 8:'relogio'},
#                                   arestas=[[0,1,1],[0,7,1],[1,2,1],[1,7,1],[2,5,1],[3,2,1],[3,4,1],[4,5,1],[6,7,1]])
# a = OrdenacaoTopologica(arquivo='fln_pequena.net')
# a = OrdenacaoTopologica(vertices={1:'1', 2: '2', 3:'3', 4:'4', 5:'5', 6:'6'},
#                                   arestas=[[1,2,1],[2,4,1], [2,5,1], [5,4,1], [4,5,1], [4,1,1], [6,3,1]])
a = OrdenacaoTopologica(vertices={0:'0', 1: '1', 2:'2', 3:'3', 4:'4', 5:'5',6:'6',7:'7'},
                                  arestas=[[0,3,1],[0,4,1],[3,4,1],[3,5,1],[5,7,1],[4,5,1],[5,7,1],[2,0,1],
                                           [2,1,1],[2,5,1],[2,6,1],[1,4,1]])

a.ordenacao_topolica()
