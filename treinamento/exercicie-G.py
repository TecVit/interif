# Problema G
# Notação Forsyth-Edwards

def main():
    tabuleiro = str(input())
    numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    print('|', end="")

    for letra in tabuleiro:
        # Se letra for igual a '/'
        # Devemos pular a linha
        if letra == '/':
            print()
            print('|', end="")

        # Se a letra for um número
        # Vamos printar os N espaços q o número representa
        elif letra in numeros:
            for espacos in range(int(letra)):
                print(' |', end="")
        else:
            print(f"{letra}|", end="")

    return 0

if __name__ == "__main__":
    main()