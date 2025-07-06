def main():
    x = int(input())
    y = int(input())
    ps = []

    for i in range(y):
        p = int(input())
        ps.append(p)
    
    t = sum(ps)
    target = t - x

    somas = {}

    for i in range(len(ps)):
        p = ps[i]

        if ps[i] in somas:
            res = [i + 1, somas[ps[i]] + 1]
            break

        somas[abs(target - p)] = i

    res.sort()

    print(*res)
    
    return 0

if __name__ == "__main__":
    main()