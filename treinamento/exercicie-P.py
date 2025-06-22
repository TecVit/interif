# Estudando

import sys
sys.setrecursionlimit(10**7)

def euler(cidades, n, m):
    visitadas = [False]*(m+1)  # arestas visitadas (1-based)
    caminho = []
    
    # Grafo: cidades[u] = list of (v, cor, id_estrada)
    
    def dfs(u, cor_ultima):
        for i, (v, cor, id_estrada) in enumerate(cidades[u]):
            if not visitadas[id_estrada]:
                if cor != cor_ultima:
                    visitadas[id_estrada] = True
                    dfs(v, cor)
                    caminho.append(id_estrada)
    
    # Tentar iniciar em todas as cidades com grau > 0
    for start in range(n):
        if len(cidades[start]) == 0:
            continue
        caminho.clear()
        for i in range(m+1):
            visitadas[i] = False
        dfs(start, -1)
        if all(visitadas[1:]):  # todas as arestas usadas
            # Verificar cor primeira e ultima aresta
            if len(caminho) == m:
                cor_primeira = None
                cor_ultima = None
                # Encontrar cor da primeira e ultima aresta no caminho
                # Para isso, mapa id_estrada -> cor
                id_para_cor = {}
                for u in range(n):
                    for v, cor, id_estrada in cidades[u]:
                        id_para_cor[id_estrada] = cor
                cor_primeira = id_para_cor[caminho[-1]]
                cor_ultima = id_para_cor[caminho[0]]
                if cor_primeira != cor_ultima:
                    print(start+1)
                    print(" ".join(map(str, (caminho))))
                    return
    print(-1)


def main():
    n, m, k = map(int, input().split())
    cidades = [[] for _ in range(n)]

    for id_estrada in range(1, m+1):
        i, j, c = map(int, input().split())
        i -= 1
        j -= 1
        cidades[i].append((j, c, id_estrada))
        cidades[j].append((i, c, id_estrada))

    # Verifica se grafo tem grau par para todas as cidades
    for u in range(n):
        if len(cidades[u]) % 2 != 0:
            print(-1)
            return

    euler(cidades, n, m)

if __name__ == "__main__":
    main()