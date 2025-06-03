def main():
    n = int(input())

    # 1 Bola (1) or (n)
    # 1 Possibilidade

    # 2 Bola
    # 1 Bola + 1 Bola (1)
    # 2 Bolas (1 < N < 4) (1)
    # 2 Possibilidades

    # 3 Bolas
    # 1 Bola + 1 Bola + 1 Bola (1)
    # 1 Bola + 2 Bolas (n - 1)
    # 2 Bolas + 1 Bola (n - 1)
    # 3 Bolas (1 < N < 4) (1)
    # 4 Possibilidades

    # 4 Bolas
    # 1 Bola + 1 Bola + 1 Bola + 1 Bola (1)
    # 1 Bola + 1 Bola + 2 Bolas (n - 1)
    # 2 Bolas + 1 Bola + 1 Bola (n - 1)
    # 1 Bola + 2 Bolas + 1 Bola (n - 1)
    # 2 Bolas + 2 Bolas (n - 2)
    # 1 Bola + 3 Bolas (n - 3)
    # 3 Bolas + 1 Bola (n - 3)
    # 7 Possibilidades

    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        if i - 1 >= 0:
            dp[i] += dp[i - 1]
        if i - 2 >= 0:
            dp[i] += dp[i - 2]
        if i - 3 >= 0:
            dp[i] += dp[i - 3]

    print(dp[n])
    
    return 0

if __name__ == "__main__":
    main()