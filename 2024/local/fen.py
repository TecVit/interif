def main():
    tabuleiro = str(input())
    tamanho = len(tabuleiro)
    
    for i in range(tamanho):
        if i == 0:
            print("|", end="")
            
        letra = tabuleiro[i]
        if letra == '/':
            print()
            print("|", end="")
            continue
        
        try:
            number = int(letra)
            for i in range(number):
                print(f" |", end="")
        except:
            letter = letra
            print(f"{letter}|", end="")
    
    return 0

if __name__ == "__main__":
    main()