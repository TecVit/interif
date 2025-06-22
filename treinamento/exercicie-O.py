# Problema O
# Tesouro

def produto_vetorial(a, b, c):
    ab_x = b[0] - a[0]
    ab_y = b[1] - a[1]
    ac_x = c[0] - a[0]
    ac_y = c[1] - a[1]

    return ab_x * ac_y - ab_y * ac_x

def main():
    n = int(input())

    for i in range(n):
        x, y = map(int, input().split())
        

    x, y = map(int, input().split())

    return 0

if __name__ == "__main__":
    main()