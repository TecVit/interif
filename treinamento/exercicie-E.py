# Problema E
# Xadrez

def main():
    while True:
        x1, y1, x2, y2 = map(int, input().split())
        
        # Acabou os casos de testes
        if x1 == y1 and y1 == x2 and x2 == y2 and y2 == 0:
            return 0
        
        if abs(x1 - x2) == abs(y1 - y2):
            print("Possible")
        else:
            print("Impossible")

    return 0

if __name__ == "__main__":
    main()