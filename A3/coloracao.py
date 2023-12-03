from Graph import Grafo


class Coloracao(Grafo):
    def __init__(self, vertices: dict[int, str]=None,
                 arestas: list[list[int, int, float]]=None, arquivo: str = None):
        dirigido = False
        super().__init__(vertices, arestas, arquivo, dirigido)

    def soma_binaria_restrita(self, casas_validas: list, soma_valor_decimal):
        soma_binario = [int(i) for i in list((bin(soma_valor_decimal)[2:]))]
        index_validos = [i for i, j in enumerate(casas_validas) if j]
        soma = [0]*len(casas_validas)
        for _ in range(soma_valor_decimal):
            index_para_somar = -1
            soma[index_validos[index_para_somar]] += 1
            while 2 in soma:
                soma[index_validos[index_para_somar]] = 0
                index_para_somar -= 1
                soma[index_validos[index_para_somar]] += 1
        return soma



    def conjuntos_independetes_maximais(self):
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
                #Remover todos subconjuntos de X de S
                possibilidades = 2**sum(X)
                for possibilidade in range(1, possibilidades-1):
                    a = self.soma_binaria_restrita(X, possibilidade)
                    if a in S:
                        S.remove(a)

            index += 1

        print(R)
        return R





a = Coloracao(arquivo="fluxo_teste/cor3.net")
a.conjuntos_independetes_maximais()
# a.soma_binaria_restrita([1,0,0,1,1,0,1], 8)
# for i in range(8):
#     a.soma_binaria_restrita([0,1,0,0,1,1], i)