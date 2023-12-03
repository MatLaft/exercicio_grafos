from Edmons_karp import EdmonsKarp
from hopcroft_karp import HopcroftKarp
from coloracao import Coloracao


while True:
    print("Selecione um exercicio para testar")
    print("1- Edmonds-Karp")
    print("2- Hopcroft-Karp")
    print("3- Coloração de Vértices")
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
    print("Inserir um arquivo(deixar na mesma pasta que esse arquivo)")

    if valor_selecionado == '1':
        while True:
            try:
                nome_arquivo = input('Digite o nome do arquivo: ')
                exe1 = EdmonsKarp(arquivo= nome_arquivo)
                break
            except Exception as error:
                print("Falha ao ler arquivo, digite novamente!")
                print(error)
        while True:
            fonte, destino = input("Digite a fonte e destino do fluxo(index) separados por espaço: ").split(" ")
            if int(fonte) in exe1.vertices.keys() and int(destino) in exe1.vertices.keys():
                break
            else:
                print("Fonte ou destino não encontrados, digite novamnete!")

        print("#"*30)
        print("Saida do exercicio:")
        exe1.get_fluxo_maximo(int(fonte), int(destino))
        print("#"*30)

    if valor_selecionado == '2':
        while True:
            try:
                nome_arquivo = input('Digite o nome do arquivo: ')
                exe2 = HopcroftKarp(arquivo=nome_arquivo)
                break
            except Exception as error:
                print("Falha ao ler arquivo, digite novamente!")
                print(error)
        print("#"*30)
        print("Saida do exercicio:")
        exe2.get_emparelhamento()
        print("#"*30)

    if valor_selecionado == '3':
        while True:
            try:
                nome_arquivo = input('Digite o nome do arquivo: ')
                exe3 = Coloracao(arquivo=nome_arquivo)
                break
            except Exception as error:
                print("Falha ao ler arquivo, digite novamente!")
                print(error)
        print("#"*30)
        print("Saida do exercicio:")
        exe3.coloracao_minima()
        print("#"*30)