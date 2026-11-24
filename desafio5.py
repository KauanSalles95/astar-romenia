from mapa import mapa_romenia, heuristica_bucareste


def busca_a_estrela(inicio, objetivo, ordenar_por_h=False,
                    testar_ao_gerar=False):

    fronteira = [(heuristica_bucareste[inicio], 0, inicio, [inicio])]
    explorados = set()

    while fronteira:

        # Ordenação: por f (A*) ou somente por h (gulosa)
        if ordenar_por_h:
            fronteira.sort(
                key=lambda no: heuristica_bucareste[no[2]]
            )
        else:
            fronteira.sort(key=lambda no: no[0])

        f_atual, g_atual, cidade_atual, caminho = fronteira.pop(0)

        # Teste correto: quando retira o destino da fronteira
        if not testar_ao_gerar and cidade_atual == objetivo:
            return caminho, g_atual

        if cidade_atual in explorados:
            continue

        explorados.add(cidade_atual)

        for vizinho, custo_estrada in mapa_romenia[cidade_atual]:
            if vizinho not in explorados:
                novo_g = g_atual + custo_estrada

                # Teste incorreto para o segundo desafio:
                # verifica o destino assim que ele é gerado
                if testar_ao_gerar and vizinho == objetivo:
                    return caminho + [vizinho], novo_g

                novo_f = novo_g + heuristica_bucareste[vizinho]
                fronteira.append(
                    (novo_f, novo_g, vizinho, caminho + [vizinho])
                )

    return None, float('inf')


# TESTE ORIGINAL: A* correto
print('A* original:')
caminho, custo = busca_a_estrela('Arad', 'Bucharest')
print('Caminho:', ' -> '.join(caminho))
print('Custo:', custo, 'km')


# DESAFIO 1: busca gulosa (somente h)
print('\nDESAFIO 1 - Busca gulosa:')
caminho, custo = busca_a_estrela(
    'Arad', 'Bucharest', ordenar_por_h=True
)
print('Caminho:', ' -> '.join(caminho))
print('Custo:', custo, 'km')


# DESAFIO 2: testar objetivo ao gerar o vizinho
print('\nDESAFIO 2 - Teste de objetivo ao gerar:')
caminho, custo = busca_a_estrela(
    'Arad', 'Bucharest', testar_ao_gerar=True
)
print('Caminho:', ' -> '.join(caminho))
print('Custo:', custo, 'km')