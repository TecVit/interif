# Problema L
# Bolas de Tênis

def main():
    n = int(input()) 

    dp = [0] * (n + 1)

    dp[0] = 1

    if n >= 1:
        dp[1] = dp[0]
    
    if n >= 2:
        dp[2] = (dp[1] + dp[0])

    for i in range(3, n + 1):
        dp[i] = (dp[i-1] + dp[i-2] + dp[i-3])

    print(dp[n])

    return 0

if __name__ == "__main__":
    main()