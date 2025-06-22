# Problema B
# Latinhas

def main():

    while True:
        n = int(input())
        if n == 0:
            break
        
        mr = float("-inf")
        g = 0

        for i in range(1, n + 1):
            p = int(input())
            if p > mr:
                mr = p
                g = i

        print(g)

    return 0

if __name__ == "__main__":
    main()