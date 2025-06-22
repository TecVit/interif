# Problema C
# Loteria

def main():
    numeros = set(map(int, input().split()))

    total = {
        6: 0,
        5: 0,
        4: 0,
    }

    while True:
        aposta = list(map(int, input().split()))
        
        if aposta == [0, 0, 0, 0, 0, 0]:
            break
        
        acertos = 0

        for numero in aposta:
            if numero in numeros:
                acertos += 1

        if acertos in total:
            total[acertos] += 1

    print(6, total[6])
    print(5, total[5])
    print(4, total[4])

if __name__ == "__main__":
    main()