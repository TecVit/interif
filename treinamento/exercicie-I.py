# Problema I
# Campeonato de Boliche

def main():
    n = int(input())
    r = []

    for i in range(n):
        nome = input()
        sequencia = list(input())

        jogadas = []
        for ch in sequencia:
            if ch == 'X':
                jogadas.append(10)
            else:
                jogadas.append(int(ch))

        frames = []
        i = 0
        while len(frames) < 9:
            if jogadas[i] == 10:
                frames.append([10])
                i += 1
            else:
                frames.append([jogadas[i], jogadas[i+1]])
                i += 2

        frames.append(jogadas[i:])

        print(frames)

        pontuacoes = []
        total = 0
        for j in range(10):
            frame = frames[j]
            if j < 9:
                # strike
                if frame[0] == 10:
                    bonus = 0
                    if len(frames[j+1]) >= 2:
                        bonus = frames[j+1][0] + frames[j+1][1]
                    else:
                        bonus = frames[j+1][0]
                        if j+2 < 10:
                            bonus += frames[j+2][0]
                    pontos = 10 + bonus
                # spare
                elif sum(frame) == 10:
                    pontos = 10 + frames[j+1][0]
                else:
                    pontos = sum(frame)
            else:
                # frame final
                pontos = sum(frame)

            total += pontos
            pontuacoes.append(total)

        r.append((total, nome, pontuacoes))

    r.sort(key=lambda x: (-x[0], x[1]))

    for total, nome, pontuacoes in r:
        print(f"{nome} : ", end="")
        for p in pontuacoes:
            print(f"|{p}", end="")
        print(f"| Total = {total}")

    return 0

if __name__ == "__main__":
    main()