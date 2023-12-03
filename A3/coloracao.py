from Graph import Grafo


class Coloracao(Grafo):
    def __init__(self, vertices: dict[int, str]=None,
                 arestas: list[list[int, int, float]]=None, arquivo: str = None):
        dirigido = False
        super().__init__(vertices, arestas, arquivo, dirigido)

    def coloracao_minima(self):
        S = [([0]*self.qtdVertices()) for _ in range(2**self.qtdVertices())]
        for index, binario in enumerate(range(2**self.qtdVertices())):
            for index_bit, bit in enumerate((bin(binario)[:1:-1])):
                S[index][len(S[index])-index_bit-1] = int(bit)
        S = S[::-1]
        R = []
        index = 0
        while True:
            X = S[index]
            if X == [0]*len(X):
                break
            c = True
            conjunto_vetices = [vertice[0] for vertice in zip(self.vertices,X) if vertice[1]]
            for v in conjunto_vetices:
                for u in conjunto_vetices:
                    if v in self.vertices_arestas[u]:
                        c = False
                        break
            if c:
                R.append(X)
            index += 1
        conjuntos_independetes_possibilidades = [[0]*len(R) for _ in range(2**len(R))]
        for index, binario in enumerate(range(2**len(R))):
            for index_bit, bit in enumerate((bin(binario)[:1:-1])):
                conjuntos_independetes_possibilidades[index][len(conjuntos_independetes_possibilidades[index])-index_bit-1] = int(bit)

        conjuntos_possiveis = []

        for possibilidade in conjuntos_independetes_possibilidades:
            conjuntos = [par[0] for par in zip(R, possibilidade) if par[1]]
            if sum([j for i in conjuntos for j in i]) == self.qtdVertices():
                subconjunto_completo = [0]*self.qtdVertices()
                for conjunto in conjuntos:
                    for index,valor in enumerate(conjunto):
                        subconjunto_completo[index] += valor
                if subconjunto_completo.count(1) == self.qtdVertices():
                    conjuntos_possiveis.append(conjuntos)

        tamanhos_minimos = [len(c) for c in conjuntos_possiveis]

        conjuntos_minimos = [conjunto for conjunto in conjuntos_possiveis if len(conjunto) == min(tamanhos_minimos)]
        print("Quantidade minima de cores:", len(conjuntos_minimos))
        conjuntos_minimos_vertices = []
        for conjunto in conjuntos_minimos:
            conjunto_vetices = []
            aux = []
            for j in range(len(conjunto)):
                for i in range(self.qtdVertices()):
                    if conjunto[j][i] == 1:
                        aux.append(list(self.vertices.keys())[i])
                conjunto_vetices.append(aux)
                aux = []
            conjuntos_minimos_vertices.append(conjunto_vetices)
            print("Possibilidade:", conjunto_vetices)
            for index, conjunto_independente in enumerate(conjunto_vetices):
                print({"cor": index+1, "Conjunto independete": conjunto_independente})

        return conjuntos_minimos
