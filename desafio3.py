from mapa import mapa_romenia, heuristica_bucareste


# DESAFIO 1 - Expandir Sibiu à mão


# Fronteira restante depois de retirar Sibiu
fronteira = [
    (447, 118, 'Timisoara', ['Arad', 'Timisoara']),
    (449, 75, 'Zerind', ['Arad', 'Zerind'])
]

# Dados do nó Sibiu
g_atual = 140
cidade_atual = 'Sibiu'
caminho = ['Arad', 'Sibiu']

# Gerar os filhos de Sibiu
for vizinho, custo_estrada in mapa_romenia[cidade_atual]:
    novo_g = g_atual + custo_estrada
    novo_h = heuristica_bucareste[vizinho]
    novo_f = novo_g + novo_h
    novo_caminho = caminho + [vizinho]

    fronteira.append((novo_f, novo_g, vizinho, novo_caminho))

# Ordenar pelo f (posição 0)
fronteira.sort(key=lambda no: no[0])

print('DESAFIO 1 - Fronteira depois de expandir Sibiu:')
for no in fronteira:
    print(no)

print()
print('Por que Arad apareceu?')
print('Porque existe uma estrada de Sibiu de volta para Arad.')


# Ordenar pelo g

fronteira2 = []

# Gerar os nós vizinhos de Arad
for vizinho, custo_estrada in mapa_romenia['Arad']:
    novo_g = custo_estrada
    novo_h = heuristica_bucareste[vizinho]
    novo_f = novo_g + novo_h
    novo_caminho = ['Arad', vizinho]

    fronteira2.append((novo_f, novo_g, vizinho, novo_caminho))

# Ordenar pelo g (posição 1)
fronteira2.sort(key=lambda no: no[1])

print()
print('DESAFIO 2 - Fronteira ordenada pelo g:')
for no in fronteira2:
    print(no)

proximo = fronteira2.pop(0)

print('Primeiro nó que sai:', proximo)
