# Estudar código gerado do ChatGPT

def main():
    P = int(input())
    usuarios = input().split()
    N = len(usuarios)

    seguidores = [list(map(int, input().split())) for _ in range(N)]

    pagerank = [1.0] * N

    for _ in range(P):
        novo_pr = [0.0] * N
        for i in range(N):
            for j in range(N):
                if seguidores[j][i] == 1 and j != i:
                    total_seguidos = sum(seguidores[j])
                    if total_seguidos > 0:
                        novo_pr[i] += pagerank[j] / total_seguidos
        pagerank = novo_pr

    resultado = sorted(enumerate(pagerank), key=lambda x: (-x[1], x[0]))

    for idx, pr in resultado:
        print(f"{usuarios[idx]}: {pr:.6f}")

if __name__ == "__main__":
    main()