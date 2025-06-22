# Problema D
# PacMan

def main():
    linhas, colunas = map(int, input().split())

    tabuleiro = [['X' for _ in range(colunas + 2)]]

    for _ in range(linhas):
        linha = ['X']
        for _ in range(colunas):
            linha.append('*')
        linha.append('X')
        tabuleiro.append(linha)

    tabuleiro.append(['X' for _ in range(colunas + 2)])

    fantasmas = int(input())

    for _ in range(fantasmas):
        y, x = map(int, input().split())
        tabuleiro[y][x] = 'F'

    y, x = map(int, input().split())
    tabuleiro[y][x] = 'P'

    movimento = str(input())
    pontuacao = 0

    for sentido in movimento:
        py, px = 0, 0

        if sentido == 'L': # Leste (X + 1)
            px += 1
        elif sentido == 'S': # Sul (Y + 1)
            py += 1
        elif sentido == 'O': # Leste (X - 1)
            px -= 1
        elif sentido == 'N': # Norte (Y - 1)
            py -= 1

        local = tabuleiro[y + py][x + px]

        if local != 'X':
            y += py
            x += px

        if local == 'F': # Fantasma (Zerar pontuação)
            pontuacao = 0
        elif local == '*': # Moeda (Adicionar 1 na pontuação)
            pontuacao += 1
            tabuleiro[y][x] = ''
        
    print(pontuacao)

    return 0

if __name__ == "__main__":
    main()