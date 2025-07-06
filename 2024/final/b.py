def main():
    x, y = map(int, input().split())
    numbers = list(map(int, input().split()))
    
    l, r = 0, y
    c = 0

    while r < x:
        next = numbers[r]
        filter = numbers[l:r]
        filter.sort()
        
        mediana = 0

        if y % 2 == 0:
            a = filter[(y // 2) - 1]
            b = filter[(y // 2)]
            mediana = (a + b) / 2
        else:
            mediana = filter[(y // 2)]
        
        if next >= 2 * mediana:
            c += 1
        
        l += 1
        r += 1
    
    print(c)

    return 0

if __name__ == "__main__":
    main()