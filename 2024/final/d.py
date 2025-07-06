def main():
    n = int(input())
    l = list(map(int, input().split()))

    t = -1

    for a in l:
       binario = bin(a)[2:]
       if len(binario) > t:
           t = len(binario)
    
    m = [[0 for _ in range(t)] for _ in range(n)]

    for i in range(n):
        a = l[i]
        binario = bin(a)[2:]
        tamanho = len(binario)

        for j in range(t - tamanho):
            binario = '0' + binario
        
        for j in range(t):
            m[i][j] = int(binario[j])
    
    end = []

    for i in range(t):
        s = 0

        for j in range(n):
            s += m[j][i]

        end.append(s)

    r = 0

    print(f"chave: ", end="")
    for i in range(t - 1, -1, -1):
        if end[i] > 0:
            print(f"{end[i]}*2^{i}{'+' if i > 0 else ''}", end="")
        r += end[i] * (2 ** i)

    print(f"={r}")

    return 0

if __name__ == "__main__":
    main()