from mapa import mapa_romenia

print("Cidades que têm exatamente 1 estrada:")

for cidade in mapa_romenia:
    quantidade = len(mapa_romenia[cidade])

    if quantidade == 1:
        print(cidade)
