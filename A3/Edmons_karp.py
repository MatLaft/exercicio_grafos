from Graph import Grafo

class RedeResidual(Grafo):
    def __init__(self, arquivo: str = None, vertices: dict[int, str] = [],
                 arestas: list[list[int, int, float]] = []):
        dirigido = True
        super().__init__(arquivo, dirigido, vertices, arestas)

        self.__aresta_residuais = [[aresta[1], aresta[0], aresta[2]] for aresta in self.arestas]

        for aresta in self.__aresta_residuais:
            if (self.vertices_arestas[aresta[0]].get(aresta[1])) is None:
                self.vertices_arestas[aresta[0]][aresta[1]] = 0

        self.arestas = [*self.arestas, *self.__aresta_residuais]
        # print(self.vertices_arestas)

class EdmonsKarp(Grafo):
    def __init__(self, arquivo: str = None, vertices: dict[int, str] = [],
                 arestas: list[list[int, int, float]] = []):
        dirigido = True
        super().__init__(arquivo, dirigido, vertices, arestas)
        self.grafo_residural = RedeResidual(arquivo, vertices, arestas)

    def __busca_em_largura_edmons_karp(self, fonte, destino):
        C = [False for vertice in self.vertices]
        A = [None for vertice in self.vertices]
        C[self.get_index(fonte)] = True

        Q = []
        Q.append(fonte)
        while len(Q) > 0:
            u = Q.pop(0)
            for v in self.grafo_residural.vizinhos(u):
                if C[self.grafo_residural.get_index(v)] is False and self.grafo_residural.peso([u, v])>0:
                    C[self.grafo_residural.get_index(v)] = True
                    A[self.grafo_residural.get_index(v)] = u
                    if v == destino:
                        p = [destino]
                        w = destino
                        while w != fonte:
                            w = A[self.grafo_residural.get_index(w)]
                            p.insert(0, w)
                        # print(p)
                        return p
                    Q.append(v)
        return None

    def get_fluxo_maximo(self, fonte, destino):
        F = 0
        caminho_aumentante = self.__busca_em_largura_edmons_karp(fonte, destino)
        while caminho_aumentante is not None:
            arestas_do_caminho = [[caminho_aumentante[i], caminho_aumentante[i + 1]]
                                  for i in range(len(caminho_aumentante) - 1)]
            # Calculo de Fp
            Fp = min(self.grafo_residural.peso(aresta) for aresta in arestas_do_caminho)

            print(Fp, [[self.rotulo(vertice[0]),self.rotulo(vertice[1])] for vertice in arestas_do_caminho],
                  [self.grafo_residural.peso(aresta) for aresta in arestas_do_caminho])

            F += Fp

            # Atualizando a capacidade residual
            for aresta in arestas_do_caminho:
                self.grafo_residural.vertices_arestas[aresta[0]][aresta[1]] -= Fp
                self.grafo_residural.vertices_arestas[aresta[1]][aresta[0]] += Fp

            caminho_aumentante = self.__busca_em_largura_edmons_karp(fonte, destino)
        print(F)
        return F








a = EdmonsKarp(arquivo="fluxo_teste/fluxo_prova.net")
# print(a.arestas)
# print(a.peso([1,2]))
a.get_fluxo_maximo(1, 10)
