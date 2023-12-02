from Graph import Grafo


class Coloracao(Grafo):
    def __init__(self, vertices: dict[int, str]=None,
                 arestas: list[list[int, int, float]]=None, arquivo: str = None):
        dirigido = False
        super().__init__(vertices, arestas, arquivo, dirigido)


    def get_colocacao(self):
        S = [([0]*self.qtdVertices()) for _ in range(2**self.qtdVertices())]
        for index, binario in enumerate(range(2**self.qtdVertices())):
            for index_bit, bit in enumerate((bin(binario)[:1:-1])):
                S[index][len(S[index])-index_bit-1] = int(bit)





a = Coloracao(arquivo="fluxo_teste/cor3.net")
a.get_colocacao()