# Problema J
# Salto em Distância

def main():
    competidores = int(input())
    saltos = int(input())

    mr_distancia = float("-inf")
    nome_mr = ''

    for i in range(competidores):
        nome = str(input())

        for j in range(saltos):
            leitura = [str(x) for x in input().split()]
            distancia = float(leitura[0])
            
            if len(leitura) < 2:
                if distancia > mr_distancia:
                    mr_distancia = distancia
                    nome_mr = nome

    print(nome_mr)
    print(f"{mr_distancia:.2f}")

    return 0

if __name__ == "__main__":
    main()