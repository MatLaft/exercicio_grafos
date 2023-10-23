from componente_fortemente_conectada import ComponenteFortementeConectada
from ordenacao_topologica import OrdenacaoTopologica
from kruskal import Kruskal


while True:
    print("Selecione um exercicio para testar")
    print("1- Componentes Fortemente Conexas")
    print("2- Ordenacao Topologica")
    print("3- Kruskal")
    print("0- Sair")
    valor_selecionado = None
    while valor_selecionado is None:
        valor_selecionado = input("Exercício: ")
        if valor_selecionado not in ['1', '2', '3', '0']:
            print("Valor inválido")
            valor_selecionado = None
    if valor_selecionado == '0':
        break

    print("Escolha como inserir seu grafo")
    print("1- Inserir um arquivo(deixar na mesma pasta que esse arquivo)")
    print("2- Criar um grafo manualmente")
    modo_construcao_grafo = None
    while modo_construcao_grafo is None:
        modo_construcao_grafo = input("Escolha: ")
        if modo_construcao_grafo not in ['1', '2']:
            print("Valor inválido")
            modo_construcao_grafo = None

    if valor_selecionado == '1':
        if modo_construcao_grafo == '1':
            while True:
                try:
                    nome_arquivo = input('Digite o nome do arquivo: ')
                    exe1 = ComponenteFortementeConectada(arquivo= nome_arquivo)
                    break
                except Exception as error:
                    print("Falha ao ler arquivo, digite novamente!")
                    print(error)
        else:
            vertices = {}
            arestas = []
            while True:
                quantidade_vertices = input("Digite o quantidade de vertices: ")
                try:
                    print("Digite o index do vertice e seu rótulo(sem espaços) no formato: index rótulo")
                    for _ in range(int(quantidade_vertices)):
                        while True:
                            index, rotulo = input("Vertice: ").split(' ')
                            try:
                                if int(index) in vertices.keys():
                                    print("Vertice inserido previamente")
                                    raise Exception
                                vertices[int(index)] = rotulo
                                break
                            except:
                                print("Valor invalido")
                    else:
                        break
                except:
                    print("Valor inválido")
            while True:
                quantidade_arestas = input("Digite o quantidade de arestas: ")
                try:
                    print("Digite o par de vertice e seu peso no formato: index_vertice1 index_vertice2")
                    for _ in range(int(quantidade_arestas)):
                        while True:
                            vertice1,vertice2 = input("Aresta: ").split(' ')
                            try:
                                if int(vertice2) not in vertices.keys() or int(vertice1) not in vertices.keys():
                                    print("Aresta com vertice inexistente")
                                    print('Vertices(index,rotulo):', vertices)
                                    raise Exception
                                for aresta in arestas:
                                    if int(vertice1) == aresta[0] and int(vertice2) == aresta[1]:
                                        print("Aresta ja inserida")
                                        print(f'Arestas:{[[i[0],i[1]] for i in arestas]}')
                                        raise Exception
                                arestas.append([int(vertice1), int(vertice2), 1])
                                break
                            except:
                                print("Valor invalido")
                    else:
                        break
                except:
                    print("Valor inválido")
            exe1 = ComponenteFortementeConectada(vertices=vertices, arestas=arestas)
            print("Grafo criado!")
            print('Vertices(index,rotulo):', vertices)
            print(f'Arestas:{[[i[0], i[1]] for i in arestas]}')
        print("#"*30)
        print("Saida do exercicio:")
        exe1.get_componentes_fortemente_conectadas()
        print("#"*30)

    if valor_selecionado == '2':
        if modo_construcao_grafo == '1':
            while True:
                try:
                    nome_arquivo = input('Digite o nome do arquivo: ')
                    exe2 = OrdenacaoTopologica(arquivo= nome_arquivo)
                    break
                except Exception as error:
                    print("Falha ao ler arquivo, digite novamente!")
                    print(error)
        else:
            vertices = {}
            arestas = []
            while True:
                quantidade_vertices = input("Digite o quantidade de vertices: ")
                try:
                    print("Digite o index do vertice e seu rótulo(sem espaços) no formato: index rótulo")
                    for _ in range(int(quantidade_vertices)):
                        while True:
                            index, rotulo = input("Vertice: ").split(' ')
                            try:
                                if int(index) in vertices.keys():
                                    print("Vertice inserido previamente")
                                    raise Exception
                                vertices[int(index)] = rotulo
                                break
                            except:
                                print("Valor invalido")
                    else:
                        break
                except:
                    print("Valor inválido")
            while True:
                quantidade_arestas = input("Digite o quantidade de arestas: ")
                try:
                    print("Digite o par de vertice e seu peso no formato: index_vertice1 index_vertice2")
                    for _ in range(int(quantidade_arestas)):
                        while True:
                            vertice1,vertice2 = input("Aresta: ").split(' ')
                            try:
                                if int(vertice2) not in vertices.keys() or int(vertice1) not in vertices.keys():
                                    print("Aresta com vertice inexistente")
                                    print('Vertices(index,rotulo):', vertices)
                                    raise Exception
                                for aresta in arestas:
                                    if int(vertice1) == aresta[0] and int(vertice2) == aresta[1]:
                                        print("Aresta ja inserida")
                                        print(f'Arestas:{[[i[0],i[1]] for i in arestas]}')
                                        raise Exception
                                arestas.append([int(vertice1), int(vertice2), 1])
                                break
                            except:
                                print("Valor invalido")
                    else:
                        break
                except:
                    print("Valor inválido")
            exe2 = OrdenacaoTopologica(vertices=vertices, arestas=arestas)
            print("Grafo criado!")
            print('Vertices(index,rotulo):', vertices)
            print(f'Arestas:{[[i[0], i[1]] for i in arestas]}')
        print("#"*30)
        print("Saida do exercicio:")
        exe2.ordenacao_topolica()
        print("#"*30)

    if valor_selecionado == '3':
        if modo_construcao_grafo == '1':
            while True:
                try:
                    nome_arquivo = input('Digite o nome do arquivo: ')
                    exe3 = Kruskal(arquivo= nome_arquivo)
                    break
                except Exception as error:
                    print("Falha ao ler arquivo, digite novamente!")
                    print(error)
        else:
            vertices = {}
            arestas = []
            while True:
                quantidade_vertices = input("Digite o quantidade de vertices: ")
                try:
                    print("Digite o index do vertice e seu rótulo(sem espaços) no formato: index rótulo")
                    for _ in range(int(quantidade_vertices)):
                        while True:
                            index, rotulo = input("Vertice: ").split(' ')
                            try:
                                if int(index) in vertices.keys():
                                    print("Vertice inserido previamente")
                                    raise Exception
                                vertices[int(index)] = rotulo
                                break
                            except:
                                print("Valor invalido")
                    else:
                        break
                except:
                    print("Valor inválido")
            while True:
                quantidade_arestas = input("Digite o quantidade de arestas: ")
                try:
                    print("Digite o par de vertice e seu peso no formato: index_vertice1 index_vertice2")
                    for _ in range(int(quantidade_arestas)):
                        while True:
                            vertice1,vertice2 = input("Aresta: ").split(' ')
                            try:
                                if int(vertice2) not in vertices.keys() or int(vertice1) not in vertices.keys():
                                    print("Aresta com vertice inexistente")
                                    print('Vertices(index,rotulo):', vertices)
                                    raise Exception
                                for aresta in arestas:
                                    if int(vertice1) == aresta[0] and int(vertice2) == aresta[1]:
                                        print("Aresta ja inserida")
                                        print(f'Arestas:{[[i[0],i[1]] for i in arestas]}')
                                        raise Exception
                                arestas.append([int(vertice1), int(vertice2), 1])
                                break
                            except:
                                print("Valor invalido")
                    else:
                        break
                except:
                    print("Valor inválido")
            exe3 = Kruskal(vertices=vertices, arestas=arestas)
            print("Grafo criado!")
            print('Vertices(index,rotulo):', vertices)
            print(f'Arestas:{[[i[0], i[1]] for i in arestas]}')
        print("#"*30)
        print("Saida do exercicio:")
        exe3.get_arvore_geradora_minima_kruskal()
        print("#"*30)