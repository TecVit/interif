def main():
    n, m = map(int, input().split())

    pista = [[-1 for _ in range(m + 2)]]

    for i in range(n):
        row = list(map(int, input().split()))
        pista.append([-1] + row + [-1])

    pista.append([-1 for _ in range(m + 2)])   

    # 1. Achar um ponto de partida
    # 2. Verificar se no sentido horário vai ser encontrado um 2
    # 3. Somar 1 no total de vezes q for encontrado

    x, y = 0, 0
    
    # (1)
    for i in range(1, n):
        j = pista[i].index(1)
        x, y = i, j
        break

    # (2) Sentidos
    # 0 - Cima
    # 1 - Direita
    # 2 - Baixo
    # 3 - Esquerda
    s, c = 0, 0

    for i in range(1, n):
        for j in range(1, m):
            pista[x][y] = 0

            cima = pista[x-1][y]
            direita = pista[x][y+1]
            baixo = pista[x+1][y]
            esquerda = pista[x][y-1]

            # (3) Adicionar 1 para cada vez que ter um perigo
            if cima == 2 and s == 0:
                c += 1
            elif direita == 2 and s == 1:
                c += 1
            elif baixo == 2 and s == 2:
                c += 1
            elif esquerda == 2 and s == 3:
                c += 1

            if cima == 1:
                x -= 1
                s = 0
            elif direita == 1:
                y += 1
                s = 1
            elif baixo == 1:
                x += 1
                s = 2
            elif esquerda == 1:
                y -= 1
                s = 3
    
    print(c)

    return 0

if __name__ == "__main__":
    main()