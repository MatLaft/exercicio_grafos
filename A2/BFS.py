from A3.Graph import Grafo


class GrafoBuscaLargura(Grafo):
    def __init__(self, arquivo: str = None, dirigido: bool = False, vertices: dict[int, str] = [],
                 arestas: list[list[int, int, float]] = []):
        super().__init__(arquivo, dirigido, vertices, arestas)

    def busca_em_largura(self, vert):
        if not self.vertices.get(vert):
            print("Vertice não incluso no grafo")
            return

        conhecidos = [vert]
        ordem = {}
        fila = [[vert, vert]]
        while len(fila) > 0:
            i = fila[0][0]
            ancestral = fila[0][1]
            fila.pop(0)
            for j in ordem:
                if ancestral in ordem[j]:
                    if ordem.get(j+1):
                        ordem[j+1].append(i)
                    else:
                        ordem[j+1] = [i]
                    break
            else:
                ordem[len(ordem)] = [i]

            for vertice in self.vertices_arestas[i].keys():
                if vertice not in conhecidos:
                    conhecidos.append(vertice)
                    fila.append([vertice, i])

        for visita in ordem:
            print(f'{visita}: {str(list(ordem[visita]))[1:-1].replace(" ","")}')
