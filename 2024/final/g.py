def main():
    b = int(input())
    caracters = str(input())
    conjunto = str(input())
    s = float(input())
    
    numero = ''

    for letra in conjunto:
        numero = numero + str(caracters.index(letra))

    print(f"{(int(numero, b) * s):.2f}")

    return 0

if __name__ == "__main__":
    main()