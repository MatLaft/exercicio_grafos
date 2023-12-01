from A3.Graph import Grafo
from operator import itemgetter


class Kruskal(Grafo):
    def __init__(self, arquivo: str = None, vertices: dict[int, str] = [],
                 arestas: list[list[int, int, float]] = []):
        dirigido = False
        super().__init__(arquivo, dirigido, vertices, arestas)

    def get_arvore_geradora_minima_kruskal(self):
        arestas_ordenadas = sorted(self.arestas, key=itemgetter(2))
        conjuntos_vertices = []
        pesos_arvore = 0
        arestas_arvore = []
        for aresta in arestas_ordenadas:
            for conjunto in conjuntos_vertices:
                if aresta[0] in conjunto and aresta[1] in conjunto:
                    break
                elif aresta[0] in conjunto:
                    arestas_arvore.append([self.vertices[aresta[0]], self.vertices[aresta[1]]])
                    for conjunto_para_conectar in conjuntos_vertices:
                        if aresta[1] in conjunto_para_conectar and conjunto_para_conectar != conjunto:
                            conjuntos_vertices[conjuntos_vertices.index(conjunto)] = conjunto.union(
                                conjunto_para_conectar)
                            del conjuntos_vertices[conjuntos_vertices.index(conjunto_para_conectar)]
                            pesos_arvore += aresta[2]
                            break
                    else:
                        conjunto.add(aresta[1])
                        pesos_arvore += aresta[2]
                    break
                elif aresta[1] in conjunto:
                    arestas_arvore.append([self.vertices[aresta[0]], self.vertices[aresta[1]]])
                    for conjunto_para_conectar in conjuntos_vertices:
                        if aresta[0] in conjunto_para_conectar and conjunto_para_conectar != conjunto:
                            conjuntos_vertices[conjuntos_vertices.index(conjunto)] = conjunto.union(conjunto_para_conectar)
                            del conjuntos_vertices[conjuntos_vertices.index(conjunto_para_conectar)]
                            pesos_arvore += aresta[2]
                            break
                    else:
                        conjunto.add(aresta[0])
                        pesos_arvore += aresta[2]
                    break

            else:
                arestas_arvore.append([self.vertices[aresta[0]], self.vertices[aresta[1]]])
                conjuntos_vertices.append({aresta[0], aresta[1]})
                pesos_arvore += aresta[2]

        print(pesos_arvore)
        for aresta in arestas_arvore[:-1]:
            print(f"{aresta[0]}-{aresta[1]}, ", end='')
        print(f"{arestas_arvore[-1][0]}-{arestas_arvore[-1][1]}")



# a = Kruskal(arquivo='fln_pequena.net')
# a = Kruskal(vertices={1:'a', 2:'b', 3:'c',4:'d', 5:'e'}, arestas=[[1,2,3],[1,3,5],[1,4,8],[1,5,9],[2,4,2],[3,5,2],[4,5,1]])
# a = Kruskal(vertices={1:'a', 2:'b', 3:'c',4:'d', 5:'e'}, arestas=[[1,2,10],[1,3,5],[2,4,3],[3,4,8],[3,5,4],[4,5,9]])
# a.get_arvore_geradora_minima_kruskal()