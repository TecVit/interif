def main():
    n = int(input())
    p = []

    for i in range(2, n + 1):
        primo = True
        for j in range(2, 12):
            if i % j == 0 and i != j:
                primo = False
                continue
        
        if primo:
            p.append(i)

    print(*p)

    return 0

if __name__ == "__main__":
    main()