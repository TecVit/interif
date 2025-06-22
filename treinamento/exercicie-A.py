# Problema A
# Futebol na TV

def main():
    n = int(input())
    ts = [0] + list(map(int, input().split()))
    
    s = 0

    for i in range(n):
        t = ts[i]
        tf = ts[i+1]
        
        d = tf - t

        if d > 15:
            s += 15
            break
        else:
            s += d

    print(s)

    return 0

if __name__ == "__main__":
    main()