def main():
    f = -1
    
    x, y = map(int, input().split())
    cs = list(map(int, input().split()))

    n = len(cs)
    i = 0
    antenas = 0

    while i < n:

        j = i
        while j + 1 < n and cs[j + 1] <= cs[i] + y:
            j += 1

        antena = cs[j]
        antenas += 1

        i = j
        while i < n and cs[i] <= antena + y:
            i += 1

    print(antenas)

if __name__ == "__main__":
    main()