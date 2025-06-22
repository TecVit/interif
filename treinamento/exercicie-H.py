# Problema H
# Ponte que Partiu

def enlaces(rede, n):
    tempo = 0
    descoberto = [-1] * n
    menor_alcance = [-1] * n
    resultado = []

    def buscando(u, pai):
        nonlocal tempo
        descoberto[u] = menor_alcance[u] = tempo
        tempo += 1

        for v in rede[u]:
            if v == pai: # Nao volta para o pai
                continue
            if descoberto[v] == -1:
                buscando(v, u) # Busca o vizinho
                menor_alcance[u] = min(menor_alcance[u], menor_alcance[v])
                if menor_alcance[v] > descoberto[u]:
                    resultado.append((min(u, v), max(u, v)))
            else:
                menor_alcance[u] = min(menor_alcance[u], descoberto[v])

    for i in range(n):
        if descoberto[i] == -1:
            buscando(i, -1)

    return len(resultado)


def main():
    n = int(input())
    rede = [[] for _ in range(n)]

    for _ in range(n):
        i = int(input())
        vizinhos = list(map(int, input().split()))

        for v in vizinhos:
            if v not in rede[i]:
                rede[i].append(v)
            if i not in rede[v]:
                rede[v].append(i)

    total = enlaces(rede, n)
    print(total)

if __name__ == "__main__":
    main()
