# Problema K
# Joilson, o Anti-Social

def main():
    x, y = map(int, input().split())
    
    menor = 9
    cadeira = 0

    cinema = []

    cinema.append([0] * (y + 2))
    for i in range(x):
        cinema.append([0] + list(map(int, input().split())) + [0])
    cinema.append([0] * (y + 2))

    cadeiras = list()

    for i in range(1, x + 1):
        for j in range(1, y + 1):
            if cinema[i][j] == 1:
                continue
            
            top = cinema[i-1][j-1] + cinema[i-1][j] + cinema[i-1][j+1]
            center = cinema[i][j-1] + cinema[i][j+1]
            bottom = cinema[i+1][j-1] + cinema[i+1][j] + cinema[i+1][j+1]

            total = top + center + bottom

            if total < menor:
                menor = total
                cadeira = ((i - 1) * y) + j
                cadeiras = [(cadeira, menor)]
            elif total == menor:
                menor = total
                cadeira = ((i - 1) * y) + j
                cadeiras.append((cadeira, -1))
    
    cadeiras.sort()

    for cadeira, menor in cadeiras:
        if menor != -1:
            print(menor)

        print(cadeira)

    return 0

if __name__ == "__main__":
    main()