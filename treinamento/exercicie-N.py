# Problema N
# Preços de Produtos

def primesOfN(n):
    primes = list()
    
    for i in range(2, n + 1):
        primo = True
        for j in range(2, int(i * (1 / 2)) + 1):
            if i % j == 0 and i != j:
                primo = False
                break
            
        if primo:
            primes.append(i)
            
    return primes

def main():
    x, y = map(int, input().split())
    
    primes = primesOfN(y)
    
    big = max([x] + primes)
    
    print(big)
    
    return 0
    
if __name__ == "__main__":
    main()