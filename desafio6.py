
from mapa import mapa_romenia, heuristica_bucareste


def busca_a_estrela(inicio, objetivo, grafo, heuristica):
    fronteira = [(heuristica[inicio], 0, inicio, [inicio])]
    explorados = set()
    iteracoes = 0

    while fronteira:
        iteracoes += 1

        fronteira.sort(key=lambda no: no[0])
        f_atual, g_atual, cidade_atual, caminho = fronteira.pop(0)

        if cidade_atual == objetivo:
            return caminho, g_atual, iteracoes

        if cidade_atual in explorados:
            continue

        explorados.add(cidade_atual)

        for vizinho, custo_estrada in grafo.get(cidade_atual, []):
            if vizinho not in explorados:
                novo_g = g_atual + custo_estrada
                novo_f = novo_g + heuristica[vizinho]

                fronteira.append(
                    (novo_f, novo_g, vizinho, caminho + [vizinho])
                )

    return None, float('inf'), iteracoes


def mostrar_resultado(origem, caminho, custo, iteracoes):
    print(f'\nOrigem: {origem}')

    if caminho:
        print('Caminho:', ' -> '.join(caminho))
        print('Custo:', custo, 'km')
    else:
        print('Nenhum caminho encontrado.')

    print('Número de iterações:', iteracoes)


def main():
    objetivo = 'Bucharest'

    # Desafio 1: testar a heurística zero
    h_zero = {c: 0 for c in mapa_romenia}

    caminho, custo, iteracoes = busca_a_estrela(
        'Arad', objetivo, mapa_romenia, h_zero
    )

    print('=== Desafio 1: heurística zero ===')
    mostrar_resultado('Arad', caminho, custo, iteracoes)

    # Desafio 2: testar outras cidades de origem
    print('\n=== Desafio 2: outras cidades de origem ===')

    for origem in ['Lugoj', 'Mehadia', 'Eforie']:
        caminho, custo, iteracoes = busca_a_estrela(
            origem, objetivo, mapa_romenia, heuristica_bucareste
        )

        mostrar_resultado(origem, caminho, custo, iteracoes)


if __name__ == '__main__':
    main()
